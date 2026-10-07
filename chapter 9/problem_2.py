# write a program to generat multiplication table from 2 to 20 and write it to the  differnt file place these files in a folder for a 13 -year old child.

def generateTable (n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

        with open (f"table/table_ {n}", "w") as f:
            f.write(table)





for i in range(2, 21):
    generateTable(i)            
