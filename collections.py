#lists

#list = array

#Shopping list

# shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]
#
# print(shopping_list)
# print(type(shopping_list))
#
# #Accessing a particulart part of the list
#
# print(shopping_list[0])
#
# #change an element in a list
# shopping_list[2] = "butter"
# print(shopping_list)
#
# #using list methods
# #adding to a list with append()
#
# shopping_list.append("chicken")
# print(shopping_list)
#
# #removing item with remove()
# shopping_list.remove("bread")
# print(shopping_list)
#
# #removing the last item fro a list, without specifying what it is
# shopping_list.pop()
# print(shopping_list)
#
# #Mix data type list
# mixture = [1, 2, 3, 4.5, "five", "six", True]
# print(mixture)
#
# #list slicing
# print(mixture[0:3])
#
# #reverse the order of the slice
# print(mixture[-2::])
#
# #Step over
# print(mixture[::2]) #skip every 2nd item on the list
#
# #Tuples
# #Tuple are Immutable - cannot be changed
#
# tuple_example = ("bread", "eggs", "milk")
# print(tuple_example)


#DICTIONARY - Another way to manage data, but they are a little bit more dynamic and complex
#Key  - Value - Pairs

#Key - is a reference to the object
#Value - the data you wish to store (string, int, float, Bool, list, dictionary)

# student_1 = {
#     "name": "Oleg",
#     "surname": "Fursa",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["variable", "data_types", "setup"]
# }
#
# #Access the dictionary
#
# print(student_1["stream"])
#
# #Access a part of the list in the dictionary
# print(student_1["completed_lesson_names"][0]) #gives Variable from the list in the dictionary
#
# #Changing a value in the dictionary
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# #Change an element in the list within dictionary
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])
#
# #Dictionary methods
# print(student_1.keys())
# print(student_1.values())

#Sets and Frozen sets

#set in Python is a list that has no order/indexing

# car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)
#
# car_parts.add("windows")
# print(car_parts)
#
# car_parts.discard("doors")
# print(car_parts)
#
# #Frozen sets - immutable set
#  x = frozenset([1, 2, 3, 4])

