import pandas as pd

print("pandas version={}".format(pd.__version__))

# pd.options.display.max_rows by default is 60
# pd.options.display.max_rows = 20000

print("pd.options.display.max_rows={}".format(pd.options.display.max_rows))

class MyPandas(object):
    def __init__(self):
        pass

    def run(self):
        print("DataFrame\n")

        arr = pd.DataFrame({
            'cars': ["BMW", "Volvo", "Ford"],
            'passings': [3, 7, 2]
        })

        print(type(arr))
        print(arr)

        print("\n")

        print("Read CSV File\n")

        df = pd.read_csv('data.csv')

        print("head(n)")

        print(df.head(10))

        print("\ntail(n)")

        print(df.tail(5))

        cleaned_data = df.dropna()

        print("\ndropna()")

        print(cleaned_data.tail(10))

        print("\nduplicated()")

        non_duplicated_data = df.duplicated()

        print(non_duplicated_data.head(30))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_pandas = MyPandas()
    my_pandas.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
