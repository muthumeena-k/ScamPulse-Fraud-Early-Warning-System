# ScamPulse – Community Fraud Early Warning System
## Live Demo

### Telegram Safety Response
![Bot Demo](bot.png)

### Community Fraud Dashboard
![Dashboard](dashboard.png)
ScamPulse is a real-time digital fraud awareness platform designed to help users identify scam SMS or WhatsApp messages before they act on them.Designed especially for first-time digital payment users and elderly individuals who are most vulnerable to social engineering fraud.

Users forward suspicious messages to a Telegram bot.  
The system analyzes the message using a hybrid approach:
- Rule-based fraud indicators (OTP requests, urgency, impersonation)
- Machine learning NLP spam classifier

The bot returns:
- A clear warning
- Explanation of why the message is dangerous
- Safety guidance

Each analyzed message is logged and visualized on a Streamlit dashboard to detect active scam campaigns in the community.

## Technologies
Python, Scikit-learn, Pandas, Streamlit, Telegram Bot API

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Run the Telegram bot
python bot.py

3. Run the dashboard
streamlit run dashboard.py
## System Workflow

1. User forwards a suspicious SMS/WhatsApp message to the Telegram bot
2. The analyzer processes the message using:
   - Rule-based fraud indicators (OTP request, urgency, impersonation)
   - Machine learning NLP classifier
3. The system assigns a risk level and explains the warning signs in simple language
4. The message category and timestamp are logged
5. The Streamlit dashboard aggregates community reports
6. Active scam campaigns are identified through trend monitoring
## Limitations and Responsible Use

This system is an assistive warning tool and not a legal fraud verification service.
Predictions are based on language patterns and known scam indicators, so false positives
and false negatives are possible.

The platform does not collect personal identity information and stores only anonymized
message content with timestamps for trend analysis.

Users should always confirm with official institutions before taking action.
