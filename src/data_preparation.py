import pandas as pd
pd.set_option('display.max_columns', None)

train = pd.read_csv("../data/raw_data/train.csv")
test = pd.read_csv("../data/raw_data/test.csv")

print("train dataset:", "\n", train.head())
print("test dataset:", "\n", test.head())

# price is the target variable
# price is a numerical and continuous variable

# id: unique identifier, numerical discrete
# carat: 
