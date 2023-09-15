import os
import pandas as pd
import numpy as np

# Get the current working directory (where the code file is located)
current_directory = os.getcwd()

# Define the naming pattern for the CSV files:
file_pattern = 'b_{}.csv'  # {} will be replaced with the file numbers (e.g., b_1.csv, b_2.csv)

# Determine the range of file numbers or a list of specific file numbers you want to load:
start_file_number = 1
end_file_number = 426  # Adjust this according to your dataset size
# Alternatively, you can create a list of specific file numbers: file_numbers = [1, 3, 5, 7]

# Initialize an empty list to store the matrices
matrix_list = pd.DataFrame({})

# Loop through the file numbers and load each CSV file
for i in range(start_file_number, end_file_number + 1):
    file_name = file_pattern.format(i)
    file_path = os.path.join(current_directory, file_name)  # Construct the full file path
    
    # Load the CSV file into a DataFrame and exclude the first column
    df = pd.read_csv(file_path,sep=";", header=None)  # Adjust header option if needed
    matrix = df[df.columns[1:]]  # Exclude the first column
    matrix['ID'] = 'b_'+str(i)
    matrix_list = pd.concat([matrix_list, matrix], axis = 0)

# print(matrix_list)

# Now, matrix_list contains all the matrices (excluding the first column) loaded from your CSV files in the same directory as your code file
# Assuming you've already loaded the dataset into `matrix_list`

# Convert the list of matrices into a single NumPy array
data = np.array(matrix_list)

# Create a Pandas DataFrame for easier data manipulation
df = pd.DataFrame(data)

# Display basic statistics of your dataset
print(df.describe())

# Check the first few rows of the DataFrame
print(df.head())