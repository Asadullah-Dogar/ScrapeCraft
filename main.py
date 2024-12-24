from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://steamdb.info/charts/")


name_elements = driver.find_elements(By.CSS_SELECTOR, '.dataTable_table_wrap')

data = []

# Loop through elements to extract the text and split into columns
for name_element in name_elements:
    rows = name_element.text.split("\n")  # Split by new line to process each game
    for row in rows:
        # Split each row into columns
        columns = row.split(" ")
        # Ensure the row has enough data to process
        if len(columns) >= 5:
            name = " ".join(columns[:-4])  # Join name which can have spaces
            current = columns[-4]
            peak_24h = columns[-3]
            all_time_peak = columns[-2]
            data.append([name, current, peak_24h, all_time_peak])

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=["Name", "Current", "24h Peak", "All-Time Peak"])

# Save the DataFrame to a CSV file
df.to_csv("steam_charts.csv", index=False)

# Close the WebDriver
driver.close()

print("Data saved to 'steam_charts.csv'")
