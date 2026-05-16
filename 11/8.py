def sort_string(s):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

input_string = input()
result = sort_string(input_string)
print(result)