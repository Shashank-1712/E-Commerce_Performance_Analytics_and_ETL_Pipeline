# E-Commerce Website Performance — ETL & Analysis

## Overview

This project focuses on building a simple **ETL pipeline for e-commerce data** and preparing the data for further analysis.

The pipeline works with data coming from multiple file formats, including CSV and JSON files. The extracted data is loaded into a MySQL database, making it easier to organize the datasets and use SQL for further analysis.

The main goal of the project is to understand how raw e-commerce data can be moved through a basic data pipeline and converted into a structured format that can be used for analysis.

---

## Project Workflow

```text
CSV / JSON Data
       ↓
   Extraction
       ↓
   Data Loading
       ↓
     MySQL
       ↓
  SQL Analysis
```

The current pipeline extracts the following datasets:

* Orders
* Order Items
* Website Pageviews
* Website Sessions
* Order Item Refunds
* Products

The CSV and JSON files are read using Pandas before being loaded into MySQL tables.

---

## Tech Stack

* **Python**
* **Pandas**
* **SQLAlchemy**
* **MySQL**
* **MySQL Connector**
* **SQL**
* **Bash**
* **Logging**

---

## ETL Pipeline

### 1. Extract

The extraction stage reads the raw CSV and JSON files using Pandas.

CSV files:

```text
orders.csv
order_items.csv
website_pageviews.csv
website_sessions.csv
```

JSON files:

```text
order_item_refunds.json
products.json
```

The file names are converted into table names during the loading process.

### 2. Load

The extracted DataFrames are loaded into a MySQL database using SQLAlchemy.

Each dataset is written to its corresponding database table using Pandas `to_sql()`.

### 3. Logging

The pipeline maintains logs for important stages of execution, including:

* ETL process start
* Data loading
* Loading errors
* ETL completion

This makes it easier to identify problems when the pipeline is executed.

---

## Automation

A Bash script is included to automate execution of the ETL process.

The script:

1. Checks whether `mailutils` is available.
2. Runs the Python ETL script.
3. Stores execution information in a log file.
4. Records whether the process completed or failed.
5. Sends an email alert when the ETL process fails.

---

## Database

The ETL pipeline is designed to load the processed datasets into a MySQL database.

The database connection is handled through SQLAlchemy using the MySQL Connector driver.

---

## Analysis Scope

Once the data is available in MySQL, it can be explored using SQL to answer questions related to:

* Order performance
* Product performance
* Website traffic
* Customer activity
* Refunds
* Conversion behavior
* Session and pageview trends

The project therefore provides a foundation for combining **ETL + SQL + e-commerce analytics** in one workflow.

---

## Project Structure

```text
E-Commerce-Website-Performance-ETL-and-Analysis/
│
├── Dataset/
│   ├── orders.csv
│   ├── order_items.csv
│   ├── website_pageviews.csv
│   ├── website_sessions.csv
│   ├── order_item_refunds.json
│   └── products.json
│
├── ETL Data Pipeline/
│   ├── E-commerce ETL.ipynb
│   └── etl_pipeline.sh
│
└── README.md
```

---

## What I Learned

Through this project, I worked with:

* Reading and combining data from different file formats
* Structuring an ETL workflow in Python
* Working with Pandas DataFrames
* Loading datasets into MySQL
* Connecting Python with databases using SQLAlchemy
* Adding logging to a data pipeline
* Using shell scripting for basic automation
* Preparing an e-commerce dataset for SQL-based analysis

---

## Future Improvements

Some possible extensions to the project are:

* Add data validation checks before loading
* Introduce a separate transformation stage
* Schedule the ETL pipeline
* Add automated data-quality monitoring
* Build a Power BI dashboard on top of the MySQL data
* Add more detailed SQL-based business analysis

---

## Author

**Shashank Dhage**

B.Tech Mechanical Engineering
IIT Bhubaneswar
