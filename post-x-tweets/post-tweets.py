# Brainstorm
# (1) Extract information from a website using Selenium, using selenium (e.g. CPI data coming out bi-weekly or monthly)
# *Need to find a way to move Date from top row into first cell of each date break
# (2) Based on information, use an IF condition to determine whether it is of 'good' or 'bad' sentiment
# (3) Post tweet on twitter account using tweepy python package (free tier). Timing of post should be dependent on timing when figures get released, utilise time python package for this.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set global options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class ExtractDataFromHTML:

    def __init__(self, url):
        self.url = url

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
            df = pd.read_html(table_html)

            if df and len(df) == 1:  # Check if any tables were found, and that there is only 1 table
                # df = df[0]  # Assuming the first table is the one you want
                print("Table has been ingested into pd DataFrame successfully")
            else:
                print("No tables found in the HTML content.")
        else:
            print("Table element not found.")

        # Close the browser
        driver.quit()

    def save_to_csv(self):
        df = self.df

        # Extract to csv file
        df.to_csv("/home/christopher/Documents/workspace/py-projects/post-x-tweets/data/cpi.csv")


# ExtractData = ExtractDataFromHTML("https://sslecal2.investing.com/?columns=exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&importance=3&countries=5&calType=week&timeZone=8&lang=1")
# ExtractData.extract_data()
# ExtractData.save_to_csv()