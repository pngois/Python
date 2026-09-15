
/*
==================================================
Superstore Sales Analysis
==================================================
Objective: Explore sales, profit, and customer behavior in the Superstore
dataset to identify business patterns - most profitable categories,
the effect of discounts on margin, sales trends over time, and
customer/region behavior.

Data source: Kaggle - Sample Superstore Dataset
Table: orders (21 columns - see PRAGMA table_info above)
==================================================
*/
PRAGMA table_info(orders);

-- 1. Exploratory Data Analysis

    -- Rows Number, Starting & Ending Order Date
Select count(*), min("Order Date"),max("Order Date") From orders;

    --Missing values in any important column?
Select
  COUNT(*) - COUNT("Order Date") AS missing_order_date,
  COUNT(*) - COUNT("Customer ID") AS missing_customer_id,
  COUNT(*) - COUNT(Sales) AS missing_sales,
  COUNT(*) - COUNT(Profit) AS missing_profit,
  COUNT(*) - COUNT(Discount) AS missing_discount,
  COUNT(*) - COUNT(Region) AS missing_region
From orders;

-- 2. Sales Profile Analysis

    --Total Sales and Total Profit
Select Sum(Sales), Sum(Profit) From orders;

    --Sales & Profit per category and sub-category
Select Category,"Sub-Category",Round(Sum(sales),2) as Total_Sales, Round(sum(profit),2) as Total_Profit
From orders
Group By Category, "Sub-Category"
Order By Category, Total_Sales DESC;

    -- Sales per Region
Select Region, sum(sales) as Total_Sales 
From orders
Group By Region;
    
    --Distribution of Discounts applied
Select Discount, count(*) as Num_orders, 
    Round(Count(*) * 100 / (Select count(*) From orders), 1) AS pct_of_orders
From orders
Group By Discount
Order By discount;
-- 3. Business Questions

    -- Which categories sell the most vs. which are the most profitable?
Select Category, Round(Sum(sales),2) as Total_Sales, Round(sum(profit),2) as Total_Profit,
    round(sum(profit)*100 / sum(sales),1) as profit_margin_pct
From orders
Group By Category
Order By Total_Sales;

    --Is there a relationship between discount and profit?
Select
  Discount,
  COUNT(*) AS num_orders,
  ROUND(AVG(Profit), 2) AS avg_profit,
  ROUND(SUM(Profit) * 100.0 / SUM(Sales), 1) AS profit_margin_pct
From orders
Group By Discount
Order By Discount;

    --Who are the top 10 customers by revenue?

Select 
    "Customer Name", sum(Sales) as total_sales
From orders 
Group By "Customer Name"
Order By total_sales DESC
limit 10;

    --How did sales evolve month by month?
Select
  strftime('%Y-%m', "Order Date") AS order_month,
  SUM(Sales) AS total_sales
From orders
Group By order_month
Order By order_month;

    --Average delivery time by region/ship mode

Select
  Region,
  "Ship Mode",
  ROUND(AVG(julianday("Ship Date") - julianday("Order Date")), 1) AS avg_delivery_days
From orders
Group By Region, "Ship Mode"
Order By Region, avg_delivery_days DESC;


-- 4. Window Functions and Ranking

    --Top 3 best-selling products within each category

Select 
    Category, "Product Name", sum(sales) as total_sales
from orders
Group By Category,"Product Name"
Order By total_sales DESC;




    --Month-over-month sales growth




    --Running total of sales over the year






