products = ["Television","Freezer","Computer","Oven"] # We defined a list that create from 4 elements as television,freezer,computer,oven and assigns this list to products variable.

print(products) # We printed products variable here.

print(len(products))  # We printed length of products list.

print(products[0:2]) # We printed elements that be  from first to third index in products list.

print(products[0],products[len(products)-1]) # We printed elements first and last index of product list.

products[len(products)-1] = "Iron" # We assigned Iron string expression to last index of products list.

print(products) # We printed products list.

products = products + ["Washing machine"] # We combined product list and a list that contain washine machine string expression and assigned to products variable.

print(products) # We printed products variable.

print(products[::-1]) # We printed the products list in reverse order.