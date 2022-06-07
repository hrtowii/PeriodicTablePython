
# Initially my approach was to create a class w/ properties and use eval() to add them to a dictionary to be printed. i didnt get it to work though so just directly add them to a dictionary
# My second approach was to use 1 list for every element and try to print out the properties in the list but i kept facing some problem because the index was weird
# Last approach which seems to work is to use 4 lists, each containing an element's specific property. Easier to use. Done w/ my friend's help
class element(): #Each element has 4 lists, MakeElement, and display() functions
    ElementNameList = []
    ElementSymList = []
    ElementProlist = []
    ElementMassList = []
    def __init__(self):
        pass
    def MakeElement(self, name, symbol, proton, atomic):
        self.ElementNameList.append(name)
        self.ElementSymList.append(symbol)
        self.ElementProlist.append(proton)
        self.ElementMassList.append(atomic)
    def display(self, target): # made by friend
        try:
            index = NewElement.ElementNameList.index(target) #If element name is in the list, stop. If not, continue on the try/except
        except:
            try: 
                index = NewElement.ElementSymList.index(target) #If element symbol is in the list?
            except:
                try:
                    index = NewElement.ElementProlist.index(target) #If element proton number is in the list?
                except:
                    try: 
                        index = NewElement.ElementMassList.index(target) #If element mass number is in the list?
                    except:
                        print("No value found")
                        return 0
        print("Element Name: " + NewElement.ElementNameList[index])
        print("Element Symbol: " + NewElement.ElementSymList[index])
        print("Element Proton Number: " + NewElement.ElementProlist[index])
        print("Element Mass Number: " + NewElement.ElementMassList[index])



# Make an element
def create():
    name = input("Input name: ")
    symbol = input("Input symbol: ")
    proton = input("Input proton number: ")
    atomic = input("Input mass number: ")
    NewElementLocal = element()
    NewElementLocal.MakeElement(name, symbol, proton, atomic)
    print("done.")
    return NewElementLocal

#Menu

#can't use list() because it's overloaded, replace with pee()
def pee():
    global NewElement
    #terrible organisation
    operation = input('''Select operation:\n [1] Create element \n [2] See element \n [3] Remove element\n ''')
    if operation == '1':     
        NewElement = create()
        pee()
    elif operation == '2':
        def show():
            target = input("Input name, symbol, proton number, or mass number: ")
            NewElement.display(target)
        show()
        pee()
    elif operation == '3': #HOW DO I DO THIS?
        def RemoveElement(): # made by friend
            global NewElement
            RemovedElement = input("Which element to be removed? ")
            try:
                index = NewElement.ElementNameList.index(RemovedElement) #Same as display but use .pop(index) to remove the elements from the lists.
            except:
                try: 
                    index = NewElement.ElementSymList.index(RemovedElement)
                except:
                    try:
                        index = NewElement.ElementProlist.index(RemovedElement)
                    except:
                        try: 
                            index = NewElement.ElementMassList.index(RemovedElement)
                        except:
                            print("No value found to remove")
                            return 0
            NewElement.ElementNameList.pop(index)
            NewElement.ElementSymList.pop(index)
            NewElement.ElementProlist.pop(index)
            NewElement.ElementMassList.pop(index)
            namelist = ', '.join(NewElement.ElementNameList) # print the list in a pretty way.
            print("Successfully removed. New list of elements: " + namelist)

        RemoveElement()
        pee()
    else:
        print('You have not chosen a valid option.')
        again()

def again():
    list_again = input('''Would you like to see main menu again? (Y/N)''')
    if list_again == 'Y' or list_again == 'y':
        pee()
    elif list_again == 'N' or list_again == 'n':
        print('OK. Bye bye. :)')
    else:
        print("read properly pls")
        again()

pee()