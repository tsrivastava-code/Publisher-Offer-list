import pandas as pd
import streamlit as st
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Affiliate Offers Dashboard", layout="wide")

# ----------------------------
# Heading
# ----------------------------
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="
            font-size: 52px;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;">
            Affiliate Offers Dashboard
        </h1>
        <p style="
            font-size: 18px;
            font-weight: 400;
            color: #e0e0e0;
            margin-top: 0;">
            Comprehensive overview of all affiliate marketing opportunities
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Placards CSS
# ----------------------------
st.markdown("""
    <style>
        .placards-row {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-bottom: 25px;
        }
        .placard {
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: #ffffff;
            width: 220px;
            height: 120px;
            padding: 15px;
            border-radius: 18px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.3);
            transition: transform 0.2s ease-in-out;
        }
        .placard:hover {
            transform: translateY(-6px);
            box-shadow: 0 8px 22px rgba(0,0,0,0.4);
        }
        .placard span.value {
            font-size: 22px;
            font-weight: 700;
            margin-top: 6px;
        }
        h2.section-heading {
            margin-top: 25px;
            margin-bottom: 5px;
            font-size: 24px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Default File Path
# ----------------------------
DEFAULT_FILE = "Publisher - Active Offer List Sep'25.xlsx"

# ----------------------------
# Load Data
# ----------------------------
def load_data(file_path):
    return pd.read_excel(file_path)

df = None
if os.path.exists(DEFAULT_FILE):
    df = load_data(DEFAULT_FILE)
    if st.button("Refresh Data"):
        df = load_data(DEFAULT_FILE)
else:
    st.warning(f"⚠️ Default file '{DEFAULT_FILE}' not found. Please upload one.")

# ----------------------------
# Dashboard Logic
# ----------------------------
if df is not None:

    # Utility: find column ignoring case
    def find_col(df, target):
        for col in df.columns:
            if col.strip().lower() == target.lower():
                return col
        return None

    geo_col = find_col(df, "Region")
    agency_col = find_col(df, "Agency Access")
    cap_col = find_col(df, "Current Cap")
    offer_col = find_col(df, "Offer")
    campaign_type_col = find_col(df, "Campaign Type")

    # Placards
    total_offers = len(df)
    active_offers = len(df[df[cap_col].astype(str).str.lower() == "yes"]) if cap_col else 0
    geos_total = 75   # Hardcoded
    current_month = "October 2025"

    st.markdown(
        f"""
        <div class="placards-row">
            <div class="placard">📦 <br> Total Offers <br><span class="value">{total_offers}</span></div>
            <div class="placard">✅ <br> Active Offers <br><span class="value">{active_offers}</span></div>
            <div class="placard">🌍 <br> GEOs Offered <br><span class="value">{geos_total}</span></div>
            <div class="placard">🗓️ <br> Current Month <br><span class="value">{current_month}</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ----------------------------
    # Sidebar (Search → Filters → Brief)
    # ----------------------------
    with st.sidebar:

        # 🔍 Search bar on top
        search_term = st.text_input(" Search Offer", "")

        # 🔎 Filters in expander
        with st.expander("Filters", expanded=False):
            if geo_col:
                geo_list = df[geo_col].dropna().unique().tolist()
                geo_filter = st.selectbox("Select Region", options=["All"] + geo_list)
                if geo_filter != "All":
                    df = df[df[geo_col] == geo_filter]

            if agency_col:
                agency_list = df[agency_col].dropna().unique().tolist()
                agency_filter = st.selectbox("Select Agency Access", options=["All"] + agency_list)
                if agency_filter != "All":
                    df = df[df[agency_col] == agency_filter]

            if cap_col:
                cap_list = df[cap_col].dropna().unique().tolist()
                cap_filter = st.selectbox("Select Current Cap", options=["All"] + cap_list)
                if cap_filter != "All":
                    df = df[df[cap_col] == cap_filter]

            if campaign_type_col:
                campaign_type_list = df[campaign_type_col].dropna().unique().tolist()
                campaign_type_filter = st.selectbox("Select Campaign Type", options=["All"] + campaign_type_list)
                if campaign_type_filter != "All":
                    df = df[df[campaign_type_col] == campaign_type_filter]
                     
        # 📑 View Brief at the bottom
        if offer_col:
            st.markdown('<h2 class="section-heading">View Offer Brief</h2>', unsafe_allow_html=True)
            offer_list = df[offer_col].dropna().unique().tolist()
            selected_offer = st.selectbox("Choose an Offer", ["None"] + offer_list)

            if selected_offer != "None":
                row_data = df[df[offer_col].astype(str) == str(selected_offer)]
                if not row_data.empty:
                    row = row_data.iloc[0]
                    brief_df = pd.DataFrame({
                        "Field": row.index,
                        "Value": row.values
                    })
                    st.dataframe(brief_df, use_container_width=True)

    # Apply search filter last
    if search_term and offer_col:
        df = df[df[offer_col].astype(str).str.contains(search_term, case=False, na=False)]

    # ----------------------------
    # Top 5 Offers of the Month (comes first now)
    # ----------------------------
    st.markdown('<h2 class="section-heading">Top 5 Offers of the Month</h2>', unsafe_allow_html=True)

    top_offers = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "Offer Name": [
            "TBD ",
            "TBD",
            "TBD",
            "TBD",
            "TBD"
        ],
        "GEO": ["TBD", "TBD", "TBD", "TBD", "TBD"],
        "Payout ($)": [0, 0, 0, 0, 0],
        "Cap": ["NIL", "NIL", "NIL", "NIL", "NIL"]
    })

    st.dataframe(top_offers.style.hide(axis="index"), use_container_width=True)

    # ----------------------------
    # Filtered Campaign Data (comes after Top 5)
    # ----------------------------
    st.markdown('<h2 class="section-heading">Filtered Campaign Data</h2>', unsafe_allow_html=True)
    st.dataframe(df.style.hide(axis="index"), use_container_width=True)

