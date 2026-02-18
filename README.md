# CrimeAnalysis
Crime analysis whit the help of Python and kaggle-data

# US Crime Data Analysis 📊

A Python-based data analysis project that automates the retrieval, cleaning, and visualization of the classic **US Arrests** dataset.

## 📝 Project Overview
This script demonstrates an end-to-end data pipeline (ETL) on a small scale. It fetches raw crime statistics directly from a remote URL, cleans the data structure, performs a statistical analysis, and generates a visualization of Murder rates across the top 15 US states.

## ✨ Key Features
* **Automated Dependency Management:** The script automatically detects missing libraries (`pandas`, `matplotlib`) and installs them—no manual `pip install` required.
* **Data Fetching:** Direct retrieval of CSV data from a remote repository.
* **Data Cleaning:** Dynamically handles column renaming to ensure data consistency.
* **Visualization:** Generates a Bar Chart visualizing Murder rates per 100,000 inhabitants using `Matplotlib`.
* **Export:** Saves the processed data locally as `brottsstatistik.csv` for further analysis in Excel or SQL.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:**
    * `pandas` (Data manipulation)
    * `matplotlib` (Data visualization)
    * `requests` (Data retrieval)
    * `subprocess` (System operations)

## 🚀 How to Run
1.  Clone this repository.
2.  Run the script directly in your terminal:
    ```bash
    python dataanalysis.py
    ```
3.  The script will:
    * Install necessary packages (if missing).
    * Display the chart.
    * Save the `brottsstatistik.csv` file in the project folder.

## 📊 Results
The analysis identifies the top 15 states with the highest murder rates (based on the 1973 dataset), providing a clear visual comparison for quick insights.

---
*Created as part of my journey into Data Analytics.*
