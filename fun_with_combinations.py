#create function for factorial
def product_between(a,b):
    #while the first number is greater than the second, multiply the first number by the first number - 1 and save the product in variable c.
    c = a
    while a > b:
        c *=  (a-1)
        a -= 1
    return c
#create function for n choose k
def n_choose_k(n,k):
    #use the efficient equation for n choose k
    nchoosek = product_between(n,n-k+1)//product_between(k,1)
    return nchoosek
#create function for number of possible tickets
def num_possible_tickets(n,k,m):
    #use equation 3 and save it in variable, return variable
    possibletickets = m * n_choose_k(n,k)
    return possibletickets

print("product_between Function")
print(product_between(5,1))
print(product_between(5,3))
print(product_between(5,5))
print(product_between(10,2))
print(product_between(15,5))
print("n_choose_k Function")
print(n_choose_k(4,1))
print(n_choose_k(4,2))
print(n_choose_k(4,4))
print(n_choose_k(16,2))
print(n_choose_k(19,5))
print("num_possible_tickets Function")
print(num_possible_tickets(4,1,5))
print(num_possible_tickets(4,2,21))
print(num_possible_tickets(4,4,1))
print(num_possible_tickets(69,5,26))
print(num_possible_tickets(44,2,19))