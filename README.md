# Device Registry Audit ETL Pipeline

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) and Data Quality pipeline built using Python, Pandas, and Great Expectations.

The pipeline processes:

- Device Registry Data
- Registry Audit Transaction Data

and creates a centralized analytics-ready master table for validation, reporting, and business insights.

---

# Project Workflow

Device Registry JSON + Registry Audit JSON
↓
ETL Processing
↓
Data Cleaning
↓
Validation
↓
Master Table Creation
↓
Great Expectations Validation
↓
Analytics Reporting

---

# Features

- JSON Data Extraction
- Data Cleaning & Transformation
- Missing Value Handling
- Duplicate Validation
- Datatype Conversion
- Master Table Creation
- Great Expectations Data Quality Checks
- Analytics Reporting
- CSV & JSON Export
- Automated Pipeline Execution

---

# Technologies Used

- Python
- Pandas
- Great Expectations
- JSON
- CSV
- Git & GitHub

---

# Folder Structure

```text
device-registry-audit-etl-pipeline/
│
├── data/
│   ├── mongo_source/
│   ├── audit_source/
│   └── processed/
│
├── reports/
│   ├── analytics_report.csv
│   └── validation_report.csv
│
├── logs/
│
├── scripts/
│   ├── etl.py
│   ├── validate.py
│   ├── master_table.py
│   ├── analytics.py
│   ├── great_expectation_check.py
│   └── master.py
│
├── README.md
├── requirements.txt
└── .gitignore