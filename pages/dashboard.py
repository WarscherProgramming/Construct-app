
import streamlit as st
import pandas as pd
import sqlite3 as sq
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.header("Project Dashboard")

def create_connection():
    return sq.connect("construction.db")

def load_data():
    conn = create_connection()
    entries = pd.read_sql_query("SELECT * FROM entries", conn)
    inspections = pd.read_sql_query("SELECT * FROM inspections", conn)
    timecards = pd.read_sql_query("SELECT * FROM timecards", conn)
    notes = pd.read_sql_query("SELECT * FROM notes", conn)
    conn.close()
    return entries, inspections, timecards, notes

entries_df, inspections_df, timecards_df, notes_df = load_data()

def filter_by_project(df, project):
    if df.empty or not project or "project" not in df.columns:
        return df
    return df[df["project"] == project]

if not entries_df.empty:
    selected_project = st.selectbox("Select Project", entries_df["project"].unique())
else:
    selected_project = None

entries_df = filter_by_project(entries_df, selected_project)
inspections_df = filter_by_project(inspections_df, selected_project)
timecards_df = filter_by_project(timecards_df, selected_project)
notes_df = filter_by_project(notes_df, selected_project)

if not entries_df.empty and "date" in entries_df.columns:
    min_date = entries_df["date"].min()
    max_date = entries_df["date"].max()

    start_date, end_date = st.date_input(
        "Select Date Range",
        [min_date, max_date]
    )
else:
    start_date, end_date = None, None

for df in [entries_df, inspections_df, timecards_df, notes_df]:
    if not df.empty and "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])


def filter_by_date(df, start, end):
    if df.empty or start is None or end is None or "date" not in df.columns:
        return df
    return df[(df["date"] >= pd.to_datetime(start)) & 
              (df["date"] <= pd.to_datetime(end))]

entries_df = filter_by_date(entries_df, start_date, end_date)
inspections_df = filter_by_date(inspections_df, start_date, end_date)
timecards_df = filter_by_date(timecards_df, start_date, end_date)
notes_df = filter_by_date(notes_df, start_date, end_date)

col1, col2 = st.columns(2)

with col1:
    if not entries_df.empty:
        company_group = entries_df.groupby("company")["man_power"].sum().reset_index()
        fig = px.bar(company_group, x="company", y="man_power", title="Man Power by Company", labels={"man_power": "Man Power", "company": "Company"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available")


with col2:
    if not entries_df.empty:
        hours_group = entries_df.groupby("company")["total_hours"].sum().reset_index()
        fig = px.bar(hours_group, x="company", y="total_hours", title="Total Hours by Company", labels={"total_hours": "Total Hours", "company": "Company"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available")