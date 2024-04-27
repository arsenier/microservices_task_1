def filter(is_good, arr):
    out = []
    for line in arr:
        if(is_good(line)):
            out.append(line)

    return out

data = [
    "one two three",
    "onetwothree",
    "abcd",
    "efgh"
]

print(filter(lambda str : ' ' not in str, data))
print(filter(lambda str : str[0] == 'a', data))
print(filter(lambda str : len(str) < 5, data))