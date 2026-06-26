Project Overview
This project demonstrates an end to end data workflow for a banking transactions dataset. It includes raw data ingestion, exploratory analysis, data cleaning, analytics generation, and an optional automated pipeline using Databricks and AWS S3. The goal is to show how financial data can be processed and transformed into business ready insights using industry standard tools and practices.

Folder Structure
Code
banking-project/
    notebooks/
        01_exploration_cleaning.ipynb
        02_analytics.ipynb

    src/
        pipeline_cleaning.py
        pipeline_analytics.py

    databricks/
        pipeline_notebook.py
        job_config.json

    data/
        raw/
            bank_transactions_raw.csv

        processed/
            bank_transactions_cleaned.csv

        analytics/
            monthly_summary.csv
            category_breakdown.csv
            utilities_trend.csv
            grocery_trend.csv
            income_vs_expense.csv

    README.md
Notebooks
01_exploration_cleaning.ipynb
This notebook performs exploratory data analysis and data cleaning.
Key steps include:

    Loading the raw transactions file
    Inspecting data types and structure
    Fixing date formats
    Converting debit and credit amounts
    Standardizing category names
    Removing duplicates
    Validating running balances
    Saving the cleaned dataset to the processed folder

This notebook represents the exploration and preparation phase of the project.

02_analytics.ipynb
This notebook generates analytics from the cleaned dataset.
Outputs include:

    Monthly spending summary
    Category level spending breakdown
    Utilities spending trend
    Grocery spending trend
    Income versus expense table

Each analytics output is saved as a separate CSV file in the analytics folder.

Source Code
pipeline_cleaning.py
This script contains the production version of the cleaning logic.
It includes functions for:

    Reading raw data
    Cleaning and transforming fields
    Validating data
    Saving cleaned output

This script is designed to be used in automated workflows.

pipeline_analytics.py
This script contains the production version of the analytics logic.
It includes functions for:

    Monthly summaries
    Category totals
    Trend calculations
    Income and expense tables

Outputs are written to the analytics folder or to AWS S3 when used in a pipeline.

Databricks
pipeline_notebook.py
This notebook is used to run the pipeline in Databricks.
It performs the following steps:

    Reads raw data from AWS S3
    Applies the cleaning logic
    Generates analytics
    Writes cleaned data and analytics back to S3

job_config.json
This file stores configuration details for running the Databricks job.
It includes cluster settings, notebook paths, and scheduling information.

Data
raw
Contains the original unmodified dataset.
File: bank_transactions_raw.csv

processed
Contains the cleaned dataset after all transformations.
File: bank_transactions_cleaned.csv

analytics
Contains all analytics outputs generated from the cleaned dataset.
Files include:

    monthly_summary.csv
    category_breakdown.csv
    utilities_trend.csv
    grocery_trend.csv
    income_vs_expense.csv

Summary
This project demonstrates a complete data workflow including exploration, cleaning, analytics, and automation. It uses Python, AWS S3, and Databricks to simulate a realistic financial data pipeline. The structure and approach follow common patterns used in data engineering and data science teams.