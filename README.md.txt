#Supply Chain Analytics Dashboard

An end-to-end Data Analytics project that analyzes supply chain operations using **Python, MySQL, and Power BI**. The project covers data generation, database design, SQL analysis, and an interactive dashboard for business insights.

---

## Project Overview

This project simulates a real-world supply chain system involving customers, suppliers, products, warehouses, orders, shipments, deliveries, and inventory.

The objective is to monitor supply chain performance, inventory levels, customer orders, supplier performance, and delivery status through an interactive Power BI dashboard.

---

##Tech Stack

- **Python**
  - Pandas
  - Faker
  - NumPy

- **Database**
  - MySQL

- **Visualization**
  - Power BI

- **Version Control**
  - Git & GitHub

---

##Dataset

The project contains the following datasets:

- Customers
- Products
- Suppliers
- Warehouses
- Inventory
- Orders
- Shipments
- Deliveries

---

## Database Design

The MySQL database was designed using relational tables with primary keys and foreign key relationships.

### Main Tables

- customers
- products
- suppliers
- warehouses
- inventory
- orders
- shipments
- deliveries

---

##Dashboard Features

The Power BI dashboard includes:

- Total Orders KPI
- Total Revenue KPI
- Total Customers KPI
- Total Products KPI
- Delayed Deliveries KPI
- Top Selling Products
- Warehouse Inventory Analysis
- Supplier Performance
- Delivery Status Distribution
- Interactive Slicers

---

## Business Insights

The dashboard helps answer questions such as:

- Which products are selling the most?
- Which suppliers receive the highest number of orders?
- How much inventory is available in each warehouse?
- How many deliveries are delayed?
- What are the monthly order trends?
- Which regions generate the most orders?

---
## 📁 Project Structure

```
Supply_Chain_Analytics
│
├── Dataset/
│
├── Python/
│
├── SQL/
│
├── PowerBI/
│   └── Supply_Chain_Analytics.pbix
│
├── Images/
│   └── dashboard.png
│
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Supply_Chain_Analytics.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dataset Generator

```bash
python generate_dataset.py
```

### Import Data

- Create the MySQL database
- Import CSV files into MySQL
- Execute SQL scripts

### Open Power BI

Open:

```
Supply_Chain_Analytics.pbix
```

Refresh the data and explore the dashboard.

---

## Skills Demonstrated

- Data Generation
- Data Cleaning
- Relational Database Design
- SQL Queries
- Data Modeling
- Power BI Dashboard Development
- DAX Measures
- Business Intelligence
- Data Visualization

---

## Future Improvements

- Predict inventory shortages
- Forecast future sales
- Supplier rating analysis
- Delivery performance forecasting
- Interactive drill-through pages

---

## Developed By

**Astha**

GitHub: https://github.com/your-github-username
