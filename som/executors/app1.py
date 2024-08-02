import sys
import pandas as pd
sys.path.append("/home/hadoop/gcpairflow/")
from paths_and_directories import *

if x == 6:
    employees = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York', 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles', 'Occupation': 'Doctor'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Chicago', 'Occupation': 'Artist'},
    {'Name': 'David', 'Age': 35, 'City': 'Houston', 'Occupation': 'Architect'},
    {'Name': 'Eva', 'Age': 28, 'City': 'Phoenix', 'Occupation': 'Scientist'}
]

df = pd.DataFrame(employees)

df.to_csv('employee.csv')
