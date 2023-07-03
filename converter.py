import pandas as pd
result = pd.read_csv('testedados1.csv', sep=";")
result.to_parquet('testedados1')
print(result)