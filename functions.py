# def sample(name,age):  #Void Function
#         print("Name :" + name + "Age :" + age)
# sample("hari", "23")
    
    
# def name_Name(name,age):
#     print("Name :" + name +" "+ "Age :" + age)
# name_Name("Hari", "23")

#Non - Void Function: 
# def add_val(a, b):
#     return a + b

# val1 = 5
# val2 = 10
# result = add_val(val1, val2)
# print("The sum is:", result)


# def Hari_1(name,name1):
#     return name + name1

# val_01 = "hari"
# val_02 = "haran"
# result = Hari_1(val_01,val_02)
# print("The Total is :", result)




# Arguments Types:
#------------------------------
# Default
# Keyword
# Required
# Variable - length


# Keyword Arguments:
# def area_rectangle(length,width):
#     area = length * width
#     return area
# rectangle_area = area_rectangle(length=50, width=90)
# print(rectangle_area) 

#position Arguments:
# def area_triangle(breadth,width):
#     area = breadth * width
#     return area
# triangle = area_triangle(50,5)
# print(triangle)

#Default Arguments:
def area_pyramids(length=56, breadth =80):
    area = length * breadth
    return area
pyramids = area_pyramids()
print(pyramids)


# mystring = "*****"
# x = 0

# for i in mystring:
#     x = x+1
#     print(mystring[0:x])

# for i in mystring:
#     x = x-1
#     print(mystring[0:x])  