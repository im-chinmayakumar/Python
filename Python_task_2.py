#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("E:\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-3.csv")


# In[7]:


df.head()


# Question 1: Distance Matrix Calculation

# In[17]:


def calculate_distance_matrix(df):
    # Create a set of unique toll IDs
    unique_ids = set(df['id_start']).union(df['id_end'])

    # Initialize an empty distance matrix DataFrame
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)

    # Iterate through unique IDs and calculate distances
    for id1 in unique_ids:
        for id2 in unique_ids:
            if id1 == id2:
                distance_matrix.loc[id1, id2] = 0  # Diagonal values set to 0
            else:
                # Find routes between id1 and id2
                forward_distance = df[(df['id_start'] == id1) & (df['id_end'] == id2)]['distance'].sum()
                backward_distance = df[(df['id_start'] == id2) & (df['id_end'] == id1)]['distance'].sum()

                # Calculate total distance (bidirectional)
                total_distance = forward_distance + backward_distance
                distance_matrix.loc[id1, id2] = total_distance
                distance_matrix.loc[id2, id1] = total_distance  # Symmetric matrix

    return distance_matrix

# Example usage:
df = pd.read_csv("E:/Downloads/MapUp-Data-Assessment-F-main/MapUp-Data-Assessment-F-main/datasets/dataset-3.csv")
distance_matrix = calculate_distance_matrix(df)
print(distance_matrix)


# Question 2: Unroll Distance Matrix

# In[23]:


def unroll_distance_matrix(distance_matrix):
    # Create an array of unique IDs from the distance_matrix
    unique_ids = distance_matrix.index.tolist()

    # Initialize an empty DataFrame to store the unrolled data
    unrolled_df = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    # Iterate through unique IDs and create rows for each combination
    for id_start in unique_ids:
        for id_end in unique_ids:
            if id_start != id_end:
                distance = distance_matrix.loc[id_start, id_end]
                unrolled_df = unrolled_df.append({'id_start': id_start, 'id_end': id_end, 'distance': distance}, ignore_index=True)

    return unrolled_df

# Example usage:
# Assuming distance_matrix is the result from calculate_distance_matrix
# result_df = unroll_distance_matrix(distance_matrix)
# print(result_df)


# Question 3: Finding IDs within Percentage Threshold

# In[24]:


import pandas as pd

def find_ids_within_ten_percentage_threshold(df, reference_value):
    # Filter rows with the given reference_value in the 'id_start' column
    reference_rows = df[df['id_start'] == reference_value]

    # Calculate the average distance for the reference value
    reference_average_distance = reference_rows['distance'].mean()

    # Calculate the 10% threshold range
    lower_threshold = reference_average_distance - 0.1 * reference_average_distance
    upper_threshold = reference_average_distance + 0.1 * reference_average_distance

    # Filter rows within the 10% threshold range
    within_threshold_rows = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]

    # Extract unique values from the 'id_start' column and sort them
    result_ids = sorted(within_threshold_rows['id_start'].unique())

    return result_ids

# Example usage:
# Assuming result_df is the DataFrame obtained from unroll_distance_matrix
# reference_value = 1001402  # Replace with the actual reference value
# result_ids = find_ids_within_ten_percentage_threshold(result_df, reference_value)
# print(result_ids)


# Question 4: Calculate Toll Rate

# In[25]:


import pandas as pd

def calculate_toll_rate(df):
    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Multiply distance by rate coefficients for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df

# Example usage:
# Assuming result_df is the DataFrame obtained from unroll_distance_matrix
# result_df_with_rates = calculate_toll_rate(result_df)
# print(result_df_with_rates)


# In[ ]:




