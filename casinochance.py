def roll(num1, num2):
    times1 = dice_nums.count(num1)
    times2 = dice_nums.count(num2)
    prob = ((times1/6)*(times2/6))*100
    return prob

finding_nums = input("Input the 2 numbers that you want to roll for: ")
find_num1, find_num2 = finding_nums.split()
dice_nums = input("Input the numbers on the die you want to roll: ")
print(roll, "% chance of rolling")