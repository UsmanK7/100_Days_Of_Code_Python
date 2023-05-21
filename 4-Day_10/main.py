
#functions with outputs 
def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name}{formated_l_name}"
print(format_name("usMAN", "KHAN"))

def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name}{formated_l_name}"
print(format_name(input("What is your first name?"),input("What is your last name?")))

#function with multiple return values
def format_name(f_name,l_name):
    if f_name=="" and l_name=="":
        return "The strings are empty yo"
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name("", ""))


#Doc-Strings- It is used to do documentation of our funcitons
def format_name(f_name,l_name):
    """"This functon will take the first and last letter of your name and return it into title case version
    of the name."""
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name}{formated_l_name}"
print(format_name("usMAN", "KHAN"))

