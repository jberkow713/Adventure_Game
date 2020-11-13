from tabulate import tabulate

# text = input("Please enter your name: \n")
# text2 = (f"Welcome {text}")
# table = [[text]]
# table2 = [[text2]]
# output = tabulate(table, tablefmt='grid')
# output2 = tabulate(table2, tablefmt='grid')
# print(output)
# print(output2)


def text_box(input_str, formt):

    table = [[input_str]]
    if formt is 1:
        output = tabulate(table, tablefmt= "fancy_grid" )
    elif formt is 2:
        output = tabulate(table, tablefmt= "grid" )
    elif formt is 3:
        output = tabulate(table, tablefmt= "plain" )
    
    return(print(output))

def printline():

    return(print('-------------------------------------'))    

# text_box("You may quit at any time during the game by typing q as an answer to any prompt", 1)
# text_box("You may quit at any time during the game by typing q as an answer to any prompt", 2)
# text_box("You may quit at any time during the game by typing q as an answer to any prompt", 3)






    




   