*******************************************************
*  Name      :Suyog Dahal          
*  Student ID:109767594                 
*  Class     :  Computer Networks        
*  HW#       :  Programming assignment 1           
*  Due Date  :  March 31 2022
*******************************************************


                 Read Me


*******************************************************
*  Description of the program
*******************************************************
This program splits a list of 1,000,000 integers into 100 different sublists then sorts 50 sublists with radix sort and 50 with counting/bucket sorts. Then by using priority queue heap, we create an n log k merging method to merge each sublist after they have been already sorted. The program works successfully it runs well on pyCharm, but slow on repl. The extra credit is a webscraping code to pull the department name, phone number, and url from ucdenver website.

Answers to the written questions:

* 1: Psuedocode for priority queue/heapsort:
SortedList=[our 100 sorted lists]
	for list in sorted list:
		we are placing the first element of every list and index key into the priority queue(heap) which takes O(log k).
	while queue:(O(N)):
		#we want to get the most significant thing from priority queue which is min value.
		#this takes (O(logK))
		#then we are placing the next element from our sorted list into our priority queue

Why it is o(n l(og k)) runtime: To place all elements in k sorted lists into our priority queue it would take o(log k) runtime. Then placing all elements from our queue into our final fully sorted list, it would take o(n). When the two runtimes are combined we get O(n( Log K)) runtime.

Performance difference.
o n log k vs o n k. If K is constant then o(nk) is equal to o(n). But only if k is constant.

* 2: Question 2 I am going to submit as a seperate file so I can just fill in the table by hand on paper.


* 3: We would initialize the bit victor to match the length of the greatest value of the elements that are being stored. Each element is stored in the index that matches the value, so if you have 45 it is stored at index 45. You would then flip the bit from 0 to 1 for each element that appears in the vector.You would pass the number you want to perform an action on to perform any dictionary operations and since the index and value corresponds, any operation would take o(n) runtime.


* 4: Implementing a hash table w/ chaining makes this possible. It allows satellite data to be stored in a linked list. To solve the problem of non-distinct keys that are shared, each key would map to the sentinel of a double linked list. Insert would take o(1) because insertion is happening at the front. Delete takes o(1) because the chain is double linked list. And search also takes o(1) because it returns the first element of the linked list. 

* 5:def max_heapify(array, i):
  length= len(array)-1
  while i<= length:
      left = 2 * i
      right = 2 * i + 1
      largest = i

      if left <= length and array[i] < array[left]:
          largest = left
      if right <= length and array[largest] < array[right]:
          largest = right
      if largest != i:
          array[i], array[largest] = array[largest], array[i]
          max_heapify(array, largest)
      else:
          break
      return array

* *****************************************************
Extra Credit:
1.: Yes I read the following tutorials and got a good grasp.
2: Code for extracredit is in webscraping.py and output file is here too, it ran for me through terminal I haven't ran on repl the output that i displayed in my computer is also copied on here.
3:Not completed.
*******************************************************
*  Source files
*******************************************************

Name:  main.py
   

Name:  
   

Name: makefile
  
Name: yyy.h


Name: yyy.cpp
   
   
*******************************************************
*  Circumstances of programs
*******************************************************

   The program runs successfully. 

*******************************************************
*  How to build and run the program
*******************************************************

1. Uncompress the homework.  The homework file is compressed.  
   To uncompress it use the following commands 
       % unzip [1234HW1]

   Now you should see a directory named homework with the files:
        main.cpp
        xxx.h
        xxx.cpp
	yyy.h
	yyy.cpp
        makefile
        Readme.txt
	[any other supporting documents]

2. Build the program.

    Change to the directory that contains the file by:
    % cd [1234HW1] 

3. Run the program by:


4. Delete the obj files, executables, and core dump by
   %./make clean
