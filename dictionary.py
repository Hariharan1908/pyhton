bike = {
    "model" : "r15v3",
    "brand" : "Yamaha",
    "Year" : 2021,
    # "CO_brands" :["beneli", "BMW", "Daytona"]
}
print(bike)

bike.update({"year" : 2022})
print(bike)
# print(len(bike))
# print(bike.values())
# print(bike.keys())
# print(bike.items())
# print("model" in bike)

# bike["model"] = "r15v4"
# print(bike)