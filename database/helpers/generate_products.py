import json
import random

def randomDate():
    randomDay = random.randint(1,32)
    randomMonth = random.randint(1,13)
    randomYear = random.randint(1970,2001)

    if(randomMonth == 2 and randomDay > 28):
        randomDay = 28

    if(randomDay < 10):
        randomDay = "0"+str(randomDay)
    else:
        randomDay = str(randomDay)

    if(randomMonth < 10):
        randomMonth = "0"+str(randomMonth)
    else:
        randomMonth = str(randomMonth)

    randomYear = str(randomYear)
    return randomMonth + "/" + randomDay + "/" + randomYear

def generateProduct(productId, price, title, description):
    product = {}
    product["id"] = productId
    product["price_in_cents"] = price
    product["title"] = title
    product["description"] = description
    product["discount"] = {}
    return product

def generateUser(userId, firstName, lastName, dateOfBirth):
    user = {}
    user["id"] = userId
    user["first_name"] = firstName
    user["last_name"] = lastName
    user["date_of_birth"] = dateOfBirth
    return user

def generateProducts(n):
    products = []
    for product in range(1,n+1):
        products.append(generateProduct("ID"+str(product), random.randint(1,999), "Product "+str(product), "Description "+str(product)))
    return products

def generateUsers(n):
    users = []
    for user in range(1,n+1):
        users.append(generateUser("ID"+str(user), "First Name "+str(user), "Last Name "+str(user), randomDate()))
    return users

products = generateProducts(5)
#for product in products:
#    print(product)

users = generateUsers(5)
#for user in users:
#    print(user)

with open('products.json', 'w') as outfile:
    json.dump(products, outfile)

with open('users.json', 'w') as outfile:
    json.dump(users, outfile)