""""
Business Context:
Intuit wants to improve financial insights for clients by analyzing customer transaction behavior. You are tasked with producing a report for the wealth analytics dashboard, which will be used by advisors.

Database Tables:
transactions
|transaction_id|           customer_id| amount             |transaction_type      |transaction_date|
|T001|  |C001| 300|      DEPOSIT|         2023-06-01|
|T002|  C002|  150|      WITHDRAWAL|            2023-06-02|
|T003|  C001|  200|      DEPOSIT|         2023-06-03|
|T004|  C001|  250|      WITHDRAWAL|            2023-06-10|
|T005|  C002|  300|      DEPOSIT|         2023-06-11|


customers
|customer_id |full_name       |region|
|C001| Alice Carter|  West|
|C002| Brian Hughes|               East|
|C003| Deepa Sharma|           Central|
Task Requirements:
Write a SQL query that outputs the following for each customer who has at least 2 transactions:
customer_id
full_name
region
total_transactions
total_amount (sum of all transaction amounts)
average_transaction_amount
latest_transaction_date
first_transaction_amount (this cannot be grouped by directly)

The query must not use GROUP BY to retrieve first_transaction_amount.
Optimize for performance, and avoid common anti-patterns (e.g., correlated subqueries inside SELECT).


select customer_id, full_name, region, count(transaction_id), sum(amount) total_amount 
from transactions t
join customers c
on c.customer_id = t.customer_id
"""






"""



Task Description:
Data Loading: Load both CSV files into spark DataFrames.
Data Transformation:w
Merge the datasets on customer_id.
Calculate each customer's total spend across all orders.
Create a new column indicating the number of days since the customer first ordered from the company.
Aggregation:
Group the data by product_category and calculate the total order amount for each category.
Identify the top 3 customers based on total spend.
Data Export:
Save the transformed and aggregated data into two separate CSV files: customer_spend.csv and category_summary.csv.
customer_spend.csv should contain customer_id, customer_name, total_spend, and days_since_first_order.
category_summary.csv should contain product_category and total_order_amount.


All must be done by using spark
"""



customer.df = spark.read.csv("", header = "True", inferschema = "True")
orders.df = spark.read.csv("orders.csv", header = "True", inferschema = "True")






