Construction Daily Logging Tool

A Streamlit-based web application for tracking daily construction activity including manpower, inspections, subcontractor notes, and employee timecards.

---

Features

* Track daily manpower and work descriptions
* Log inspections with results and notes
* Record subcontractor delays/issues
* Manage employee timecards
* Persistent storage using SQLite database

---

Tech Stack

* Python
* Streamlit
* SQLite
* Pandas

---

Project Structure

construction-tool/
├── app.py
├── database.py
├── requirements.txt
├── README.md

---

Installation

1. Clone the repository:

git clone https://github.com/WarscherProgramming/Construction-tool.git
cd Construction-tool

2. Install dependencies:

pip install -r requirements.txt

3. Run the app:

streamlit run app.py

---

Database

This app uses SQLite for lightweight, file-based data storage.

Tables:

* entries
* notes
* inspections
* timecards

---

Future Improvements

* Replace session state with direct database writes
* Add filtering (date, project, company)
* Add edit/delete functionality
* Deploy to Streamlit Cloud

---

Author

Zachary Warscher
