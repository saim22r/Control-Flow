# Syntax if variable - condition age:

# weather = "rainy"
#
# if weather == "Sunny": # if this condition is true the next line would execute
#     print("Enjoy the weather")
# if weather != "Sunny":
#     print("The weather is not rainy, Enjoy for now")
#
# # Lets use our ticket age criteria
# age = 18
# if age < 19:
#     print("You are not allowed into this movie")

# For loops and While loops
# Loops help us iterate through our data such as lists, dicts and sets

# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# print(shopping_list[1])

# Iterate through a list with a for loop
# First iteration
# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# for items in shopping_list:
#     print(items)

# # Second iteration
# shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
# for items in shopping_list:
#     if items == "bread":
#         break
#     print(items)

# Third iteration with dict
# student_data ={
#     "student_name": "Saim",
#     "course":"DevOps",
#     "course_topics" : 4,
#     "topic_names":["Business week", "Python", "Virtualisation with vagrant", "AWS cloud"]
# }
# # print(student_data)
#
# # Iterate though the data
# for data in student_data.values():
#     if data == "Saim": # If condition is true then the loop exits
#         print(data)

# While loop is used to monitor the data

# ## First Iteration of while loop
# num = 0
#
# while num < 10: # while num value is less than 10
#     print(f"it's working -> {num}")
#     num += 1 # adding 1 into num value each time it iterates though

## Second iteration of while loop
# num = 0
#
# while num < 10:
#     print(f"It's working -> {num}")
#     if num ==5: # When condition is met the loop will exit
#         break
#     num += 1

## Third iteration of while loop
# Prompt user to input age and restrict in digits only
# check if the data is in digits display it back to the user if not in digits prompt the user with a message to enter in digits

age = input("What is your age? ")
Age = age.isdigit()

while Age > 0:
    print(f"Thank you! You are {age}")#
    break
else:
    print("Not valid")
