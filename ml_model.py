# ml_model.py

def categorize_expense(description):
    """
    Rule-based expense categorization using keyword matching
    """

    desc = description.lower().strip()

    CATEGORY_KEYWORDS = {
        "Food": [
            "food", "restaurant", "hotel", "coffee", "tea",
            "snack", "lunch", "dinner", "breakfast"
        ],
        "Travel": [
            "auto", "cab", "uber", "ola", "bus",
            "train", "metro", "travel", "taxi", "fuel", "petrol"
        ],
        "Entertainment": [
            "movie", "cinema", "netflix", "spotify",
            "game", "concert"
        ],
        "Bills": [
            "rent", "electricity", "water", "gas",
            "internet", "wifi", "mobile", "recharge"
        ],
        "Shopping": [
            "amazon", "flipkart", "mall",
            "clothes", "dress", "shoes"
        ]
    }

    for category, keywords in CATEGORY_KEYWORDS.items():
        for word in keywords:
            if word in desc:
                return category

    return "Other"
