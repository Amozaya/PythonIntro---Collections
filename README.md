# Waiter Helper program

## List

This section of code creates a list of starter, main, dessert and drinks menu

```
starter_menu = ["Bruschetta", "Parma Ham & Asparagus", "Mozzarella Fritta", "Sardine Fritta", "No Starter"]

main_menu = ["Pollo Milanese", "Branzino", "Riso Fungi", "Carbonara", "Margherita Pizza"]

dessert_menu = ["Limoncello Tart", "Amaretto Tiramisu", "Pannacotta", "No Dessert"]

drink_menu = ["Coke", "Sprite", "Juice", "Water", "No Drink"]
```

## Customer order list

This list stores all the customers selections
```
customers_order = []
```

## Customer selections

This code allows customer to see all the options available on the menu and make their selection.

I have also added formatting to print(), so lists are more readable:

``print(*starter_menu, sep=", "``
In this case, ``*starter_menu`` used to print all the list items separately, without brackets, and ``sep=", "`` used to add formatting, so each list item will be separated by come and space between them.

```
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
```
Final part of the code tells customer what their order is
```
#Print final order
print("Your final order is: ")
print(*customers_order, sep=", ")
```