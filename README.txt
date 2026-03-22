# 🏗️ Construct App

## 📌 Overview

Construct App is a web-based construction project tracking tool built with Streamlit. It is designed to help streamline daily field operations by centralizing key project data such as manpower, inspections, timecards, and notes into a single, easy-to-use dashboard.

This application replaces manual tracking methods (e.g., paper logs or scattered spreadsheets) with a structured, data-driven workflow.

---

## 🚀 Features

* 📅 **Daily Logs** – Track manpower and on-site activity
* 🛠️ **Inspections** – Record and monitor inspection data
* ⏱️ **Timecards** – Log and review worker hours
* 📝 **Notes** – Store project-related updates and comments
* 📊 **Dashboard** – Visualize project data using interactive charts
* 🔍 **Filtering** – Filter data by project for better insights

---

## 🧰 Tech Stack

* **Frontend / App Framework:** Streamlit
* **Database:** SQLite
* **Data Processing:** Pandas
* **Visualization:** Plotly

---

## 📷 Screenshots

![Dashboard](images/Dashboard.png)
![main](images/main.png)
![summary](images/Summary.png)

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
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

```bash
streamlit run app.py
```

---

## 🗄️ Database

The application uses a local SQLite database (`construction.db`) to store all project data.

> Note: You may see sample/test data included for demonstration purposes.

---

## 🎯 Purpose

This project was built to:

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
