# 📈 NSE Market Scanner

A Streamlit web app to screen and analyze stocks from the NSE (National Stock Exchange) using various filters like top gainers, top losers, volume shockers, and technical indicators.

LIVE DEMO : https://marketscanner-keakz7fafvxiednjhp2tkn.streamlit.app/

## 🚀 Features

- Top Gainers & Losers  
- Volume Shockers  
- Custom Filters (LTP > 200 & Change > 2%)  
- Sector-based filtering (IT, Banking, FMCG)  
- Moving Average crossover detection (SMA 5 vs SMA 20)  
- Combined Sector + Moving Average filter  
- Interactive Price Charts and Histograms  
- CSV Export of results  
- 📧 Email Alerts (via Gmail SMTP)

---
## 🧰 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Data Processing:** `pandas`, `numpy`  
- **Email Service:** `smtplib`, `email`  
- **Visualization:** `plotly`  
- **Environment Management:** `python-dotenv`  
- **Language:** Python 3.x
## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/anshkie/MarketScanner.git
cd nse-market-scanner
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env file
env
Copy
Edit
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@example.com
⚠️ Note: Use a Gmail App Password if you're using 2-Step Verification.

▶️ Running the App
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.

📦 File Structure
bash
Copy
Edit
nse-market-scanner/
├── app.py               # Main Streamlit app
├── scanner.py           # Core logic and utilities
├── requirements.txt     # Python dependencies
├── .env                 # Secret email credentials (not tracked)
└── README.md
📬 Email Alerts
Enable the "Send Email Alert" checkbox in the sidebar.

Sends filtered stocks as an HTML table to your configured email address.

🛡️ Security Notes
Keep your .env file secret.

It should be listed in .gitignore.

Never hardcode email credentials in source files.

Use App Passwords instead of your main Gmail password.

✨ Future Ideas
Add more sectors and filters

Live price updates

