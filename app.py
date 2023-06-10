import pandas as pd
from flask import Flask, request

app = Flask(__name__)

df = pd.read_csv("data.csv")

# Define the API routes
@app.route("/api/total_items")
def total_items():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    department = request.args.get("department")

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date) & (df["department"] == department)]

    total_items = df["quantity"].sum()

    return total_items

@app.route("/api/nth_most_total_item")
def nth_most_total_item():
    item_by = request.args.get("item_by")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    n = request.args.get("n")

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    df = df.sort_values(by=item_by, ascending=False)

    nth_most_total_item = df.iloc[n-1]["name"]

    return nth_most_total_item

@app.route("/api/percentage_of_department_wise_sold_items")
def percentage_of_department_wise_sold_items():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    percentage_of_department_wise_sold_items = df.groupby("department").size() / len(df) * 100

    return percentage_of_department_wise_sold_items

@app.route("/api/monthly_sales")
def monthly_sales():
    product = request.args.get("product")
    year = request.args.get("year")

    df = df[(df["product"] == product) & (df["year"] == year)]

    monthly_sales = df.groupby("month").size()

    return monthly_sales

if __name__ == "__main__":
    app.run()