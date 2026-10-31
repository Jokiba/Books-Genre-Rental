# importing required library
import pandas as pd

# extracting excel file for data processing
def extract_data(file_name: str)-> pd.DataFrame:
    return pd.read_excel(file_name)

# data filtering with desired book genre
def filter_data(data: pd.DataFrame, genre: str)-> pd.DataFrame:
    data = data[data['rental'] == True]
    return data[data['genre'].str.contains(genre.strip().lower(), case= False, na= False)]

# data sorting with book year published in ascending order
def sort_data(data: pd.DataFrame)-> pd.DataFrame: 
    return data.copy().sort_values(by= 'published')

# create new data column with reverse year published
def new_column(data: pd.DataFrame)-> pd.DataFrame:
    data['contra_published'] = data['published'].astype(str).str[::-1]
    return data

# final result: creating new excel file
def create_new_files(data: pd.DataFrame, new_file_name: str):
    data.to_excel(new_file_name.strip().lower(), index= False)

# function calling with ETL pipeline
extract_data('books.xlsx').pipe(filter_data, genre=input("Input book genre: ")).pipe(sort_data).pipe(new_column).pipe(create_new_files, new_file_name=input("Input new file name with extension(.xlsx): "))
