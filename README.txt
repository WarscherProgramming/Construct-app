Construction Daily Logging Tool

A Streamlit-based web application for tracking daily construction activity including manpower, inspections, subcontractor notes, and employee timecards.

---

How It Works

1. Data is stored in a SQLite database (`construction.db`)
2. The dashboard loads data using pandas
3. Users can:
   - Select a project
   - Filter by date range
4. Data is dynamically filtered and visualized using Plotly charts


Features

* Interactive dashboard for construction project data
* Project-based filtering across all datasets
* Date range filtering for dynamic analysis
* Visualizations:
  - Manpower by company
  - Total hours by company
* Data stored and retrieved from SQLite database
* Built with Streamlit for fast UI development

---

Tech Stack

* Python
* Streamlit
* SQLite
* Pandas
* Plotly 

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

git clone https://github.com/WarscherProgramming/Construct-app.git
cd Construct-app

2. Install dependencies:

pip install -r requirements.txt

3. Run the app:

streamlit run "Daily Log.py"

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
