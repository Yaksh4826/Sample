import pandas as pd

fish = pd.read_csv("C:\\Users\\yaksh\\Downloads\\Fish.csv")
print(fish);
# Printing the number of rows and columns:

print(fish.dtypes)


print(fish.isnull().sum());

print(fish["Length1","Length2","Length3"].mean());

      