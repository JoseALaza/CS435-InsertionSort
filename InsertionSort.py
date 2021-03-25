import random

compcount = 0

def avgList(size):
    AvgList = list(range(1, size+1))
    random.shuffle(AvgList)
    return AvgList

def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def insertionSort_mod(values):
    k = 0
    n = len(values) - 1
    global compcount
    compcount = 0
    while k+1 <= n:
        i = k+1
        curr_val = values[i]
        compcount += 1
        while i>0 and values[i-1] > curr_val:
            values[i] = values[i-1]
            i=i-1
            compcount += 1
        values[i] = curr_val
        k = k + 1
    return values, compcount


size = int(input("Please enter an N-Size: "))
repeats = int(input("Please enter an N number of times to run Average case: "))

avgComp = 0.0


bestCase = list(range(1, 33))
worstCase = list(reversed(bestCase))

f = open('result.txt', 'w')

f.write("Best Case array\n" + str(bestCase) + "\n")
arr, comp = insertionSort_mod(bestCase)
f.write("Sorted array\n" + str(arr) + "\nComparison Count: \n" + str(comp) + "\n")

f.write("\nWorst Case array\n" + str(worstCase) + "\n")
arr, comp = insertionSort_mod(worstCase)
f.write("Sorted array\n" + str(arr) + "\nComparison Count: \n" + str(comp) + "\n")

for i in range(repeats):
    avg = avgList(size)
    f.write("\nAverage Case array\n" + str(avg) + "\n")
    arr, comp = insertionSort_mod(avg)
    f.write("Sorted array\n" + str(arr) + "\nComparison Count: \n" + str(comp) + "\n")
    avgComp += comp
f.write("Average result of random size N: " + str(avgComp/repeats))

f.close()
