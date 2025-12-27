# insights.py

def generate_insights(df):
    insights = []

    if df.empty:
        return ["No expenses yet. Start adding expenses to get insights."]

    total_spend = df["Amount"].sum()
    insights.append(f"💰 Total spending so far: ₹{total_spend:.2f}")

    # ---------- LEVEL 1: Category dominance ----------
    category_spend = df.groupby("Category")["Amount"].sum()
    top_category = category_spend.idxmax()
    top_amount = category_spend.max()
    top_pct = (top_amount / total_spend) * 100

    insights.append(
        f"📊 Your highest spending category is **{top_category}**, "
        f"which accounts for **{top_pct:.1f}%** of your total expenses."
    )

    if top_category == "Bills" and top_pct > 50:
        insights.append(
            "⚠️ A large portion of your spending is fixed costs (Bills), "
            "which reduces your financial flexibility."
        )

    # ---------- LEVEL 2: Behavioral patterns ----------
    txn_count = df["Category"].value_counts()
    frequent_category = txn_count.idxmax()

    insights.append(
        f"🔁 You spend most frequently on **{frequent_category}** "
        f"({txn_count[frequent_category]} transactions)."
    )

    if frequent_category == "Food":
        insights.append(
            "🍽️ Frequent food transactions suggest impulse or convenience spending."
        )

    # ---------- LEVEL 3: Actionable recommendations ----------
    if "Food" in category_spend and category_spend["Food"] > 0.25 * total_spend:
        insights.append(
            "🥗 Recommendation: Consider setting a weekly food budget to control expenses."
        )

    if "Bills" in category_spend and category_spend["Bills"] > 0.5 * total_spend:
        insights.append(
            "📉 Recommendation: Review fixed bills like rent, internet, or subscriptions "
            "to identify potential savings."
        )

    if "Entertainment" in category_spend and category_spend["Entertainment"] < 500:
        insights.append(
            "🎬 Your entertainment spending is low. "
            "Ensure you allocate some budget for personal enjoyment."
        )

    return insights
