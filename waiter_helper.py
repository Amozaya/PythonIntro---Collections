starter_menu = ["Bruschetta", "Parma Ham & Asparagus", "Mozzarella Fritta", "Sardine Fritta", "No Starter"]

main_menu = ["Pollo Milanese", "Branzino", "Riso Fungi", "Carbonara", "Margherita Pizza"]

dessert_menu = ["Limoncello Tart", "Amaretto Tiramisu", "Pannacotta", "No Dessert"]

drink_menu = ["Coke", "Sprite", "Juice", "Water", "No Drink"]

customers_order = []



#Add started selection
print("Please select your starter: ")
print(*starter_menu, sep=", ")

starter_selection = input()

customers_order.append(starter_selection)

#Add  main selection
print("Please select your main: ")
print(*main_menu, sep=", ")

main_selection = input()

customers_order.append(main_selection)

#Add dessert selection
print("Please select your dessert: ")
print(*dessert_menu, sep=", ")

dessert_selection = input()

customers_order.append(dessert_selection)

#Add drink selection
print("Please select your drink: ")
print(*drink_menu, sep=", ")

drink_selection = input()

customers_order.append(drink_selection)

#Print final order
print("Your final order is: ")
print(*customers_order, sep=", ")