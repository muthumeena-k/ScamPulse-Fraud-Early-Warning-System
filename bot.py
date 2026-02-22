import pickle
from logger import log_message
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Load trained AI model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def analyze_message(text):
    vec = vectorizer.transform([text])
    ai_prob = model.predict_proba(vec)[0][1]

    text_lower = text.lower()
    rule_score = 0
    reasons = []
    category = "General Suspicious"

    if "otp" in text_lower:
        rule_score += 0.4
        reasons.append("Message requests OTP")

    if "bank" in text_lower or "account" in text_lower:
        rule_score += 0.3
        reasons.append("Possible bank impersonation")

    if "urgent" in text_lower or "immediately" in text_lower:
        rule_score += 0.2
        reasons.append("Creates urgency pressure")

    if "click" in text_lower or "http" in text_lower or "link" in text_lower:
        rule_score += 0.3
        reasons.append("Contains suspicious link")

    if "delivery" in text_lower or "courier" in text_lower:
        category = "Delivery Scam"
    elif "bank" in text_lower:
        category = "Banking Scam"
    elif "lottery" in text_lower or "won" in text_lower:
        category = "Reward Scam"

    final_score = min(ai_prob + rule_score, 1)
    return final_score, category, reasons


TOKEN = "7953905477:AAGaWhv7PweLghDZMEbc2m1T7P2vyn7Rbfs"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    score, category, reasons = analyze_message(user_text)
    log_message(category, score)

    if score > 0.7:
        decision = "Do NOT trust this message. It is very likely a scam."
    elif score > 0.4:
        decision = "This message looks suspicious. Verify independently before taking action."
    else:
        decision = "No major warning signs detected, but remain cautious."

    reason_text = "\n• ".join(reasons)

    reply = f"""
* ScamPulse Safety Check*

* Assessment:*  
*{decision}*

* Message Type:*  
{category}

* Warning Signs Detected:*  
• {reason_text}

* Recommended Actions:*  
• Never share OTP or passwords  
• Do not click links from unknown senders  
• Contact the organization using its official website/number  
• Report fraud at *1930* or *cybercrime.gov.in*

_Important: Scammers often create urgency to force quick decisions._
"""

    await update.message.reply_text(reply, parse_mode="Markdown")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()