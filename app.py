import streamlit as st
from scanner import (
    get_top_gainers, get_top_losers,
    get_volume_shockers, filter_custom_stocks,
    send_email_alert, plot_price_chart, plot_histogram
)

st.set_page_config(page_title="NSE Market Scanner", layout="wide")
st.title("📈 NSE Market Scanner")

st.sidebar.title("Scanner Filters")
option = st.sidebar.selectbox("Choose a Screener", [
    "Top Gainers", "Top Losers", "Volume Shockers", "Custom Filter",
    "Filter by Sector", "With Moving Averages", "Sector + Moving Avg"
])

show_charts = st.sidebar.checkbox("Show Line Charts")
show_histogram = st.sidebar.checkbox("Show Histogram")
send_alert = st.sidebar.checkbox("Send Email Alert")

# Load data
if option == "Top Gainers":
    st.subheader("🚀 Top Gainers")
    df = get_top_gainers()
elif option == "Top Losers":
    st.subheader("📉 Top Losers")
    df = get_top_losers()
elif option == "Volume Shockers":
    st.subheader("📊 Volume Shockers")
    df = get_volume_shockers()
elif option == "Custom Filter":
    st.subheader("🔎 Custom Filter: LTP > 200 and Change > 2%")
    df = filter_custom_stocks()
elif option == "Filter by Sector":
    st.subheader("🏢 Filter by Sector")
    sector = st.sidebar.selectbox("Select Sector", ["IT", "Banking", "FMCG"])
    df = filter_custom_stocks()  # Simulated sector filtering
    df = df[df['Symbol'].str.contains("TCS|INFY|WIPRO") if sector == "IT" else ""]
elif option == "With Moving Averages":
    st.subheader("📉 Stocks with MA (SMA 5 vs 20)")
    df = filter_custom_stocks()
    df["SMA_5"] = df["LTP"].rolling(5).mean()
    df["SMA_20"] = df["LTP"].rolling(20).mean()
elif option == "Sector + Moving Avg":
    st.subheader("📊 Filter by Sector + MA")
    sector = st.sidebar.selectbox("Select Sector", ["IT", "Banking", "FMCG"])
    df = filter_custom_stocks()  # Simulated
    df = df[df['Symbol'].str.contains("TCS|INFY|WIPRO") if sector == "IT" else ""]
    df["SMA_5"] = df["LTP"].rolling(5).mean()
    df["SMA_20"] = df["LTP"].rolling(20).mean()

# Display table
st.dataframe(df)

# CSV Download
st.download_button("📥 Download CSV", df.to_csv(index=False), "scanner_output.csv", "text/csv")

# Optional: Email alert
if send_alert:
    st.success("📧 Sending alert to your email...")
    send_email_alert(df)

# Optional: Show charts
if show_charts:
    for symbol in df["Symbol"].head(5):  # Limit to 5 for speed
        st.plotly_chart(plot_price_chart(symbol + ".NS"))

if show_histogram:
    st.plotly_chart(plot_histogram(df, col="Change (%)"))
    st.plotly_chart(plot_histogram(df, col="Volume"))
