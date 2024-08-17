# x=10/0

# try:
#     x = 10/0
# except:
#     print("Well that didn't work...")



try:
    answer = input ("What sould i divide 10 by?")
    num=int(answer)
    print(10/num)

except ZeroDivisionError as e:
    print("you can't divide by zero!")

except ValueError as e:
    print("you didn't give me a valid number!")
    print(e)

finally:
    print("This code always runs")