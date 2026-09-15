# Superstore Sales Analysis

Exploratory data analysis of the Superstore sales dataset, using SQL (SQLite) for analysis and Python for data preparation.

## Objective
Explore sales, profit, and customer behavior to identify business patterns — most profitable categories, the effect of discounts on margin, sales trends over time, and customer/region behavior.

## Data source
[Sample Superstore Dataset from Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) — order-level retail data (9,994 records, 21 columns). Data cleaning (encoding, date formatting) is handled in Python (`Dataset Conversion.py`), then loaded into a SQLite database — all analysis from there on is done in pure SQL.

## Questions answered
- What's the overall sales/profit picture, and how do they break down by category and region?
- Which categories sell the most vs. which are actually the most profitable?
- Is there a relationship between discount level and profit?
- Who are the top customers by revenue?
- How did sales evolve month by month, and what's the month-over-month growth?
- What are the best-selling products within each category?
- What's the running total of sales over the year?

## Key findings
- Furniture generates almost as much revenue as Technology ($742k vs $836k), but its profit margin is only 2.5%, compared to ~17% for Technology and Office Supplies — revenue alone hides how unprofitable a category can be.
- Nearly half of all orders (48%) had no discount applied at all, while 20% discounts accounted for another 36% — together these two levels cover the vast majority of orders.
- Best-selling products by category: Canon imageCLASS 2200 Copier (Technology, $61.6k), Fellowes PB500 Binding Machine (Office Supplies, $27.5k), and HON 5400 Series Task Chairs (Furniture, $21.9k).
- Month-over-month growth peaked at +1132% in March 2014 — though this is partly an artifact of an unusually weak February, not just a strong March. Growth rates should be read alongside absolute sales, not in isolation.

## How to run
```bash
pip install -r requirements.txt
python "Dataset Conversion.py"
```
Then open `Superstore_Analysis.sql` in VS Code (with the SQLite extension) or DB Browser for SQLite to run the queries against `superstore.db`.