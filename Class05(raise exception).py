# Raising an exception:
# We can raise an exception by using the "raise" keyword.



user_input = (input("Enter a number between 0 and 10:"))
g = int(user_input) 


if g < 0 or g > 10 :
    raise Exception("PLEASE ENTER NUMBERS BETWEEN 0 AND 10 !!!!")

else:
    print(f"Thank you!\nYour bank account will be credited with Rs.{g*10000} soon.")
