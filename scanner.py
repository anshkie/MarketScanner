import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
SYMBOLS = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "LT.NS", "WIPRO.NS", "BAJFINANCE.NS", "ITC.NS"]
load_dotenv()
def fetch_data(symbols=SYMBOLS):
    data = []
    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="2d")
            if len(hist) >= 2:
                prev_close = hist['Close'].iloc[-2]
                last_price = hist['Close'].iloc[-1]
                volume = hist['Volume'].iloc[-1]
                change = last_price - prev_close
                pct_change = (change / prev_close) * 100
                data.append({
                    "Symbol": symbol.replace(".NS", ""),
                    "LTP": round(last_price, 2),
                    "Change": round(change, 2),
                    "Change (%)": round(pct_change, 2),
                    "Volume": int(volume)
                })
        except Exception as e:
            print(f"Error for {symbol}: {e}")
    return pd.DataFrame(data)

def get_top_gainers():
    df = fetch_data()
    return df.sort_values("Change (%)", ascending=False).head(10)

def get_top_losers():
    df = fetch_data()
    return df.sort_values("Change (%)", ascending=True).head(10)

def get_volume_shockers():
    df = fetch_data()
    return df.sort_values("Volume", ascending=False).head(10)

def filter_custom_stocks():
    df = fetch_data()
    return df[(df["LTP"] > 200) & (df["Change (%)"] > 2)]

def send_email_alert(df):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = MIMEMultipart()
    msg["Subject"] = "📈 NSE Market Scanner Alert"
    msg["From"] = sender
    msg["To"] = receiver

    html = df.to_html(index=False)
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        st.success("✅ Email sent successfully to your inbox!")
        print("Email sent!")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
        print("Failed to send email:", e)

def plot_price_chart(symbol):
    df = yf.Ticker(symbol).history(period="5d", interval="1h")
    fig = px.line(df, x=df.index, y="Close", title=f"{symbol} Price Chart")
    return fig

def plot_histogram(df, col="Change (%)"):
    fig = px.histogram(df, x=col, nbins=10, title=f"{col} Distribution")
    return fig
