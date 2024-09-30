def reverse_string(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


input_string = input("Digite a string que deseja inverter: ")
result = reverse_string(input_string)

print(f"String invertida: {result}")