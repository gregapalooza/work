#An app for buying a car
#Greg Vaggalis

from tkinter import *

def vehicle():

    vehicle_price = 0
    #finds vehicle price .get() recieves info from radiobutton
    if car_choice.get() == "sedan":
        vehicle_price += 10000
    elif car_choice.get() == "jeep":
        vehicle_price += 15000
    elif car_choice.get() == "truck":
        vehicle_price += 20000

    engine_price = 0
    #finds engine price .get() recieves info from radiobutton
    if engine_upgrade.get() == "large":
        engine_price += 5000
    elif engine_upgrade.get() == "medium":
        engine_price += 2500
    elif engine_upgrade.get() == "small":
        engine_price += 1000

    total_price = vehicle_price + engine_price #finds total

    lines = "Here is the receipt for your purchase.\nYou've chosen a " + str(car_choice.get()) + " with a " + str(engine_upgrade.get()) + " engine upgrade.\nYour total for the vehicle you chose is " + str(total_price) + " dollars.\n"
    #writes purchase history
    boxSummary.delete('1.0', END)
    boxSummary.insert('1.0', lines)

def save_receipt():
    #writes a save file, user opens receipt file to see updated receipt file
    text_file = open("reciept.txt", "w+")
    receipt = boxSummary.get('1.0', END)
    text_file.write(receipt)
    text_file.close()
    

#creation of window
root = Tk()
root.title("Greg's Car Dealership")
root.geometry("800x500")

car_design = Label(root, text = "Please choose your car preference:")
car_design.grid(row = 0, column = 0, columnspan = 2, sticky = W)

car_choice = StringVar()
car_choice.set("sedan")

car_choices = ["sedan", "jeep", "truck"] #car choice radiobutton
column = 1
for car in car_choices:
    Radiobutton(root,
                text = car,
                variable = car_choice,
                value = car
                ).grid(row = 1, column = column, sticky = W)
    
    column += 1

engine_choiceLabel = Label(root, text = "Please choose your engine upgrade:")
engine_choiceLabel.grid(row = 2, column = 0, columnspan = 2, sticky = W)

engine_upgrade = StringVar()
engine_upgrade.set("large")

engine_upgrades = ["large", "medium", "small"] #engine upgrade choice radiobutton
column = 1
for upgrade in engine_upgrades:
    Radiobutton(root,
                text = upgrade,
                variable = engine_upgrade,
                value = upgrade
                ).grid(row = 3, column = column, sticky = W)

    column += 1

calculateButton = Button(root, text = "Calculate", command = vehicle) #button to execute program
calculateButton.grid(row = 4, column = 0, sticky = E)

boxSummary = Text(root, width = 75, height = 10, wrap = WORD) #textbox to inform price
boxSummary.grid(row = 5, column = 0, columnspan = 4)

saveButton = Button(root, text="Save my purchase", command = save_receipt) #saves receipt
saveButton.grid(row = 6, column = 1, sticky = W)

root.mainloop()
