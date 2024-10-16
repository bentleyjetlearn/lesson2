myself = {
    "name": "nishtha",
    "age": 85,
    "hobbies": "coding, reading"
}


#get the value
print("My name is" , myself["name"])

#update a value in a dictionary
myself["name"] = "bentley"
print(myself)

#add items
myself["fav_food"] = "pasta"
print(myself)

#remove the values in the dictionary
del myself["age"]
print(myself)

#check for membership
if "hobbies" in myself:
    print("yes ,hobbies are there in the dictionary")
else:
    print("no , hobbies are not there in the dictionary")

#length of the dictionary
print(len(myself))

