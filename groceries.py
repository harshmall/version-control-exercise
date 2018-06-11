# groceries.py

from IPython import embed

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#
#1. Print all products (already done for you!).

#print(products)

#2. Print the first product.
#print (products[0])

#3. Print the name of the first product.
#print (products[0]["name"])

#first_product = products[0]
#print(first_product["name"])

#4. Print the number of products.
#print(len(products))

#5. Print the name of each product
#for product in products:
    #print (product["name"])

#product_count_message = "THERE ARE " + str(len(products)) + " PRODUCTS:"
#
#print("--------------")
#print(product_count_message)
#print("--------------")
#
##for product in products:
##    print(" + " + product["name"])
#
#def sort_by_name(product):
#   return product["name"]
#
#6. Print in alphabetical order the name of each product.
#products = sorted(products, key=sort_by_name)
#
##
###7. Print in alphabetical order the name of each product, and include its price rounded to two decimal places.
#for product in products:
#    price_usd = '${0:.2f}'.format(product["price"])
#    print(" + " + product["name"] + " " + "("  + price_usd + ")")
#
#-------------------
#-------------------

#8. Print the number of unique departments.

departments =[] #create new empty list called departments
#
for product in products:
    departments.append(product["department"]) #call on any list to add a new item to the list
#
departments = list(set(departments)) #remove duplicates from the list 'departments'
#
departments.sort() #sorting by alphabetical order
#
department_count_message = " THERE ARE " + str(len(departments)) + " DEPARTMENTS:"
#
print("--------------")
print(department_count_message)
print("--------------")
#
#def products_belonging_to(dept_name):
#    return [product for prodt in products if product["department"] == dept_name]
#    #for product in products:
#    #        if product["department"] == dept_name:
#    #            new_products.append(product)
#    #return new_products # TODO: look up all products belonging to the department
#
#for department in departments:
#    associated_products = products_belonging_to(department)
#    label = "products"
#    if len(associated_products) == 1:
#        label = "product"
#    print(" + " + department.title() + " (" + str(len(associated_products)) + " " + label + ")")



    #count = 0
    #for product in products:
    #    if (product["department"]==department):
    #        count = count+1
    #if(count==1):
    #    print(" + "+department.title()+" ("+str(count)+" product)")
    #else:
    #    print(" + "+department.title()+" ("+str(count)+" products)")


#9. Print the name of each unique department.
#list(set(department))

    #Print in alphabetical order the name of each unique department.
    #Print in alphabetical order the name of each unique department, as well as the number of products associated with that department.
