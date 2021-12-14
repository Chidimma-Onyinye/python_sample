import json

def read(name = None):
    with open("db.json", "r") as file:
        users = json.load(file)

        if name is not None:
            for user in users:
                if user['name'] == name:
                    return user  # user is an object {}
            else:
                return {}
                

        return users



def login(name, password):
    users = read(name)
    if users == {}:
        print("No such user")
    else:
        if users['password'] == password:
            print("Login Success!")
        else:
            print("Invalid password!!!")
        
           


login("Chidimma", "1234")



def create(name, password):
    users = read()
    user = read(name)
    # users is the former list
    if user == {}:
        profile = {"name":name, "password":password}
        users.append(profile)

        with open("db.json", "w") as file:
            json.dump(users, file, indent= 3)
            print("Profile Created!")
    else:
        print("User already exist")


create("Dans", "3245")