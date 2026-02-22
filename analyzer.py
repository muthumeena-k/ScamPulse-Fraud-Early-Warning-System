import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def analyze_message(text):
    text_lower = text.lower()
    reasons = []
    rule_score = 0

    # OTP detection
    if "otp" in text_lower:
        reasons.append("Message requests OTP")
        rule_score += 0.3

    # urgency language
    urgent_words = ["urgent", "immediately", "now", "blocked", "suspended", "verify"]
    if any(word in text_lower for word in urgent_words):
        reasons.append("Creates urgency pressure")
        rule_score += 0.2

    # bank impersonation
    bank_words = ["bank", "account", "kyc", "rbi"]
    if any(word in text_lower for word in bank_words):
        reasons.append("Possible bank impersonation")
        category = "Banking Scam"
        rule_score += 0.3
    else:
        category = "General Scam"

    # ML model prediction
    vec = vectorizer.transform([text])
    ai_prob = model.predict_proba(vec)[0][1]

    final_score = min(ai_prob + rule_score, 1)

    return final_score, category, reasons