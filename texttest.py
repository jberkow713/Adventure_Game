from tabulate import tabulate

# text = input("Please enter your name: \n")
# text2 = (f"Welcome {text}")
# table = [[text]]
# table2 = [[text2]]
# output = tabulate(table, tablefmt='grid')
# output2 = tabulate(table2, tablefmt='grid')
# print(output)
# print(output2)


def text_box(input_str):

    table = [[input_str]]
    output = tabulate(table, tablefmt='grid')

    return(print(output))

def printline():

    return(print('-------------------------------------'))    

   