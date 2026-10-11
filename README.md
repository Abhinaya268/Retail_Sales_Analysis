# Retail Sales Analysis

## Project Overview
Retail Sales Analysis is a data analytics project that explores retail sales, profit, product performance, customer contribution, regional trends, and discount patterns using Excel, SQL, and PostgreSQL.

The goal is to transform raw sales data into meaningful business insights that support data-driven decisions.

## Dataset
- **Dataset:** Sample Superstore
- **Records:** 9,994
- **Columns:** 21
- **Key fields:** Order Date, Region, Category, Sub-Category, Sales, Quantity, Discount, and Profit

## Tools and Technologies
- **Microsoft Excel:** Data inspection, cleaning, KPI calculations, PivotTables, and charts
- **PostgreSQL:** Data storage, aggregation, filtering, grouping, and business analysis
- **Python:** CSV processing and automated database import
- **Pandas:** Data loading and transformation
- **SQLAlchemy:** PostgreSQL connection and data loading
- **GitHub:** Project version control and portfolio presentation

## Project Workflow
1. Inspected and prepared the Superstore dataset.
2. Checked date, numeric, and percentage fields.
3. Calculated business KPIs and created Excel PivotTables and charts.
4. Created a PostgreSQL table with 21 columns.
5. Imported and verified all 9,994 records using Python.
6. Wrote SQL queries to analyze sales, profit, regions, categories, products, customers, monthly trends, and discounts.

## Business Questions
- Which region generates the highest sales?
- Which product category generates the highest profit?
- Which month has the highest sales?
- Which sub-categories generate the most profit?
- How are discounts associated with sales and profit?
- Which products generate the most revenue?
- Which customers contribute the most profit?
- How do categories perform across different regions?

## Key Findings
- **Top sales region:** West
- **Top-profit category:** Technology
- **Highest-sales month:** November 2017
- **Top-profit sub-category:** Copiers
- **Top-selling product:** Canon imageCLASS 2200 Advanced Copier
- **Top customer by profit:** Tamara Chand

These findings are based on the SQL analysis performed on the dataset.

## Project Structure
```text
Retail_Sales_Analysis/
├── data/
│   └── Sample - Superstore.csv
├── excel/
│   └── Retail_Sales_Cleaned.xlsx
├── sql/
│   ├── import_data.py
│   └── retail_sales_analysis.sql
├── dashboard/
├── documentation/
└── README.md
```

## How to Run
1. Install Python and PostgreSQL.
2. Install the required Python packages:
   `python -m pip install pandas sqlalchemy "psycopg[binary]"`
3. Create the `retail_sales_db` database and the `public.retail_sales` table.
4. Place the CSV dataset in the `data/` folder.
5. Run the import script:
   `python sql/import_data.py`
6. Open `sql/retail_sales_analysis.sql` in a PostgreSQL query tool and execute individual queries.

## Skills Demonstrated
- Data cleaning and validation
- Excel formulas and PivotTables
- SQL aggregation and grouping
- Date-based analysis
- Sales and profit analysis
- Customer and product analysis
- Python automation
- Data interpretation and documentation

## Conclusion
This project demonstrates an end-to-end retail analytics workflow, from preparing raw data to importing it into a relational database and answering practical business questions with SQL.

It showcases foundational skills relevant to entry-level Data Analyst roles.