1) Build a Shopping Cart
You can use either lists or dictionaries. The program should have the following capabilities:

1) Takes in input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, print out all items in the user's list
from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def MakeShoppingList():
    ShoppingList = ["Eggs", "Milk", "Bacon", "Chips"]
    WhatDo = input("Would you like to 'Show', 'Add' to, or 'Delete' and item from the list? (type 'quit' to quit)" )
    while WhatDo != 'quit':
        if WhatDo == "Show":
            return ", ".join(ShoppingList)
        elif WhatDo == "Add":
            AddSL = input("What would you like to add? (type 'quit' to quit) ")
            ShoppingList.append(AddSL)
            if AddSL == "quit":
                ShoppingList.pop()
                print(ShoppingList)
                break
            else:
                continue
        elif WhatDo == "Delete":
            DelSL = input("What would you like to delete? ")
            if DelSL == "quit":
                return ", ".join(ShoppingList)
                break
            else:
                ShoppingList.remove(DelSL)
                continue
        else:
            print("Please type 'Show', 'Add', or 'Delete")
            break
MakeShoppingList()
'Eggs, Milk, Bacon, Chips'