import pandas as pd
import random
import itertools
course_df = pd.read_csv(r'C:\Users\xzz00\OneDrive\Desktop\Table generation\course_professor.csv')
student_df = pd.read_csv(r'C:\Users\xzz00\OneDrive\Desktop\Table generation\Student.csv')

course_ids = course_df['CourseID'].unique()
student_uins = student_df['UIN'].unique()
cycle_course_ids = itertools.cycle(course_ids)

# Assign courses to students, ensuring more than one student can be assigned to each course
study_data = []
for uin in student_uins:
    course_id = next(cycle_course_ids)  # Get the next course ID from the cycling iterator
    score = random.randint(0, 100)  # Random score between 0 and 100
    study_data.append({'CourseID': course_id, 'UIN': uin, 'Score': score})

# Create the Study DataFrame
study_df = pd.DataFrame(study_data)
study_df.to_csv(r'C:\Users\xzz00\OneDrive\Desktop\Table generation\Study.csv', index=False)