import heapq  # importing for our final heap function.

def readFile(fileName):
    file = open(fileName, 'r')
    finalResult = []
    for line in file:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word.strip():
                finalResult.append(word)
    # using same method to open our rand1000000.txt file
    # open a file
    # putting 10,000 integers in 100 different files.
    num_frame = [[0 for i in range(0, 10000)] for j in range(0, 100)]
    outputFile = open('sublist0.txt', 'w')
    row = 0  # will be index for example sublist [row]+.txt
    col = 0
    for line in finalResult:
        num_frame[row][col] = int(line)
        outputFile.write('%s,' % line)
        col += 1
        if (col % 10000 == 0):  # remainder ==0, we close the file
            outputFile.close()
            col = 0
            row += 1
            outputFile = open('sublist' + str(row) + '.txt', 'w')
    outputFile.close()


# finally 100 different files created.
fileName = "rand1000000.txt"
readFile(fileName)

# radix sort
def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10

# bucket sort code
def bucketSort(firstList):
    bucket = []
    slotNum = (max(firstList) - min(firstList) + 1) // len(firstList) + 1
    for i in range(slotNum):
        bucket.append([])
    for j in firstList:
        indexB = (j - min(firstList) + 1) // len(firstList)
        bucket[indexB].append(j)

    for i in range(slotNum):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(slotNum):
        for j in range(len(bucket[i])):
            firstList[k] = bucket[i][j]
            k += 1
    return firstList


# counting sort code
def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]





# create variable sorted_list
sorted_list = []
# now we want to go through lists 0-50 and perform bucket sort.
for i in range(0, 50):
    currentList = []  # set temp list empty
    file = open('sublist' + str(i) + '.txt', 'r')
    for line in file:
        line = line.strip()
        words = line.split(",")  # numbers are seperated by ','
        for word in words:
            if word.strip():
                currentList.append(int(word))  # add 'numbers aka words into current list.'
    file.close()
    bucketSort(currentList)  # perform bucket sort algorithm in currentList.
    # print(currentList)
    sorted_list.append(currentList)  # then put our sorted currentList into our sorted_list.
for i in range(50, 100):
    currentList = []
    file = open('sublist' + str(i) + '.txt', 'r')
    for line in file:
        line = line.strip()
        words = line.split(",")
        for word in words:
            if word.strip():
                currentList.append(int(word))
    file.close()
    radixSort(currentList)
    # print(currentList)
    sorted_list.append(currentList)

final = []  # final list.
queue = []  # setting open list for elements inside the queue.
list_no = 0

for list in sorted_list:
    heapq.heappush(queue, (list[0], list_no, 0))  # push first element from lists into our queue.
    list_no += 1  # move to next list index
while queue:
    number, list_index, number_index = heapq.heappop(queue)  # pop significant number from queue into final list
    final.append(number)
    number_index += 1  # going to next index

    if (number_index < len(sorted_list[list_index])):  # while we still have remaining numbers, we need to add to queue.

        heapq.heappush(queue, (sorted_list[list_index][number_index], list_index, number_index))
print(final)  # print final result
