# find max normal

def findmax(seq):
    max_number = seq[0]
    for num in seq:
        if num>max_number:
            max_number=num
    return max_number

print(findmax([1, 2, 3,45, 4]))

# Runtime --> amount of primitive operations required to solve problem