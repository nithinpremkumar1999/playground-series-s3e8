import pandas as pd
pd.set_option('display.max_columns', None)

train = pd.read_csv("../data/raw_data/train.csv")
test = pd.read_csv("../data/raw_data/test.csv")

print("--------------------------")
print("train dataset:", "\n", train.head())
print("--------------------------")
print("test dataset:", "\n", test.head())

# target variable is:
# price: numerical continuous

# independent variables are:
# id: unique identifier, numerical discrete,
# carat: numerical continuous,
# cut: categorical ordinal,
# color: categorical nominal,
# clarity: categorical ordinal,
# depth: numerical continuous,
# table: numerical continuous,
# x: numerical continuous,
# y: numerical continuous,
# z: numerical continuous

print("--------------------------")
print("{} observations and {} features in train set.".format(*train.shape))
print("{} observations and {} features in test set.".format(*test.shape))


print("--------------------------")
print("inspect price column", "\n")
print(train.price.describe())
print("numbers of NA values:", train.price.isnull().sum())


print("--------------------------")
print("inspect id column", "\n")
print(train.id.describe())
print("numbers of NA values:", train.id.isnull().sum())
# index is redundant as the column does not add any info and same as index of dataframe
train.drop("id", axis=1, inplace=True)

print("--------------------------")
print("inspect carat column", "\n")
print("train dataset:")
print(train.carat.describe())
print("numbers of NA values:", train.carat.isnull().sum(), "\n")
print("test dataset:")
print(test.carat.describe())
print("numbers of NA values:", test.carat.isnull().sum())

print("--------------------------")
print("inspect cut column", "\n")
print("train dataset:")
print(train.cut.unique())
print("numbers of NA values:", train.cut.isnull().sum(), "\n")
print("test dataset:")
print(test.cut.unique())
print("numbers of NA values:", test.cut.isnull().sum())

print("--------------------------")
print("inspect color column", "\n")
print("train dataset:")
print(train.color.unique())
print("numbers of NA values:", train.color.isnull().sum(), "\n")
print("test dataset:")
print(test.color.unique())
print("numbers of NA values:", test.color.isnull().sum())

print("--------------------------")
print("inspect clarity column", "\n")
print("train dataset:")
print(train.clarity.unique())
print("numbers of NA values:", train.clarity.isnull().sum(), "\n")
print("test dataset:")
print(test.clarity.unique())
print("numbers of NA values:", test.clarity.isnull().sum())

print("--------------------------")
print("inspect depth column", "\n")
print('train dataset:')
print(train.depth.describe())
print("numbers of NA values:", train.depth.isnull().sum(), "\n")
print('test dataset:')
print(test.depth.describe())
print("numbers of NA values:", test.depth.isnull().sum())

print("--------------------------")
print("inspect table column", "\n")
print('train dataset:')
print(train.table.describe())
print("numbers of NA values:", train.table.isnull().sum(), "\n")
print('test dataset:')
print(test.table.describe())
print("numbers of NA values:", test.table.isnull().sum())

print("--------------------------")
print("inspect x column", "\n")
print('train dataset:')
print(train.x.describe())
print("numbers of NA values:", train.x.isnull().sum(), "\n")
print('test dataset:')
print(test.x.describe())
print("numbers of NA values:", test.x.isnull().sum())

print("--------------------------")
print("inspect y column", "\n")
print('train dataset:')
print(train.y.describe())
print("numbers of NA values:", train.y.isnull().sum(), "\n")
print('test dataset:')
print(test.y.describe())
print("numbers of NA values:", test.y.isnull().sum())

print("--------------------------")
print("inspect z column", "\n")
print('train dataset:')
print(train.z.describe())
print("numbers of NA values:", train.z.isnull().sum(), "\n")
print('test dataset:')
print(test.z.describe())
print("numbers of NA values:", test.z.isnull().sum())

print("--------------------------")
print("Check for duplicates:", "\n")
print("train dataset:")
print(train[train.duplicated()], "\n")
print("test dataset:")
print(test[test.duplicated()])

#train.to_csv("../data/clean_data/train.csv", index=False)
#test.to_csv("../data/clean_data/test.csv", index=False)