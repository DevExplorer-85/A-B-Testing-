import pandas as pd

df = pd.read_csv("BangaloreZomatoData.csv")

print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("\nColumns:")
print(df.columns.tolist())

print("\nDinner Ratings Sample:")
print(df['Dinner Ratings'].head(10))

print("\nDelivery Ratings Sample:")
print(df['Delivery Ratings'].head(10))

print("\nTop Areas:")
print(df['Area'].value_counts().head(10))

print("\nHome Delivery %")
print(df['IsHomeDelivery'].value_counts(normalize=True)*100)

print(df['Dinner Ratings'].dtype)
print(df['Delivery Ratings'].dtype)

df['Dinner Ratings'] = pd.to_numeric(
    df['Dinner Ratings'],
    errors='coerce'
)

df['Delivery Ratings'] = pd.to_numeric(
    df['Delivery Ratings'],
    errors='coerce'
)

print("\nDinner Rating Stats")
print(df['Dinner Ratings'].describe())

print("\nDelivery Rating Stats")
print(df['Delivery Ratings'].describe())


print(
    df[['Dinner Ratings','Dinner Reviews']]
    .corr()
)


print(
    df[['Delivery Ratings','Delivery Reviews']]
    .corr()
)

area_rating = (
    df.groupby('Area')['Dinner Ratings']
    .mean()
    .sort_values(ascending=False)
)

print(area_rating.head(10))

cost_area = (
    df.groupby('Area')['AverageCost']
    .mean()
    .sort_values(ascending=False)
)

print(cost_area.head(10))


print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nUnique Areas:")
print(df['Area'].nunique())

print("\nSample Areas:")
print(df['Area'].sample(20))

print("\nDinner Ratings Statistics")
print(df['Dinner Ratings'].describe())

print("\nDelivery Ratings Statistics")
print(df['Delivery Ratings'].describe())


top_restaurants = (
    df[['Name','Dinner Ratings','Dinner Reviews']]
    .sort_values('Dinner Ratings', ascending=False)
)

print(top_restaurants.head(15))


df['restaurant_score'] = (
    df['Dinner Ratings'] * 0.7 +
    (df['Dinner Reviews'] / df['Dinner Reviews'].max()) * 5 * 0.3
)


print(
    df[['Name','restaurant_score']]
    .sort_values('restaurant_score', ascending=False)
    .head(15)
)





print("\nAverage Ratings by Features")

print("\nHome Delivery")
print(df.groupby('IsHomeDelivery')['Dinner Ratings'].mean())

print("\nTakeaway")
print(df.groupby('isTakeaway')['Dinner Ratings'].mean())

print("\nIndoor Seating")
print(df.groupby('isIndoorSeating')['Dinner Ratings'].mean())

print("\nVeg Only")
print(df.groupby('isVegOnly')['Dinner Ratings'].mean())






top_cuisines = (
    df['Cuisines']
    .value_counts()
    .head(15)
)

print(top_cuisines)



print(
    df[['AverageCost','Dinner Ratings']]
    .corr()
)



print(
    df[['Dinner Reviews','Dinner Ratings']]
    .corr()
)