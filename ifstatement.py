# a = "Naveen"
# b = "Sneha"

# if a<b and b>a:
#     print("Will be married Soon")
# else:
#     print("Otherwise they got breakup")

# print(bool("Python"))  

# F String
# age = 23
# a = f"My age is {age}"
# print(a)

# int = int(input("Enter a number: "))

# if int % 2 != 0:
#     print(f"{int} is an odd number.")
# else:
#     print(f"{int} is an Even number.")


# for i in range(1, 101):   
#     if i % 2 == 0:  
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

#///////////////////////////////////////////////////////////


# hari = 18  #Lites
# naveen = 15  #Gram

# if hari < naveen and hari > naveen:
#     print("Sabash da mahane🙌")
# elif hari == naveen or hari != naveen:
#     print("Mathikita pangu 🤣")
# else:
#     print("Mission Successful👍")

# print("Mattikita pangu 🤣") if hari > naveen else print("I'm Batman 🦇")




# a = 10
# b = 10

# if a < b:
#     print("Is Equal to the statement")
# elif a > b:
#     print("is Not Equal to")
# else:
#     print("Otherwise Exits")


# hari = "meghna"
# naveen = "Sneha"

# if hari > naveen:
#     print("Naveen Has been Rejected From Sneha")
#     if hari == naveen:
#         print("Hari Got Rejected From the meghna")
#     else:
#         print("Otherwise Both are Selected From the Both Peoples")


# DSA Program
def two_sum(nums, target):
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))



# Total1 =int(input("Enter the first number: "))
# Total2 = int(input("Enter the second number: "))

# sum = Total1 + Total2
# Sub = Total1 - Total2
# Div = Total1 / Total2
# Mul = Total1 * Total2
# print("The sum of", Total1, "and", Total2, "is:", sum)
# print("The Sub of", Total1, "and", Total2, "is:", Sub)
# print("The Div of", Total1, "and", Total2, "is:", Div)
# print("The Mul of", Total1, "and", Total2, "is:", Mul)


#odd or Even

# Num_1 = int(input("Enter the Value :"))

# if Num_1 % 2 == 0:  
#   print(f"{Num_1} is even")
# elif Num_1 % 2 == 0:
#   print(f"{Num_1} id odd")
# else:
#   print("Error")

# While Loop -- its continue the statement is while is true

# num = 1 
# while num < 100:
#     print(num)
#     num += 1


# For Loop

# for fr in range(1,20,2):
#     print(fr)


# for name in "Banana":
#     print(name)

# color = ["Hello", "World", "Computer"]
# for x in color:
#     print(x)


# Name = ["Hariharan", "Naveen","Sharan"]
# for c in Name:
#     if c == "Hariharan":
#         continue
#     print(c)
# else:
#     print("The Plan is succesful")





