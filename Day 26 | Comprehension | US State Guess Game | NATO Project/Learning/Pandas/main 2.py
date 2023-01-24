# Learning about Pandas

import pandas

student_dict ={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index,row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)