class Calculator():
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print (f"Your answer is: {self.num1 + self.num2}")

    def substract(self):
        print (f"Your answer is: {self.num1 - self.num2}")

    def multiply(self):
        print (f"Your answer is: {self.num1 * self.num2}")

    def division(self):
        print(f"Your answer is: {self.num1 / self.num2}")


num_1 = int(input("Type the first number: "))
num_2 = int(input("Type the second number: "))

sum1 = Calculator(num_1, num_2)


print("1.Add\n"
      "2.Substract\n"
      "3.Multiply\n"
      "4.Division")


user_input = int(input("What would you like to do? "))


if user_input == 1:
    sum1.add()
elif user_input == 2:
    sum1.substract()

elif user_input == 3:
    sum1.multiply()

elif user_input == 4:
    sum1.division()

else:
    print("That's not possible. Please Try again")



