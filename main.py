"""
JSON: Javascript Object Notation
[]., incase you forget what operation to perform
whatever you can do with your map, you can do with your list comprehension, learn LC well

JSON is what the backend sends to the frontend
It is a native JS datatype

load - get data from a json file
loads - writing(sending data) to a json file
loads - get data from a string with json content
dumps - converting data to a string with json content

WEB 3
WEB 3 JS
"""

import json

# data = """{
#      "name":"Chidimma",
#     "password":"1233"
# }"""

# data_stuffs = json.loads(data)
# print(data_stuffs['name'])

# user = {
#      "name":"Chidimma",
#     "password":"1234"
# }

# user_json = json.dumps(user)
# print(type(user_json))
# print(user_json)


# with open("db.json") as file:
#     content= json.load(file)
#     print(type(content))
#     print(content)


with open("db.json", "w") as file:
    content = [
        {
            "name":"Chidimma",
            "password":"1234"
        },

        {
            "name":"Mma",
            "password":"3334"
        }

    ]
    json.dump(content, file, indent= 3)






# request = {
#     "name":"Chidimma",
#     "email":"mma@gmail.com",
#     "subjects": ["Maths", "English", "Physics", "Chemistry"]
# }




# # Average of numbers
# numbers = input("\n Enter the numbers, separated by a comma: \n")
# # "".split
# numbers_list = numbers.split(",")
# # print(numbers_list)


# numbers_convert = [int(number) for number in numbers_list]  #representing the individual numbers
# # print(numbers_convert)
# avg = sum(numbers_convert)/ len(numbers_convert)
# print(avg)
