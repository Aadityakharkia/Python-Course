# Function with output

def format_name(f_name,l_name):
# Documantation  under ' ' '  Take a first and last name and format it to return the title case version of the name  ' ' ' 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
print(format_name(input("What is your first name ?"),
input("What is your last name ?")))
# format_name()   Check for documentation



