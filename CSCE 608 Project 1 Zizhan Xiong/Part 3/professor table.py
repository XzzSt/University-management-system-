import names
import random
import pandas as pd
# Since we need to create all UINs between 10000-99999, we will have a total of 90000 entries.
# This is a large number and might not be practical for a single CSV, but for demonstration purposes,
# let's create a smaller subset to show the process.
departments = [
    'CSCE', 'ENG', 'MATH', 'HIST', 'BIO', 'PHYS', 'CHEM',
    'ECON', 'ECE', 'STAT', 'ASTR', 'MUS', 'ART', 'PHIL', 'PSY'
]

num_professors = 10000

# Initialize an empty list to store professor data
professors_data = []
ProfUIN = 0000
# Generate professor data with UINs starting from 10000 onwards
for i in range(num_professors):
    ProfUIN = i
    ProfName = names.get_full_name()  # Generate a more realistic name
    DepartmentName = random.choice(departments)
    Age = random.randint(25, 70)  # Assuming ages range from 25 to 70
    Gender = random.choice(['Male', 'Female']) 
    
    # Append the generated data to the list
    professors_data.append((ProfUIN, ProfName, DepartmentName, Age, Gender))

# Create a DataFrame
professors_df = pd.DataFrame(professors_data, columns=['ProfUIN', 'ProfName', 'DepartmentName', 'Age', 'Gender'])
professors_df.to_csv(r'C:\Users\xzz00\OneDrive\Desktop\professor.csv', index=False)
professors_df.head()