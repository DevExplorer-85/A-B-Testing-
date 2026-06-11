import pandas as pd
import numpy as np

np.random.seed(42)

n_customers = 5000

customers = pd.DataFrame({
    "customer_id": range(n_customers),

    "orders": np.random.poisson(8, n_customers),

    "avg_order_value": np.random.normal(
        450,
        100,
        n_customers
    ),

    "days_since_last_order": np.random.randint(
        1,
        180,
        n_customers
    )
})

customers["total_revenue"] = (
    customers["orders"] *
    customers["avg_order_value"]
)


customers["future_revenue"] = (
    customers["total_revenue"] * 0.4
    + np.random.normal(
        0,
        300,
        n_customers
    )
)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = customers[
    [
        "orders",
        "avg_order_value",
        "days_since_last_order"
    ]
]

y = customers["future_revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    "R² Score:",
    r2_score(y_test, predictions)
)
customers["predicted_ltv"] = model.predict(X)

customers["segment"] = pd.qcut(
    customers["predicted_ltv"],
    q=3,
    labels=["Low Value", "Medium Value", "High Value"]
)

print(customers["segment"].value_counts())

print(
    customers.groupby("segment")["predicted_ltv"]
    .mean()
)


top_customers = (
    customers[
        ["customer_id",
         "predicted_ltv",
         "orders",
         "avg_order_value"]
    ]
    .sort_values(
        "predicted_ltv",
        ascending=False
    )
)

print(top_customers.head(10))

