import math
def busamount(students):
    busnum = math.ceil(students/52)
    return busnum

students = int(input("How many students are there: "))
print(busamount(students), "buss(es)")