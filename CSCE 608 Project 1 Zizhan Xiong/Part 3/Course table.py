import pandas as pd
import random
import re
course_df = pd.read_csv(r'C:\Users\xzz00\OneDrive\Desktop\Table generation\course_professor.csv')

course_ids = course_df['CourseID'].unique()
i = 0
values = [1.16, 3.22]
course_data = []
for ids in course_ids:
    course_ids = ids
    Credit = random.randint(2, 4)
    CRN = 10000+i
    Department = re.match(r'\D+', ids).group()
    Start_Date = random.choice(values)
    i = i+1
    course_data.append({'CourseID': course_ids, 'Credit': Credit, 'CRN': CRN, 'Department': Department, 'Start_Date': Start_Date})

course_df = pd.DataFrame(course_data)
course_df.to_csv(r'C:\Users\xzz00\OneDrive\Desktop\Table generation\Course.csv', index=False)