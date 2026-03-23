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

## 🧰 Tech Stack

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

git clone https://github.com/WarscherProgramming/Construct-app.git
cd Construct-app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

streamlit run app.py

---

Database

This app uses SQLite for lightweight, file-based data storage.

Tables:

* Practice full-stack Python development
* Create a real-world tool for construction workflow management
* Explore data visualization and dashboard design

---

## 🔮 Future Improvements

* User authentication and role-based access
* Cloud deployment (AWS, Azure, or Streamlit Cloud)
* Mobile-friendly UI enhancements
* Export reports (PDF/Excel)
* Improved data validation and error handling

---

## 👤 Author

**Zachary Warscher**
GitHub: https://github.com/WarscherProgramming
