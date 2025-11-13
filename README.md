🏥 Healthcare Provider Analysis Dashboard

This repository contains the code, configuration, and documentation for an interactive data analytics dashboard that visualizes and analyzes healthcare provider and patient data.
The system is built to help healthcare professionals understand patient demographics, healthcare spending, and coverage insights using a clean, modern Streamlit interface powered by Pandas and Plotly.

📘 Table of Contents

Overview

Architecture

Dashboard Features

Data Source

Technology Stack

Project Structure

Setup and Deployment

Dashboard Sections

Home (Key Metrics)

Demographics

Financial Insights

Geographic Distribution

Data Explorer

Future Enhancements

Author

🩺 Overview

The Healthcare Provider Analysis Dashboard provides an end-to-end data visualization solution for analyzing healthcare patient data.
It enables analysts and administrators to:

Explore demographic patterns

Compare financial statistics like coverage and expenses

Understand patient distribution by region

Identify healthcare trends and correlations

The dashboard combines cleaned datasets, processed through a data pipeline, and presents the results visually for intuitive exploration.

🧱 Architecture

The system follows a modular data pipeline + visualization approach.

+-----------------+       +---------------------+       +-------------------------+       +--------------------------+
|   Raw Data      | --->  |   Data Cleaning     | --->  |   Processed (Silver)    | --->  |   Streamlit Dashboard    |
| (CSV / Source)  |       | (Nulls, Types Fix)  |       |   Dataset (CSV)         |       |  (Interactive UI)        |
+-----------------+       +---------------------+       +-------------------------+       +--------------------------+


Raw Layer: Original patient dataset (CSV or API data source)

Silver Layer: Cleaned and formatted dataset (PATIENTS_SILVER.csv)

Dashboard Layer: Streamlit application for exploration and analysis

📊 Dashboard Features

Interactive Data Visualization using Streamlit and Plotly

Demographics Analysis by gender, age, race, and marital status

Financial Overview of healthcare expenses and coverage

Geographic Mapping of patients by city/state

Data Exploration Tab for correlation and numeric trend analysis

Clean and Responsive UI for data storytelling

📈 Data Source

Source File: PATIENTS_SILVER.csv

Type: Structured CSV dataset

Content: Patient demographics, healthcare coverage, expenses, and location

Cleaning: Null and missing values handled, data types standardized

🛠 Technology Stack
Category	Tools / Libraries
Programming	Python
Framework	Streamlit
Data Processing	Pandas, NumPy
Visualization	Plotly Express
Version Control	Git, GitHub
Presentation	PowerPoint (.pptx)
📂 Project Structure
Project-HealthCare-Provider-Analysis/
│
├── app/
│   ├── Home.py
│   ├── Demographics.py
│   ├── Financial.py
│   ├── Geographic.py
│   ├── DataExplorer.py
│
├── data/
│   └── PATIENTS_SILVER.csv
│
├── docs/
│   └── Healthcare_Critical_Analysis_Presentation.pptx
│
├── requirements.txt
└── README.md

⚙️ Setup and Deployment

Clone the Repository

git clone https://github.com/saitejamudapalli/Project-HealthCare-Provider-Analysis.git
cd Project-HealthCare-Provider-Analysis


Install Dependencies

pip install -r requirements.txt


Run the Streamlit App

streamlit run Home.py


View in Browser

http://localhost:8501

🏠 Dashboard Sections
🏠 Home (Key Metrics)

Displays overall summary of the healthcare dataset:

Total number of patients

Male vs Female distribution

Average healthcare expenses

Average coverage

👩‍⚕️ Demographics

Visual insights into:

Gender distribution (Pie Chart)

Race and Marital Status breakdowns (Bar Charts)

Age Distribution histogram

💰 Financial Insights

Detailed financial analytics:

Expense distribution

Coverage vs Expenses (Scatter Plot)

Average spending comparison by gender

🌍 Geographic Distribution

Visualizes patient data on an interactive map:

City/state-based distribution

Expense trends across locations

🧮 Data Explorer

A powerful tab for analytical users:

View correlation heatmaps

Explore numerical relationships

Perform deeper statistical analysis

🔮 Future Enhancements

Integration with real-time healthcare APIs

Predictive modeling for patient outcomes

Role-based dashboard access control

Deployment on Streamlit Cloud / AWS / Azure

👤 Author

Saiteja Mudapalli
📧 mudapallisaiteja@gmail.com
🔗 [GitHub Profile](https://github.com/saitejamudapalli)

📸 Dashboard Preview

The above dashboard shows financial insights including expense distribution, coverage comparison, and average costs across genders.
