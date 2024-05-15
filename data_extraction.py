import gspread
import tkinter as tk
from tkinter import messagebox
import random
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
# Define the scope of access (read-only in this case)

def get_data():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Path to the JSON file containing your credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/georgietalukdar/Downloads/Dinner Party/dinner-party-25-05-298bf5be561f.json', scope)

    # Authenticate with Google Sheets
    client = gspread.authorize(credentials)

    # Open the Google Sheet by its name
    sheet = client.open('Dinner Party 25/05/24')

    worksheet = sheet.get_worksheet(0)  # Here, 0 represents the first worksheet

    # Get all values from the worksheet
    data = worksheet.get_all_values()

    # Convert data to pandas DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row contains column headers

    df.to_csv('test.csv')
    return df

