# ============================================
# 🏥 Healthcare Critical Analysis Dashboard
# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Page setup ---
st.set_page_config(page_title="🏥 Healthcare Critical Analysis", layout="wide")

# =========================================================
# 📦 Load Data
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("PATIENTS_SILVER.csv")

    # Convert date columns
    if 'birthdate' in df.columns:
        df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')
    if 'deathdate' in df.columns:
        df['deathdate'] = pd.to_datetime(df['deathdate'], errors='coerce')

    # Convert numeric columns
    for col in ['healthcare_expenses', 'healthcare_coverage', 'lat', 'lon']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


df = load_data()

# =========================================================
# 🧭 Navigation Tabs
# =========================================================
st.title("🏥 Healthcare Critical Analysis Dashboard")
tabs = st.tabs(["🏠 Home", "👩‍⚕️ Demographics", "💰 Financial", "🌍 Geography", "🧮 Data Explorer"])


# =========================================================
# 🏠 HOME TAB — Key Metrics
# =========================================================
with tabs[0]:
    st.subheader("📊 Key Metrics")

    total_patients = len(df)
    male_patients = df[df['gender'].str.upper() == 'M'].shape[0] if 'gender' in df.columns else 0
    female_patients = df[df['gender'].str.upper() == 'F'].shape[0] if 'gender' in df.columns else 0
    avg_expenses = df['healthcare_expenses'].mean() if 'healthcare_expenses' in df.columns else 0
    avg_coverage = df['healthcare_coverage'].mean() if 'healthcare_coverage' in df.columns else 0

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Patients", total_patients)
    col2.metric("Male Patients", male_patients)
    col3.metric("Female Patients", female_patients)
    col4.metric("Avg Healthcare Expenses", f"${avg_expenses:,.2f}")
    col5.metric("Avg Coverage", f"${avg_coverage:,.2f}")

    st.markdown("---")
    st.success("✅ Dashboard loaded successfully — all visualizations generated.")


# =========================================================
# 👩‍⚕️ DEMOGRAPHICS TAB
# =========================================================
with tabs[1]:
    st.header("👩‍⚕️ Demographics Overview")

    # Gender distribution
    if 'gender' in df.columns:
        gender_counts = df['gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        fig_gender = px.pie(gender_counts, names='Gender', values='Count', title="Gender Distribution")
        st.plotly_chart(fig_gender, use_container_width=True)

    # Race distribution
    if 'race' in df.columns:
        race_counts = df['race'].value_counts().reset_index()
        race_counts.columns = ['Race', 'Count']
        fig_race = px.bar(race_counts, x='Race', y='Count', title="Race Distribution", color='Race')
        st.plotly_chart(fig_race, use_container_width=True)

    # Marital Status
    if 'marital' in df.columns:
        marital_counts = df['marital'].value_counts().reset_index()
        marital_counts.columns = ['Marital Status', 'Count']
        fig_marital = px.bar(marital_counts, x='Marital Status', y='Count',
                            title="Marital Status Distribution", color='Marital Status')
        st.plotly_chart(fig_marital, use_container_width=True)

    # Age distribution
    if 'birthdate' in df.columns:
        today = datetime.today()
        df['age'] = df['birthdate'].apply(lambda x: (today - x).days // 365 if pd.notnull(x) else None)
        fig_age = px.histogram(df, x='age', nbins=40, title="Age Distribution of Patients",
                            color_discrete_sequence=["#EF553B"])
        st.plotly_chart(fig_age, use_container_width=True)


# =========================================================
# 💰 FINANCIAL TAB
# =========================================================
with tabs[2]:
    st.header("💰 Financial Insights")

    if {'healthcare_expenses', 'healthcare_coverage'}.issubset(df.columns):
        df_fin = df.dropna(subset=['healthcare_expenses', 'healthcare_coverage'])

        # Expenses distribution
        fig_expenses = px.histogram(df_fin, x='healthcare_expenses', nbins=40,
                                    title="Distribution of Healthcare Expenses")
        st.plotly_chart(fig_expenses, use_container_width=True)

        # Scatter: Coverage vs Expenses
        fig_scatter = px.scatter(
            df_fin,
            x='healthcare_coverage',
            y='healthcare_expenses',
            color='gender',
            title="Healthcare Coverage vs Expenses by Gender",
            trendline="ols"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Average by gender
        avg_by_gender = df_fin.groupby('gender')[['healthcare_expenses', 'healthcare_coverage']].mean().reset_index()
        fig_bar = px.bar(avg_by_gender, x='gender', y='healthcare_expenses',
                        title="Average Healthcare Expenses by Gender", color='gender')
        st.plotly_chart(fig_bar, use_container_width=True)


# =========================================================
# 🌍 GEOGRAPHY TAB
# =========================================================
with tabs[3]:
    st.header("🌍 Geographic Distribution")

    if {'lat', 'lon'}.issubset(df.columns):
        df_geo = df.dropna(subset=['lat', 'lon'])
        if not df_geo.empty:
            fig_map = px.scatter_mapbox(
                df_geo,
                lat='lat',
                lon='lon',
                hover_name='city' if 'city' in df.columns else None,
                hover_data=['state', 'gender', 'healthcare_expenses'] if 'state' in df.columns else None,
                color='state' if 'state' in df.columns else None,
                zoom=3,
                title="Patient Distribution by State",
            )
            fig_map.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.warning("⚠️ No geographic coordinates available for map visualization.")


# =========================================================
# 🧮 DATA EXPLORER TAB
# =========================================================
with tabs[4]:
    st.header("🧮 Data Explorer")

    # Dataset Overview
    col1, col2 = st.columns(2)
    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))

    # Correlation Heatmap Only
    st.markdown("### 🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        corr = numeric_df.corr()
        fig_corr = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation between Numerical Columns",
            color_continuous_scale="RdBu_r"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.warning("⚠️ No numeric columns found for correlation heatmap.")
