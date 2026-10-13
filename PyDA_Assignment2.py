import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df =  sns.load_dataset("taxis")
print(df.head())

print(df.isnull().sum())
num_cols = df.select_dtypes(include="number").columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include=["object","category","str"]).columns
for col in cat_cols:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

df = df.dropna(subset=["pickup","fare","pickup_borough"])
print(df.isnull().sum())

df["pickup"] = pd.to_datetime(df["pickup"])

df = df.sort_values("pickup")

plt.figure(figsize=(12, 6))
plt.plot(df["pickup"], df["fare"])

plt.xlabel("Pickup Timestamp")
plt.ylabel("Fare")
plt.title("Fare Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

borough_fare = df.groupby("pickup_borough")["fare"].sum()

borough_fare.plot(kind="bar", figsize=(10, 6))

plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare")
plt.title("Total Fare by Pickup Borough")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

payment_counts = df["payment"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(payment_counts, labels=payment_counts.index,
        autopct="%1.1f%%", startangle=90)

plt.title("Distribution of Trips by Payment Method")
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["distance"].dropna(), bins=20, edgecolor="black")

plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.title("Distribution of Taxi Trip Distances")
plt.show()

plt.figure(figsize=(10, 6))

df.boxplot(column="tip", by="pickup_borough")

plt.xlabel("Pickup Borough")
plt.ylabel("Tip Amount")
plt.title("Distribution of Tips by Pickup Borough")
plt.suptitle("")

plt.show()

plt.figure(figsize=(10, 6))

sns.countplot(data=df, x="pickup_borough")

plt.xlabel("Pickup Borough")
plt.ylabel("Number of Trips")
plt.title("Number of Trips by Pickup Borough")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough"
)

plt.title("Distance vs Fare by Pickup Borough")
plt.xlabel("Distance")
plt.ylabel("Fare")
plt.tight_layout()
plt.show()

columns = ["distance", "fare", "tip", "tolls", "total"]

corr = df[columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

pair_df = df[
    ["distance", "fare", "tip", "total", "pickup_zone"]
].dropna()

sns.pairplot(
    pair_df,
    hue="pickup_zone",
    diag_kind="hist"
)

plt.show()

plt.figure(figsize=(10, 6))

sns.violinplot(
    data=df,
    x="payment",
    y="fare"
)

plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Fare")
plt.tight_layout()
plt.show()

