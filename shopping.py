shoppinglist = ['tape', 'paper towels', 'soda pop', 'match box', 'match box']
def show():
    print(f'Here is the list so far: {shoppinglist} ')
def add_items():
    new_item = input('Do you wish to add something to the list?')
    if new_item in ['No','no','No.','no.']:
        pass
    elif new_item in ['Yes','yes','yes.','Yes.']:
        new_item2 = input('What item would you like to add to the list?').lower()
        position = input('Which position would you like to add your item?')
        if position.isdigit():
            position = int(position)
            if position < 0 or position > len(shoppinglist):
                print('Error. Try another position.')
                pass
            else:
                shoppinglist.insert(position, new_item2)
        else:
            print('Error. Try making the position an integer.')
            pass
    else:
        print('Error. Try making the item you wish to add a string.')
        pass
def remove_items():
    item_removed = input('Do you wish to remove any item from the list?')
    if item_removed in ['No','no','No.','no.']:
        pass
    elif item_removed in ['Yes','yes','yes.','Yes.']:
        item_removed2 = input('Which item would you like to remove from the list?').lower()
        if item_removed2 in shoppinglist:
            shoppinglist.remove(item_removed2)
        else:
            print('Error. Try making the item you want to remove in the list.')
            pass
on = True
while on:
    show()
    add_items()
    remove_items()
    show()
    result = input('If you are happy with the list, you can quit or continue.')
    if result in ['Quit','quit','I quit.','i quit.','quit.','Quit.']:
        print('Thanks for playing!')
        break
    else: 
        continue
