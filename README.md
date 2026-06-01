# Cafe Sales Dashboard

An interactive multi-page Power BI dashboard built on a cafe sales dataset, providing business insights across revenue performance, location & payment analysis, product performance, and food & beverage trends.

![me](https://github.com/jcon242/cafe_sales/blob/main/gifs/pro_2_gif_1.gif)

## About the Dataset

The dataset contains 10,000 transactions recorded across a full calendar year, spanning two locations (**In-store** and **Takeaway**) and three payment methods (**Cash**, **Credit Card**, and **Digital Wallet**).

**Key fields include:** Transaction ID, date, item, item category (food/drink), quantity, price per unit, total spent, location, and payment method.

It's commonly used for practising data cleaning, analysis, visualisation, and business intelligence projects.

## Tools Used

- **Python (Pandas)** – data cleaning and preprocessing (`dirty_cafe_sales.csv` → `clean_cafe_sales`)
- **Power BI Desktop** – dashboard design and visualisation

![Dashboard in Action](pro_2_gif_2.gif)

## Dashboard Pages

| Page | Purpose |
|------|---------|
| **Executive Overview** | High-level KPIs: total transactions, orders, revenue, and average transaction value |
| **Location & Payment Analysis** | Revenue and transaction breakdowns by location (In-store vs Takeaway) and payment method |
| **Product Performance** | Best and worst performing items by revenue and quantity sold |
| **Food & Beverage Analysis** | Food vs drink revenue split, strike rate by quarter, and item order distribution |

![me](https://github.com/jcon242/cafe_sales/blob/main/gifs/pro_2_gif_2.gif)

![me](https://github.com/jcon242/cafe_sales/blob/main/gifs/pro_2_gif_3.gif)

## Getting Started

1. Clone or download this repository
2. Open the [Cafe Sales Dashboard (PDF)](./cafe_sales_dashboard.pdf) to preview all pages

## Notes

- The raw dataset (`dirty_cafe_sales.csv`) was cleaned in Python before being loaded into Power BI
- A significant portion of records contain `N/A` values across location and payment method fields — these are retained and surfaced in the dashboard for transparency
- All data is fictional and intended for practice/portfolio purposes only
