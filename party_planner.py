#Create first function with parameters friends, cans, and packs
def plan_party(friends, cans, packs):
    #Find the amt of cans needed (include yourself) and initialize bonuscans
    amtofcans = (friends + 1) * cans
    bonuscans = 0
    #If there are cans left, subtract the amount of cans needed from the amount of cans you will have
    if (amtofcans % packs != 0):
        bonuscans = (amtofcans//packs+1) * packs - (amtofcans)
        print(f"{amtofcans//packs+1} {packs}-pack(s) needed")
        print(f"{bonuscans} extra can(s)")
    else:
        #Otherwise, print the amount of packs you need  
        print(f"{amtofcans//packs} {packs}-pack(s) needed")
        print(f"{bonuscans} extra can(s)")


def plan_party2(friends,cans,packs):
    #Find amt of cans needed (include yourself)
    amtofcans = (friends + 1) * cans
    if (amtofcans % packs != 0):
       #Find amount of packs needed, add 1 in order to round up the amount of packs
       packs = amtofcans//packs+1
       print(packs)
       return{packs}
       
    else: 
        #Print packs if there is no remainder
        packs = amtofcans//packs
        print(packs)
        return{packs}
#Prompt user for input, and validate those inputs
friends = int(input("How many friends are you throwing this party for? "))
if (friends < 0):
   while friends < 0: 
    friends = int(input("Can't have negative value, try again: "))
cans = int(input("How many cans will each person drink? "))
if (cans < 0):
   while cans < 0:
    cans = int(input("Can't have negative value, try again: "))
packs = int(input("How many cans are in each pack? "))
if (packs <= 0):
    while packs <= 0:
     packs = int(input("Must have at least 1 can per pack, try again: "))
#Put inputs into functions
plan_party(friends,cans,packs)
print(f"Return value from plan_party2: {plan_party2(friends,cans,packs)}")
        
