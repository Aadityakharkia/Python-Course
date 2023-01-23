# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.item()}
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}

import random
names = ["Alex","beth","Caroline","Dave","Elanor","Freddie"]

student_score = {name:random.randint(1,100) for name in names}
print(student_score)

passed_students = {name:value for (name,value) in student_score.items() if value >=60}
print(passed_students)

