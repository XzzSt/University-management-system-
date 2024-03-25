import csv
import random
import names
# Function to generate a random phone number as a float
def generate_phone():
    # Generate a 10-digit phone number and convert it to float
    phone_int = random.randint(1000000000, 9999999999)
    return float(f"{phone_int // 1000000000}.{phone_int % 1000000000}")


# Function to generate table data
def generate_students(num_students, filepath):
    students_data = []
    UIN  = 10001  # To ensure UINs are unique

    for i in range(num_students):
        UIN =  UIN + 1
        StuName = names.get_full_name()
        BirthYear = random.randint(1999, 2005)  # Assuming BirthYear between 1999 and 2005
        Gender = random.choice(['Male', 'Female'])
        Phone = generate_phone()
        Major = random.choice([
            'Computer Science', 'Engineering', 'Mathematics', 'History', 'Biology',
            'Physics', 'Chemistry', 'Economics', 'Electrical Eng', 'Statistics',
            'Astronomy', 'Music', 'Art', 'Philosophy', 'Psychology'
        ])

        students_data.append([UIN, StuName, BirthYear, Gender, Phone, Major])

    # Write the data to a CSV file
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UIN', 'StuName', 'BirthYear', 'Gender', 'Phone', 'Major'])
        writer.writerows(students_data)

# Path where the CSV will be saved
file_path = r'C:\Users\xzz00\OneDrive\Desktop\Student.csv'

# Generate data for 100 students and save to a CSV file
generate_students(20000, file_path)
