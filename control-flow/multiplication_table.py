number = int(input("Enter a number to see its multiplication table: "))
for multiplier in range(1, 11):
    product = number * multiplier
    print(f" {number} * {multiplier} = {product}")
    