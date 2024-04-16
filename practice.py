from datetime import date

name = "Ben"

def greeting(name):
    print(f"Hello {name}")
    print(f"Nothing, {name}")

    print(f"Still nope {name}")



    print(f"this? {name}")
print(f"what about now? {name}")

print(f"nowwww? {name}")

greeting("JASON")

print(f"sure this is.. {name}")


def count():
    print("One")
    print("Two")
    print("Three")
    return
    print("Four")
    print("Five")


count()

def day_of_week():
    day = date.today().strftime('%A')

    if(day == "Wednesday"):
        return f"It is {day}"
    
    return f"It's {day}"

today = day_of_week()
print(today)

def add_two_numbers(num1, num2):
    maxNum = max(num1, num2)
    return maxNum

print(add_two_numbers(6, 4))

def print_hello(greeting = "hi"):
    print(greeting + "!!!")

print_hello()
print_hello("WHATS UP")

def calculate_tax(price, shipping, tax_rate, member_discount):
    return (price + (price * tax_rate)) + shipping - member_discount

print(calculate_tax(100, 10, 0.2, 10))
print(calculate_tax(100, 10, 10, 0.2))
print(calculate_tax(shipping=10, tax_rate=0.2, price=100, member_discount=10))


num = 9
total = num * 3
print(total)


