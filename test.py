import pandas as pd

df = pd.read_csv("WHO-COVID-19-global-table-data 08-28-21.csv")
print(df['countryName'].head(10))

