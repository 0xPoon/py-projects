# (2) Conduct Transformation on data: make it so data is in a proper tabular format
# Run 'extract_cpi_data.py', obtain df
# Ingest df into TransformData()
import pandas as pd
from extract_int_rate_data import ExtractDataFromHTML
from datetime import datetime

# Set global options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width',-1)

class TransformData:
    def __init__(self, df):
        self.df = df

    def remove_null_rows(self):
        df = self.df

        # Identify rows with a null value in the first cell
        rows_to_drop = df[df.iloc[:, 0].isnull()].index

        # Drop the identified rows
        df = df.drop(rows_to_drop)

        # df.to_csv('/home/christopher/Documents/workspace/py-projects/post-x-tweets/data/cpi_amended.csv')
        return df

        # # for i in range(0, len(df.index)):
        # #     first_cell_data = df.iloc[i][0]
        # #     if first_cell_data == 'nan':
        # #         print(i, first_cell_data)

    def transform_date_format(self):
        df = self.remove_null_rows()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        for i in range(0, len(df.index)):
            first_cell_data = df.iloc[i, 0]

            # Check if any of the weekday components of 'weekdays' list is present in first_cell_data
            if any(weekday in str(first_cell_data) for weekday in weekdays):
                input_date_format = "%A, %B %d, %Y"     # Tuesday, September 17, 2024
                output_date_format = "%d/%m/%Y"         # 17/09/2024

                # Parse the first_cell_data into a datetime object
                parsed_date = datetime.strptime(first_cell_data, input_date_format)

                # Format the date to "dd/mm/YYYY"
                first_cell_data = parsed_date.strftime(output_date_format)

                # Update the DataFrame with the transformed date
                df.iloc[i, 0] = first_cell_data

        # df.to_csv('/home/christopher/Documents/workspace/py-projects/post-x-tweets/data/cpi_amended_date.csv')
        return df

    def fill_down_date(self):
        df = self.transform_date_format()

        prev_date = None
        for i in range(0, len(df.index)):
            if ':' in df.iloc[i, 0]:
                df.iloc[i, 0] = prev_date
            else:
                prev_date = df.iloc[i, 0]
            # print(df.iloc[i, 0])

        df = df.rename(columns={"Time": "Date"})    # rename 'Time' to 'Date'
        df = df.drop(columns=["Unnamed: 5"])
        # df.to_csv('/home/christopher/Documents/workspace/py-projects/post-x-tweets/data/cpi_amended_filled_down_date.csv')
        return df

    def extract_filtered_df(self):
        df = self.fill_down_date()

        int_rate_df = df[df['Event'].str.contains("Fed Interest Rate Decision")]
        print(int_rate_df.head())
        return int_rate_df


# Call ExtractDataFromHTML from 'extract_cpi_data.py'
Extracted_DF = ExtractDataFromHTML("https://sslecal2.investing.com/?columns=exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&importance=3&countries=5&calType=week&timeZone=8&lang=1")
Extracted_DF.extract_data()
data = Extracted_DF.save_to_csv()       # Save original df to 'data'

# Create instance of TransformData
Transform_Data = TransformData(data)
Transform_Data.remove_null_rows()
Transform_Data.transform_date_format()
Transform_Data.fill_down_date()
Transform_Data.extract_filtered_df()