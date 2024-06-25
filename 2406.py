# find max normal

def findmax(seq):
    max_number = seq[0]
    for num in seq:
        if num>max_number:
            max_number=num
    return max_number

# Runtime --> amount of primitive operations required to solve problem

# Most preferred runtimes:
# 1. Constant (Good)
# 2. Logarithmic (Good)
# 3. Linear (Good)
# 4. Psuedo-Linear Time ---> n*log(n) (Good)
# 5. Quadratic and more (Bad)
# 6. Exponential 2^n (Worse)

# Sorting Algorithms:

l = [1, 3000, 4, 2, 45, 6, 65, 0]

# Bubble Sort

def bubblesort(seq):
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j]>seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        print(seq)

# Selection Sort

def selectionsort(seq):
    for i in range(len(seq)):
        minindex = i
        for j in range(i, len(seq)):
            if seq[minindex]>seq[j]:
                minindex = j
        seq[i], seq[minindex] = seq[minindex], seq[i]

        