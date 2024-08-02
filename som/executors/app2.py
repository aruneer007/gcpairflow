import sys
import pandas as pd


if x == 6:
    datasample = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York', 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles', 'Occupation': 'Doctor'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Chicago', 'Occupation': 'Artist'},
    {'Name': 'David', 'Age': 35, 'City': 'Houston', 'Occupation': 'Architect'},
    {'Name': 'Eva', 'Age': 28, 'City': 'Phoenix', 'Occupation': 'Scientist'}
]

df = pd.DataFrame(datasample)

df.to_csv('sample_data.csv')
