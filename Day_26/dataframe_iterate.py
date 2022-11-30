student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through a data frame

for (key, value) in student_data_frame.items():
    print(key)

for (index, row) in student_data_frame.iterrows():
    print(row)