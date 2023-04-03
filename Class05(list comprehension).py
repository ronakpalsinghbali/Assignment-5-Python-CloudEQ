# List Comprehension:



# List Comprehension with comdition:

my_list = ["Apple","Mango","Banana","Kiwi","Watermelon","Cherry","Grapes"]

my_new_list = [ a for a in my_list if a != "Cherry"]

print(f"With condition: (Removed \"Cherry\")\n{my_new_list}")

print("")





# List Comprehension without comdition:



#(i) Example 1 :

my_list = ["Apple","Mango","Banana","Kiwi","Watermelon","Cherry","Grapes"]

my_new_list = [ a for a in my_list ]

print(f"Without condition:\n {my_new_list}")

print("")


#(ii) Example 2 :

my_new_list = [x for x in range(10)]

print(f"Without condition:\n {my_new_list}")


