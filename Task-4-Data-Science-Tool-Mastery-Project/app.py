import os
import joblib
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="E-Commerce Churn Prediction API")

templates = Jinja2Templates(directory="templates")

# Model path resolution
MODEL_PATH = "models/churn_production_pipeline.joblib"
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = "../models/churn_production_pipeline.joblib"

pipeline = joblib.load(MODEL_PATH)

# Model ke feature names auto-detect karein
try:
    expected_features = pipeline.feature_names_in_.tolist()
except AttributeError:
    expected_features = pipeline.named_steps['model'].feature_name_


class CustomerData(BaseModel):
    Customer_Service_Calls: float
    Cart_Abandonment_Rate: float
    High_Cart_Friction: float
    Days_Since_Last_Purchase: float
    Digital_Engagement_Composite: float
    Engagement_Friction_Ratio: float = 0.5
    Wishlist_Conversion_Ratio: float = 0.5
    Annual_Monetary_Velocity: float = 1000.0
    Spend_Per_Purchase: float = 50.0
    Is_Dormant_90Days: int = 0
    Total_Purchases: float = 20.0
    Average_Order_Value: float = 50.0
    Membership_Years: float = 2.0
    Discount_Usage_Rate: float = 0.2
    Returns_Rate: float = 0.05
    Payment_Method_Diversity: float = 2.0
    Credit_Balance: float = 100.0
    Product_Reviews_Written: float = 3.0


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Compatible with both new and old starlette/jinja2 versions
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": None}
    )


@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    customer_service_calls: float = Form(...),
    cart_abandonment_rate: float = Form(...),
    high_cart_friction: float = Form(...),
    days_since_last_purchase: float = Form(...),
    digital_engagement_composite: float = Form(...)
):
    # Base dictionary
    data = {
        'Customer_Service_Calls': customer_service_calls,
        'Cart_Abandonment_Rate': cart_abandonment_rate,
        'High_Cart_Friction': high_cart_friction,
        'Days_Since_Last_Purchase': days_since_last_purchase,
        'Digital_Engagement_Composite': digital_engagement_composite,
        'Engagement_Friction_Ratio': 0.5,
        'Wishlist_Conversion_Ratio': 0.5,
        'Annual_Monetary_Velocity': 1000.0,
        'Spend_Per_Purchase': 50.0,
        'Is_Dormant_90Days': 1 if days_since_last_purchase > 90 else 0,
        'Total_Purchases': 20.0,
        'Average_Order_Value': 50.0,
        'Membership_Years': 2.0,
        'Discount_Usage_Rate': 0.2,
        'Returns_Rate': 0.05,
        'Payment_Method_Diversity': 2.0,
        'Credit_Balance': 100.0,
        'Product_Reviews_Written': 3.0
    }

    # Model ke trained column order ke hisab se DataFrame banayein
    df_input = pd.DataFrame([data])
    if expected_features:
        df_input = df_input.reindex(columns=expected_features, fill_value=0.0)

    # Prediction
    prob = pipeline.predict_proba(df_input)[0, 1]
    prediction = int(prob >= 0.5)

    status = "High Risk of Churn" if prediction == 1 else "Likely Retained"
    risk_color = "#e53e3e" if prediction == 1 else "#38a169"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": {
                "status": status,
                "probability": f"{prob * 100:.1f}%",
                "color": risk_color
            }
        }
    )


@app.post("/predict")
def predict_api(payload: CustomerData):
    df_input = pd.DataFrame([payload.model_dump()])
    if expected_features:
        df_input = df_input.reindex(columns=expected_features, fill_value=0.0)
        
    prob = pipeline.predict_proba(df_input)[0, 1]
    return {
        "churn_prediction": int(prob >= 0.5),
        "churn_probability": round(float(prob), 4)
    }