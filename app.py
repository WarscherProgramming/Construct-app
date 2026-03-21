
# --------------------------------------------------
# Construction Daily Logging Tool
# 
# Purpose:
# Streamlit app for tracking daily construction data:
# - Manpower
# - Inspections
# - Subcontractor notes
# - Timecards
#
# Data is stored in a SQLite database (construction.db)
#
# Future Improvements:
# - Replace session state with direct DB writes
# - Add filtering (date, project, company)
# - Add edit/delete functionality
# --------------------------------------------------

import pandas as pd
import streamlit as st
import time
import os
import sqlite3 as sq 

# -----------------------------
# DATABASE SETUP & FUNCTIONS
# -----------------------------
def init_db():
    conn = sq.connect("construction.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        project TEXT,
        company TEXT,
        man_power INTEGER,
        description TEXT,
        hours_worked INTEGER,
        total_hours INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        project TEXT,
        company TEXT,
        notes TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inspections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        project TEXT,
        inspection TEXT,
        inspection_notes TEXT,
        result TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timecards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        project TEXT,
        employee TEXT,
        hours_worked INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_entry(entry):
    conn = sq.connect ("construction.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO entries (date, project, company, man_power, description, hours_worked, total_hours)
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (
        str(entry["date"]),
        entry["project"],
        entry["company"],
        entry["man_power"],
        entry["description"],
        entry["hours_worked"],
        entry["total_hours"]
    ))
    conn.commit()
    conn.close()

def insert_notes(notes):
    conn = sq.connect ("construction.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO notes (date, project, company, notes)
    VALUES (?, ?, ?, ?)""", (
        str(notes["date"]),
        notes["project"],
        notes["company"],
        notes["notes"]
    ))
    conn.commit()
    conn.close()

def insert_inspection(inspection):
    conn = sq.connect ("construction.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO inspections (date, project, inspection, inspection_notes, result)
    VALUES (?, ?, ?, ?, ?)""", (
        str(inspection["date"]),
        inspection["project"],
        inspection["inspection"],
        inspection["inspection_notes"],
        inspection["result"]
    ))
    conn.commit()
    conn.close()

def insert_timecard(timecard):
    conn = sq.connect ("construction.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO timecards (date, project, employee, hours_worked)
    VALUES (?, ?, ?, ?)""", (
        str(timecard["date"]),
        timecard["project"],
        timecard["employee"],
        timecard["hours_worked"]
    ))
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# STREAMLIT APP CONFIG
# -----------------------------
st.set_page_config(page_title="Construction Tool", layout="wide")

st.header("Construction Tool")

#------------------------------
# HELPER FUNCTIONS
#------------------------------
st.markdown("""
<style>
.divider {
    border-left: 2px solid #ddd;
    height: 100%;
    margin: 0 10px;
}
</style>
""", unsafe_allow_html=True)

def company_selector(label="Company", options=None):
    if options is None:
        options =["Design Drywall (Framers and Hangers)", 
                  "Design Drywall (Tapers)", 
                  "Design Drywall (Painters)",
                  "Arizona Insulation",
                  "Arrowhead Doors",
                  "Blade Runners",
                  "Cookson Doors",
                  "Custom Steel Works",
                  "DGO Plumbing",
                  "Fazzari Flooring",
                  "ME Maricopa Electric",
                  "Mirage Glass and Mirror",
                  "RCI Systems",
                  "RSA Air Conditioning",
                  "Sherwood Welding",
                  "Southwest Acoustics",
                  "Starkweather Roofing",
                  "W&W Structural Steel",
                ]
    return st.selectbox(label, options)

def show_success_message(message):
    placeholder = st.empty()
    placeholder.success(message)
    time.sleep(2)
    placeholder.empty()

#-----------------------------
#PROJECT AND DATE INPUT
#-----------------------------
st.subheader("Project")

project = st.selectbox("Select Project", ["Apex Garages", "Apex Clubhouse"])

date = st.date_input("Date")

#--------------------------------
#SESSION STATES FOR USER INPUT'S
#--------------------------------
if "entries" not in st.session_state:
    st.session_state.entries = []

if "notes" not in st.session_state:
    st.session_state.notes = []

if "inspections" not in st.session_state:
    st.session_state.inspections = []

if "timecards" not in st.session_state:
    st.session_state.timecards = []

# -----------------------------
# USER INPUT SECTIONS
# -----------------------------

col1, div1, col2, div2, col3 = st.columns([1, 0.05, 1, 0.05, 1])
with col1:
    st.subheader("Daily Man Power")
    

    company = company_selector()

    log_col1, log_col2 = st.columns(2)
    with log_col1:
        man_power = st.selectbox("Man Power", range(1, 100))

    with log_col2:
        hours = st.selectbox("Hours Worked", range(1, 13))

    description = st.text_input("Description: ")

    total_hours = man_power * hours

    if st.button("Add Entry", key="add_entry"):

        if not description.strip():
            st.warning("Please enter a description before adding the entry.")
            st.stop()

        entry = {
            "date": date,
            "project": project,
            "company": company,
            "man_power": man_power,
            "description": description,
            "hours_worked": hours,
            "total_hours": total_hours,
        }
    
        st.session_state.entries.append(entry)
        show_success_message("Entry added successfully!")

with div1:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
 
with col2:
    st.subheader("Inspections")

    inspection = st.text_input("Inspection Details: ")
 
    inspection_notes = st.text_input("Inspection Notes: ")

    result = st.selectbox("Result", ["Pass", "Partially Pass", "Fail"])

    if st.button("Add Inspection", key="add_inspection"):

        if not inspection.strip():
            st.warning("Please enter inspection details before adding the entry.")
            st.stop()

        if not inspection_notes.strip():
            st.warning("Please enter inspection notes before adding the entry.")
            st.stop()

        inspection_entry = {
            "date": date,
            "project": project,
            "inspection": inspection,
            "inspection_notes": inspection_notes,
            "result": result,
            }

        st.session_state.inspections.append(inspection_entry)
        show_success_message("Inspection entry added successfully!")

with div2:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with col3:

    st.subheader("Daily Notes")

    sub_contractor = company_selector(label='Sub Contractor')

    note = st.text_input("Subcontractor Delays/Issues: ")

    severity_level = st.selectbox("Severity", ["Low", "Medium", "High"])

    if st.button("Add Notes", key="add_notes"):

        if not note.strip():
            st.warning("Please enter a note before adding the entry.")
            st.stop()

        notes_entry = {
            "date": date,
            "project": project,
            "company": sub_contractor,
            "notes": note
            }
    
        st.session_state.notes.append(notes_entry)
        show_success_message("Notes entry added successfully!")

st.subheader("Timecard")
col1, col2 = st.columns(2)
with col1:
    timecard = st.selectbox("Employee Name", ["Zachary Warscher", "O. Jose Castaneda Morales", "Ronald Sanchez"])
with col2:
    hours_worked = st.selectbox("Hours", range(1, 13))

if st.button("Add Timecard", key="add_timecard"):
    timecard_entry = {
        "date": date,
        "project": project,
        "employee": timecard,
        "hours_worked": hours_worked
        }
    
    st.session_state.timecards.append(timecard_entry)
    show_success_message("Timecard entry added successfully!")

# -----------------------------
# DAILY SUMMARY
# -----------------------------
st.subheader("Daily Summary")

df = pd.DataFrame(st.session_state.entries)
df2 = pd.DataFrame(st.session_state.notes)
df3 = pd.DataFrame(st.session_state.inspections)
df4 = pd.DataFrame(st.session_state.timecards)

st.dataframe(df, width="content")
st.dataframe(df2, width="content")
st.dataframe(df3, width="content")
st.dataframe(df4, width="content")


if st.button("Save to Database", key="save_database"):
    for entry in st.session_state.entries:
        insert_entry(entry)
    for note in st.session_state.notes:
        insert_notes(note)
    for inspection in st.session_state.inspections:
        insert_inspection(inspection)
    for timecard in st.session_state.timecards:
        insert_timecard(timecard)

    show_success_message("Data saved to database successfully!")
    st.session_state.entries.clear()
    st.session_state.notes.clear()
    st.session_state.inspections.clear()
    st.session_state.timecards.clear()
    st.rerun()