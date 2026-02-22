import pandas as pd
from datetime import datetime
import os

LOG_FILE = "scam_log.csv"

def log_message(category, risk_score):
    row = {
        "timestamp": datetime.now(),
        "category": category,
        "risk_score": risk_score
    }
    df = pd.DataFrame([row])

    if os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_FILE, mode="w", header=True, index=False)