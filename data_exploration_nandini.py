import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
# 'encoding="latin1"' is used to handle any special characters in the dataset.
# 'parse_dates=["Order Date"]' automatically converts 'Order Date' column to datetime format.
data = pd.read_csv('global-superstore.csv', encoding='latin1', parse_dates=['Order Date'])

# Ensure 'Order Date' is in datetime format
# 'errors="coerce"' will handle any invalid date formats by converting them to NaT (Not a Time).
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')

# Create a new column 'Month' which contains the month and year of each order
# 'dt.to_period('M')' converts the datetime to a Period object representing the month and year.
data['Month'] = data['Order Date'].dt.to_period('M')

# Group the data by 'Month' and calculate the sum of 'Sales'
# '.agg({'Sales': 'sum'})' specifies that we want to sum the 'Sales' column only.
# '.reset_index()' converts the resulting Series back to a DataFrame.
sales_over_time = data.groupby('Month').agg({'Sales': 'sum'}).reset_index()

# Convert the 'Month' period back to a timestamp for plotting
# 'dt.to_timestamp()' converts the Period object to a Timestamp object (a specific point in time).
sales_over_time['Month'] = sales_over_time['Month'].dt.to_timestamp()

# Plotting Sales Over Time
plt.figure(figsize=(12, 6))  # Set the figure size for the plot
sns.lineplot(x='Month', y='Sales', data=sales_over_time)  # Create a line plot of Sales over Time
plt.title('Sales Over Time')  # Set the title of the plot
plt.xlabel('Order Date')  # Label the x-axis
plt.ylabel('Sales')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels to avoid overlap
plt.show()  # Display the plot

# Group the data by 'Category' and calculate the sum of 'Sales'
# '.agg({'Sales': 'sum'})' specifies that we want to sum the 'Sales' column only.
sales_by_category = data.groupby('Category').agg({'Sales': 'sum'}).reset_index()

# Plotting Sales by Category
plt.figure(figsize=(10, 6))  # Set the figure size for the plot
sns.barplot(x='Sales', y='Category', data=sales_by_category)  # Create a bar plot of Sales by Category
plt.title('Sales by Category')  # Set the title of the plot
plt.xlabel('Sales')  # Label the x-axis
plt.ylabel('Category')  # Label the y-axis
plt.show()  # Display the plot
