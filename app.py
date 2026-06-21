import requests
import streamlit as st

st.set_page_config(page_title="Premium Sports Analytics", page_icon="📊", layout="centered")

def fetch_sports_data():
    url = "https://quotes-api-self.vercel.app/api/sports/fixtures"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get("data", [])
        return []
    except Exception:
        return []

st.title("🏆 Premium Sports Insights")
st.subheader("Real-Time Pre-Match Analytical Reports")
st.write("---")

with st.spinner("Analyzing current statistical variations..."):
    fixtures = fetch_sports_data()

if not fixtures:
    st.info("No premium statistical anomalies detected in current matches. Check back shortly.")
else:
    for item in fixtures[:5]:
        home = item.get("homeTeam", "Home")
        away = item.get("awayTeam", "Away")
        prob = item.get("probability", "N/A")
        insight = item.get("insight", "Balanced fixture expected based on recent historical form.")
        
        with st.container():
            st.markdown(f"### ⚽ {home} vs {away}")
            st.metric(label="Value Probability Matching Factor", value=f"{prob}")
            st.markdown(f"💡 **Data Insight:** {insight}")
            st.write("---")

st.caption("Data engines cycle and update automatically.")
