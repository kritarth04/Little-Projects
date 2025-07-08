import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_columns', None)

def error_check(col_name, condition_type):
    conditions = ['>', '<', '==', '!=', '>=', '<=']
    if col_name not in df.columns:
        print(f"Column '{col_name}' does not exist.")
        return False
    elif condition_type not in conditions:
        print(f"Condition '{condition_type}' is not valid.")
        return False
    return False

def filtering():
    col_name = input("Enter column name (Make sure its accurate): ")
    condition_type = input("Enter condition (e.g., >, <, ==, etc.): ")
    try:
        value = float(input("Enter a value: "))
    except ValueError:
        print("Please enter a numeric value.")
        return

    try:
        query_str = f"{col_name} {condition_type} {value}"
        filtered_df = df.query(query_str)
        print(f"\n✅ {len(filtered_df)} record(s) matched your filter.")
        print(filtered_df)

        ask_fil_1 = input("Do you want to save this filtered result :").strip().upper()
        if ask_fil_1 == "YES":
            ask_fil_2 = input("Enter a name for the file : ")
            df.to_csv(f"{ask_fil_2}.csv", index=False)
            print("Saved...")
        else:
            print("On to the next")
        return filtered_df
    except Exception as e:
        print(f"❌ Error in filtering: {e}")
    else:
        print("❌ Filtering not applied due to invalid input.")

print("\nWelcome to DATA ANALYZER")
print()

while True:
    ask = input("\nDo you want to analyze a CSV file? (YES/NO): ").strip().upper()

    if ask == 'YES':
        source_file_path = input("Enter your CSV file path: ")

        try:
            data = pd.read_csv(source_file_path)
            df = DataFrame(data)

            print('___________________________________________________________')
            print("Number of rows x columns : ", df.shape, "\n")
            print("Column names :\n", df.columns, "\n")
            print("Data types of the columns :\n", df.dtypes, "\n")
            print("First 5 rows of the dataset :\n", df.head(5), "\n")

            print('___________________________________________________________')
            print("The overall summary of dataset:")
            print(df.describe())

            print('___________________________________________________________')

            while True:
                ask_2 = input("\nDo you want to filter the data? (YES/NO): ").strip().upper()

                if ask_2 == "YES":
                    filtering()
                elif ask_2 == "NO":
                    print("Exiting filtering process.")
                    break
                else:
                    print("Please answer with YES or NO.")

        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
        except Exception as e:
            print("Error loading CSV:", e)

        # Ask if user wants to analyze another CSV
        again = input("\nDo you want to analyze another file? (YES/NO): ").strip().upper()
        if again != 'YES':
            print("Thank you for using CSV Data Analyzer!")
            break

    elif ask == 'NO':
        print("Thank you for visiting!")
        break
    else:
        print("Please answer with YES or NO.")