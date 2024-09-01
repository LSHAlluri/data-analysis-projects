
food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
# converting strings to lists
foodList = food.split(',')
equipmentList = equipment.split(',')
petsList = pets.split(',')
sleep_aidsList = sleep_aids.split(',')
# sorting the lists alphabetically
foodList.sort()
equipmentList.sort()
petsList.sort()
sleep_aidsList.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [foodList, equipmentList, petsList, sleep_aidsList]
print("Cargo hold contents are:\n{0}\n{1}\n{2}\n{3}".format(cargo_hold[0],cargo_hold[1],cargo_hold[2],cargo_hold[3]))

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.he
cabinetNum = int(input("0.Food\n1.Equipment\n2.Pets\n3.Sleepaids\nSelect a cabinet from the cargo hold: "))

# # d) Use bracket notation and format to display the contents of the selected cabinet. 
# # If the user entered an invalid number, print an error message.
# if cabinetNum in (0,1,2,3):
#     print(cargo_hold[cabinetNum])   
# else:
#     print("Invalid input!")

# # e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. 
# # Use the in method to check if the cabinet contains the selected item, then print 
# # “Cabinet ____ DOES/DOES NOT contain ____.”
# cabinet = int(input("0.Food\n1.Equipment\n2.Pets\n3.Sleepaids\nSelect a cabinet from the cargo hold: "))
zero = "Food"
one = "Equipment"
two = "Pets"
three = "Sleepaids"

if cabinetNum in (0,1,2,3):
    cabinetItem = input("Enter the item you want to check availability for: ")
    if cabinetItem in cargo_hold[cabinetNum]:
        print("The cabinet contains {0}.".format(cabinetItem))
    else:
        print("The cabinet does NOT contain {0}!".format(cabinetItem))
else:
    print("Invalid input!")
