# task 1
# list1 = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     list1.append(num)
# print("Numbers in list 1: ", list(list1))
# list2 = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     list2.append(num)
# print("Numbers in list 2: ", list(list2))
# combinedList = list1 + list2
# combinedList.sort()
# print("The sorted combined list: ", list(combinedList))

# task 2
# print("Smallest element:", min(combinedList))
# print("Largest element:", max(combinedList))

# task 3
# birthdays = {
#     "Albert Einstein": "03/14/1879",
#     "Benjamin Franklin": "01/17/1706",
#     "Ada Lovelace": "12/10/1815"
# }
# print("Welcome to the birthday dictionary. We know the birthdays of:")
# for name in birthdays:
#     print(name)
# name = input("Who's birthday do you want to look up? ")
# found = False
# for key in birthdays:
#     if key.lower() == name.lower():   # Compare in lowercase
#         print(f"{key}'s birthday is on {birthdays[key]}")
#         found = True
#         break

# task 4
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
new_dict = {}
for k in keys:
    new_dict[k] = sample_dict[k]
print("New dictionary:", new_dict)