import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import add_expense, get_expenses
from ml_model import categorize_expense
from insights import generate_insights

def color_category(val):
    colors = {
        "Food": "#FFE5B4",
        "Travel": "#B4E1FF",
        "Entertainment": "#E0BBE4",
        "Bills": "#FFB4B4",
        "Shopping": "#C1E1C1",
        "Other": "#E0E0E0"
    }
    return f"background-color: {colors.get(val, '#FFFFFF')}"

st.title("💰 AI Personal Expense Tracker")

date = st.date_input("Date")
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0)

if st.button("Add Expense"):
    category = categorize_expense(description)
    add_expense(date, description, amount, category)
    st.success("Expense added successfully!")
data = get_expenses()
df = pd.DataFrame(
    data,
    columns=["ID", "Date", "Description", "Amount", "Category"]
)
st.subheader("📋 Expense History")

if not df.empty:
    st.dataframe(df.style.applymap(color_category, subset=["Category"]))
else:
    st.info("No expenses added yet.")

if not df.empty:
    total_spend = df["Amount"].sum()
    avg_txn = df["Amount"].mean()
    top_category = df.groupby("Category")["Amount"].sum().idxmax()

    k1, k2, k3 = st.columns(3)
    k1.metric("💰 Total Spend", f"₹{total_spend:.0f}")
    k2.metric("📈 Avg Transaction", f"₹{avg_txn:.0f}")
    k3.metric("🏷️ Top Category", top_category)

if not df.empty:
    st.subheader("📊 Spending by Category")

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:
        fig1, ax1 = plt.subplots()
        df.groupby("Category")["Amount"].sum().plot(kind="bar", ax=ax1)
        ax1.set_ylabel("Amount")
        st.pyplot(fig1)

    # Pie Chart
    with col2:
        fig2, ax2 = plt.subplots()
        category_sum = df.groupby("Category")["Amount"].sum()
        ax2.pie(
            category_sum,
            labels=category_sum.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax2.set_title("Category Share")
        st.pyplot(fig2)

if not df.empty:
    st.subheader("📅 Spending Trend")

    df["Date"] = pd.to_datetime(df["Date"])
    daily_spend = df.groupby("Date")["Amount"].sum()

    fig, ax = plt.subplots()
    daily_spend.plot(marker="o", ax=ax)
    ax.set_ylabel("Amount")
    st.pyplot(fig)

st.subheader("🧠 AI Budget Insights")

if not df.empty:
    for insight in generate_insights(df):
        st.write(insight)
