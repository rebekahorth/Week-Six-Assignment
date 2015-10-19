#Rebekah Orth with help from Dr. Neumann and working with Marissa Gross and Alicia Williams
#CIS 125- Week 6


def populate(world,h,w): 
    pass
def display(world,h,w):
    pass
def generation(world,h,w):
    pass

def main():
    import random
    world = []
    h = 22
    w = 80
    
    populate(world,h,w)
    
    x = input ("Press a key, Q stops the program ")
    while x != "Q":
        
        display(world,h,w)
        
        generation(world,h,w)
        
        x = input ("Press a key, Q stops the program ")
    
main()