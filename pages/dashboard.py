
import streamlit as st
import pandas as pd
import sqlite3 as sq
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.header("Project Dashboard")

#------------------------------------------
# Database Connection and Data Loading
#------------------------------------------
def create_connection():
    conn = sq.connect("construction.db")
    return conn

def load_data():
    with sq.connect("construction.db") as conn:
        entries = pd.read_sql_query("SELECT * FROM entries", conn)
        inspections = pd.read_sql_query("SELECT * FROM inspections", conn)
        timecards = pd.read_sql_query("SELECT * FROM timecards", conn)
        notes = pd.read_sql_query("SELECT * FROM notes", conn)
    return entries, inspections, timecards, notes

entries_df, inspections_df, timecards_df, notes_df = load_data()

#------------------------------------------
# Data Filtering by Project and Date
#------------------------------------------
def filter_by_project(df, project):
    if df.empty or not project or "project" not in df.columns:
        return df
    return df[df["project"] == project].copy()

if not entries_df.empty:
    selected_project = st.selectbox("Select Project", entries_df["project"].unique())
else:
    selected_project = None

dfs = [entries_df, inspections_df, timecards_df, notes_df]
dfs = [filter_by_project(df, selected_project) for df in dfs]
entries_df, inspections_df, timecards_df, notes_df = dfs

def convert_dates(df):
    if not df.empty and "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

def filter_by_date(df, start, end):
    if df.empty or start is None or end is None or "date" not in df.columns:
        return df
    return df[(df["date"] >= pd.to_datetime(start)) & 
              (df["date"] <= pd.to_datetime(end))]

df2 = [entries_df, inspections_df, timecards_df, notes_df]
df2 = [convert_dates(df) for df in df2]
entries_df, inspections_df, timecards_df, notes_df = df2

if not entries_df.empty and "date" in entries_df.columns:
    min_date = entries_df["date"].min().date()
    max_date = entries_df["date"].max().date()
    date_range = st.date_input("Select Date Range", value=(min_date, max_date))

    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = None, None 
else:
    start_date, end_date = None, None

df3 = [entries_df, inspections_df, timecards_df, notes_df]
df3 = [filter_by_date(df, start_date, end_date) for df in df3]
entries_df, inspections_df, timecards_df, notes_df = df3

#------------------------------------------
# Dashboard Visualizations
# ------------------------------------------  
col1, col2 = st.columns(2)

with col1:
    if not entries_df.empty:
        company_group = entries_df.groupby("company")["man_power"].sum().reset_index().sort_values("man_power", ascending=False)
        fig = px.bar(company_group, x="company", 
                    y="man_power", 
                    color="company", 
                    title="Man Power by Company",
                    labels={"man_power": "Man Power", "company": "Company"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available")


with col2:
    if not entries_df.empty:
        hours_group = entries_df.groupby("company")["total_hours"].sum().reset_index().sort_values("total_hours", ascending=False)
        fig = px.bar(hours_group, 
                    x="company", 
                    y="total_hours", 
                    color="company", 
                    title="Total Hours by Company", 
                    labels={"total_hours": "Total Hours", "company": "Company"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available")