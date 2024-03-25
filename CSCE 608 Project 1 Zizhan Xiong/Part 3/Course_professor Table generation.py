import random
import csv


# Function to generate a random course ID
def random_course_id(existing_ids):
    while True:
        dept = random.choice(['CSCE', 'ENG', 'MATH', 'HIST', 'BIO', 'PHYS', 'CHEM', 'ECON', 'ECE', 'STAT','ASTR', 'MUS', 'ART', 'PHIL', 'PSY'])
        number = random.randint(100, 699)
        course_id = f"{dept}{number}"
        if course_id not in existing_ids:
            existing_ids.add(course_id)
            return course_id

# Function to generate table data
def generate_table(num_rows, existing_ids):
    table_data = []
    for _ in range(num_rows):
        row = {
            'CourseID': random_course_id(existing_ids),
            'Credit': random.randint(2, 4),  # Assuming credits are between 2 and 4
            'ProfUIN': random.randint(0000, 9999)  # Assuming UINs are between 10000 and 99999
        }
        table_data.append(row)
    return table_data

# Usage
existing_ids = set()


# Change the path below to match the path to your desktop
desktop_path = r'C:\Users\xzz00\OneDrive\Desktop\course_professor.csv'

with open(desktop_path, 'w', newline='') as csvfile:
    fieldnames = ['CourseID', 'Credit', 'ProfUIN']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in generate_table(2000, existing_ids):  # Assuming you have a function to generate your table data
        writer.writerow(row)

print(f"CSV file saved to: {desktop_path}")
