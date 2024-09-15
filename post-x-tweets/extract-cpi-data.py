# (1) Extract information from a website using Selenium, using selenium (e.g. CPI data coming out bi-weekly or monthly)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from io import StringIO

# Set global options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class ExtractDataFromHTML:

    def __init__(self, url):
        self.url = url
        self.df = None  # Initialize df attribute

    def extract_data(self):
        url = self.url
        # Initialize Chrome driver
        driver = webdriver.Chrome()
        driver.get(url)  # Open the target site

        # Wait for the table element to be visible
        table_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ecEventsTable")))

        # Check if the table element is present
        if table_element:
            # Extract the outer HTML of the table
            table_html = table_element.get_attribute("outerHTML")

            # Read the HTML table into a pandas DataFrame
            df = pd.read_html(StringIO(table_html))

            if df and len(df) == 1:  # Check if any tables were found, and that there is only 1 table
                self.df = df[0]  # Store the DataFrame in the instance variable
                print("Table has been ingested into pd DataFrame successfully")
            else:
                print("No tables found in the HTML content.")
        else:
            print("Table element not found.")

        # Close the browser
        driver.quit()

    def save_to_csv(self):
        if self.df is not None:
            # Extract to csv file
            self.df.to_csv("/home/christopher/Documents/workspace/py-projects/post-x-tweets/data/cpi.csv")
        else:
            print("DataFrame is empty. No data to save to CSV.")

# Create an instance of ExtractDataFromHTML
ExtractData = ExtractDataFromHTML("https://sslecal2.investing.com/?columns=exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&importance=3&countries=5&calType=week&timeZone=8&lang=1")
ExtractData.extract_data()
ExtractData.save_to_csv()