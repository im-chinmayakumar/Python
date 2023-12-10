#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[16]:


data =pd.read_csv("E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv")
data
data1 = pd.read_csv("E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-2.csv")


# In[17]:


data.head()
data1.head()


# Question 1: Car Matrix Generation

# In[10]:


def generate_car_matrix(dataset_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset_path)

    # Pivot the DataFrame to create a matrix based on the specified rules
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for col in car_matrix.columns:
        car_matrix.at[col, col] = 0

    return car_matrix


dataset_path = r'E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)


# Question 2: Car Type Count Calculation

# In[11]:


def get_type_count(df):
    # Add a new categorical column 'car_type' based on values of the column 'car'
    conditions = [
        (df['car'] <= 15),
        ((df['car'] > 15) & (df['car'] <= 25)),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices, right=False)

    # Calculate the count of occurrences for each 'car_type' category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_counts = dict(sorted(type_counts.items()))

    return type_counts

# Example usage:
dataset_path = r'E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
data = pd.read_csv(dataset_path)
result_type_counts = get_type_count(data)
print(result_type_counts)


# Question 3: Bus Count Index Retrieval

# In[12]:


def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage:
dataset_path = r'E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
data = pd.read_csv(dataset_path)
result_bus_indexes = get_bus_indexes(data)
print(result_bus_indexes)


# Question 4: Route Filtering

# In[13]:


def filter_routes(df):
    # Group by 'route' and calculate the average of 'truck' column for each route
    average_truck_values = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' values is greater than 7
    selected_routes = average_truck_values[average_truck_values > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

# Example usage:
dataset_path = r'E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
data = pd.read_csv(dataset_path)
result_routes = filter_routes(data)
print(result_routes)


# Question 5: Matrix Value Modification

# In[14]:


def multiply_matrix(input_matrix):
    # Create a copy of the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to each value in the DataFrame
    for col in modified_matrix.columns:
        for row in modified_matrix.index:
            if modified_matrix.at[row, col] > 20:
                modified_matrix.at[row, col] *= 0.75
            else:
                modified_matrix.at[row, col] *= 1.25

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage:
# Assuming result_matrix is the DataFrame obtained from the generate_car_matrix function
result_matrix_modified = multiply_matrix(result_matrix)
print(result_matrix_modified)


# Question 6: Time Check

# In[25]:


def verify_time_completeness(df):
    data1 = pd.read_csv("E:/Downloads/MapUp-Data-Assessment-F-main/MapUp-Data-Assessment-F-main/datasets/dataset-2.csv")

# Call the function to check time completeness
result_series = verify_time_completeness(data1)

# Print the result
print(result_series)


# In[ ]:




