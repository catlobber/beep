#create function 
def show_verses(drink,n):
    #while loop, looping as long there are cans, if there is one can it prints the statements as shown
    while n != 0:
        if n == 1:
            print(f"1 can of {drink} on the wall.")
            print(f"1 can of {drink}.")
            print(f"Take one down, pass it around,")
            print(f"No more cans of {drink} on the wall.")
            n -= 1
            #otherwise, print as normal
        else:
            print(f"{n} cans of {drink} on the wall,")
            print(f"{n} cans of {drink}.")
            print(f"Take one down, pass it around,")
            if (n - 1) == 1:
                print(f"1 can of {drink} on the wall.")
            else: 
                print(f"{n} cans of {drink} on the wall.")
            n -= 1
#get user input
drink = input("What are we drinking today?")
n = int(input("And how many cans are we starting with?"))
#input validation
while n <= 0:
    n = int(input("Must have at least 1 can, try again: "))
show_verses(drink,n)