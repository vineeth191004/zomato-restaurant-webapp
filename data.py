import pandas as pd
import sqlite3

def detect_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def load_csv(file_path):
    encoding = detect_encoding(file_path)
    return pd.read_csv(file_path, encoding=encoding)

def load_excel(file_path):
    return pd.read_excel(file_path, engine='openpyxl')

# Load the Zomato restaurant CSV file and the country code Excel file
zomato_df = load_csv('zomato.csv')
country_df = load_excel('Country-Code.xlsx')

# Print column names for both DataFrames to verify the presence of 'Country Code'
print("Zomato DataFrame columns:", zomato_df.columns)
print("Country DataFrame columns:", country_df.columns)

# Merge the two DataFrames on the 'Country Code' column
merged_df = pd.merge(zomato_df, country_df, on='Country Code', how='left')

# Establish a connection to the SQLite database
conn = sqlite3.connect('final_zomato_restaurants.db')
cursor = conn.cursor()

# Create the final table with combined data
cursor.execute('''
CREATE TABLE IF NOT EXISTS final_restaurants (
    Restaurant_ID INTEGER PRIMARY KEY,
    Restaurant_Name TEXT,
    Country_Code INTEGER,
    Country_Name TEXT,
    City TEXT,
    Address TEXT,
    Locality TEXT,
    Locality_Verbose TEXT,
    Longitude REAL,
    Latitude REAL,
    Cuisines TEXT,
    Average_Cost_for_two INTEGER,
    Currency TEXT,
    Has_Table_booking INTEGER,
    Has_Online_delivery INTEGER,
    Is_delivering_now INTEGER,
    Switch_to_order_menu INTEGER,
    Price_range INTEGER,
    Aggregate_rating REAL,
    Rating_color TEXT,
    Rating_text TEXT,
    Votes INTEGER
)
''')

# Insert the merged data into the final table
merged_df.to_sql('final_restaurants', conn, if_exists='replace', index=False)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Final combined database created successfully.")
