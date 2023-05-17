Programming_Dictionary = {
    "Bug": "An error in a program  that prevents the program from running as expected",
    "Function": "A piece  of code that you can easy call over and over again ",
    "Loop":"The action of doing something over and over again",
}
#Retreiving items from dictionary
# print(Programming_Dictionary["Bug"])

#Adding new items to dictionary
Programming_Dictionary["Loop"]="The action of doing something over and over again"

# print(Programming_Dictionary)

#Create an empty dictionary
empty_dictionary=[]

#Wipe an existing dictionary
# Programming_Dictionary={}
# print(Programming_Dictionary)

#Edit an item in the dictionary---If it find nothing in the dictionary that you writen inside [] then it create new
Programming_Dictionary["Bug"]="A moth in your dictionary"
# print(Programming_Dictionary)

#Nesting
Capitals={
    "Pakistan","Islamabad"
    "America","Washington DC"
}

#Nesting in dictionary in lists
Travel_log={
    "Pakistan",["karachi","mianwali","lahore"],
     "America",["mexico","washington","new york"]
}

#Dictionaries inside Dictiories
travel_log={
    "France",{"cities visited":["paris","Lille","Dijon"],"total_visits": 12},
    "Germany",{"cities visited":["Berlin","Hamburg","Stuttgart"],"total_visits":3}
}
#Nesting Dictionaries inside List
travel_log=[
    {
        "Country":"france",
        "cities visited":["paris","Lille","Dijon"],
        "total_visits": 12
    }
]
