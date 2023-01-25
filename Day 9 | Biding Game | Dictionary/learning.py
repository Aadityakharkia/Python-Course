# Dictionaries

# For dictonaries we use { }
# There are two parts of dictonaries key and value
'''
a= {
    "v":"aa"
}
print(a["v"])

# Adding new items to dictonary
a["Loop"] = 


# Grading Problem

student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
student_grades = {}
for i in student_scores:
    score = student_scores[i]
    if score>90:
        student_grades[i]="Outstanding"
    elif score >80:
        student_grades[i]="Exceeds Expectations"
    elif score >70:
        student_grades[i]="Acceptable"
    else:
        student_grades[i]="Fail"

print(student_grades)



# Nesting

capital={
    "France":"Paris",
    "Germany":"Berlin",
}

# Nesting a list in dictionary

travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}

# Nesting a dictionary in a dictionary

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"citiees_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
}

# Nesting a dictionary in a list

travel_log = {
    {"country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits":12},
    
    {"country":"Germany",
    "citiees_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":5}
}


# Codeing Challenge

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
}
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

'''