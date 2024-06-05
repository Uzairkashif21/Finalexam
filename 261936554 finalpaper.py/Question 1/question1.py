#Question 1
def decimal_binary(a):
    if  a== 0:
        return "0"
    
    elif a== 1:
        return "1"
    return decimal_binary(a//2)+str(a%2)

decimal_number= 20
binary_representation = decimal_binary(decimal_number)
print(f"binary number {decimal_number} in binary represenation is {binary_representation}")
