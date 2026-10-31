# Customer Orders ETL Pipeline Using Python and Pandas

## Project Overview
This project implements a simple ETL (Extract, Transform, Load) pipeline using Python and Pandas.

It processes customer, order, and product CSV files to generate a final order report.

## Technologies Used
- Python
- Pandas
- CSV Files
- Git
- GitHub

## Project Structure
```text
Python_and_Pandas/
├── customers.csv
├── orders.csv
├── products.csv
├── main.py
├── final_orders.csv
└── README.md
```

## ETL Process

### 1. Extract
- Read customer, order, and product CSV files using Pandas.

### 2. Transform
- Remove duplicate customer records.
- Identify invalid customer IDs.
- Join customer and order datasets.
- Join product information.
- Calculate total amount using quantity × price.

### 3. Load
- Generate the final output file: `final_orders.csv`.

## Project Output
The final dataset contains:
- Order ID
- Customer Name
- City
- Product Name
- Quantity
- Price
- Status
- Total Amount

## How to Run

Install Pandas:

```bash
pip install pandas
```

Execute:

```bash
python main.py
```

## Learning Outcomes
- CSV file processing
- Data cleaning
- Data validation
- Pandas DataFrame operations
- Data merging and transformation
- ETL pipeline development