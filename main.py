import numpy as np
import time
import sys

# Bubble Sort Implementation
# Resource: https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(arr):
    n = len(arr)
     
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    
    return arr

# Merge Sort Implementation
# Resource: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Quick Sort Implementation
# Resource: https://www.geeksforgeeks.org/quick-sort/
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

# Radix Sort Implementation
# Resource: https://www.geeksforgeeks.org/radix-sort/
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

def fillBestCase(arr, length):
    for x in range(length):
        arr[x] = x

def fillAverageCase(arr, length):
    for x in range(length):
        arr[x] = np.random.randint(1, length)

def fillWorstCase(arr, length):
    for x in range(length):
        arr[x] = length-x

#############
# Main Code #
#############

if __name__ == "__main__":
    #Increase python recursion limit since python is rude
    sys.setrecursionlimit(100000)

    #Print welcome message
    print("Welcome to the test suite of selected sorting algorithms!")

    #Open the output file and initialize the string to add everything to
    file = open('output.txt', 'w')
    completeString = ""

    #Control variables
    quit = 0
    scenario = 0

    #Main loop checking whether the user wants to quit or not
    while quit != 5:
        #Get the users choice
        quit = int(input("Select the sorting algorithm you want to test.\n-------------------------\n1. Bubble Sort\n2. Merge Sort\n3. Quick Sort\n4. Radix Sort\n5. Exit\n\nSelect a sorting algorithm (1-5): "))

        #Matching that variable to see what sort they would like to test
        match quit:
            #Case 1 is for the Bubble Sort Method
            case 1:
                #Get the user's wanted scenario
                scenario = int(input("Case Scenarios for Bubble Sort\n---------------\n1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit bubble sort test\n\nSelect the case (1-4): "))

                #Match the user's inputted scenario
                match scenario:
                    #Case 1 is for Best Case Array Sort
                    case 1:
                        #Set length of array
                        n = 100
                        
                        #Base case loop 
                        for _ in range(3):
                            #Initialize array with n length
                            arr = [0] * n
                            #Fill array with best case
                            fillBestCase(arr, n)
                            
                            #Test the sort
                            start = time.time()
                            bubbleSort(arr)
                            end = time.time()
                            
                            #Print results and input them into a file
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            
                            #Increment array size
                            n*=10

                        #Ask the user if they want to input their own size
                        #This assumes that the user wants to test the same case 
                        #Whether that be best, average, or worst
                        #This is the loop for it to happen multiple times
                        while 1 == 1:
                            #Ask if the user wants to input another
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                #Ask the user for the size of N
                                n = int(input("What is the N? "))
                                #Initialize the size of the array to N
                                arr = [0] * n
                                #Fill the array with Best case in relation to size n
                                fillBestCase(arr, n)

                                #Test the sort
                                start = time.time()
                                bubbleSort(arr)
                                end = time.time()

                                #Print the results and input them into a file
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            #If the user doesn't want to input their own values
                            #Break from the while loop
                            else:
                                break
                    #This follows the same pattern where this is the average case for bubble sort
                    case 2:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillAverageCase(arr, n)

                            start = time.time()
                            bubbleSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillAverageCase(arr, n)

                                start = time.time()
                                bubbleSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break 
                    #This follows the same pattern where this is the worst case for bubble sort
                    case 3:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillWorstCase(arr, n)

                            start = time.time()
                            bubbleSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillWorstCase(arr, n)

                                start = time.time()
                                bubbleSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Bubble Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
            #This is the case for Merge Sort
            case 2:
                scenario = int(input("Case Scenarios for Merge Sort\n---------------\n1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit merge sort test\nSelect the case (1-4): "))
                
                match scenario:
                    #This follows the same pattern where it is the best case for Merge Sort
                    case 1:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillBestCase(arr, n)
                            
                            start = time.time()
                            mergeSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillBestCase(arr, n)

                                start = time.time()
                                mergeSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the average case for Merge Sort
                    case 2:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillAverageCase(arr, n)

                            start = time.time()
                            mergeSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillAverageCase(arr, n)

                                start = time.time()
                                mergeSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the worst case for Merge Sort
                    case 3:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillWorstCase(arr, n)

                            start = time.time()
                            mergeSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillWorseCase(arr, n)

                                start = time.time()
                                mergeSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Merge Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
            #This is the quick sort case
            case 3:
                scenario = int(input("Case Scenarios for Quick Sort\n---------------\n1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit quick sort test\nSelect the case (1-4): "))
                
                match scenario:
                    #This follows the same pattern where it is the best case for quick sort
                    case 1:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillBestCase(arr, n)
                            
                            start = time.time()
                            quicksort(arr, 0, n-1)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillBestCase(arr, n)

                                start = time.time()
                                quicksort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the average case for quick sort
                    case 2:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillAverageCase(arr, n)

                            start = time.time()
                            quicksort(arr, 0, n-1)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10
                    
                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillAverageCase(arr, n)

                                start = time.time()
                                quicksort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the worst case for quick sort
                    case 3:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillWorstCase(arr, n)

                            start = time.time()
                            quicksort(arr, 0, n-1)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillWorstCase(arr, n)

                                start = time.time()
                                quicksort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Quick Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
            #This is the case for Radix sort
            case 4:
                scenario = int(input("Case Scenarios for Radix Sort\n---------------\n1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit radix sort test\nSelect the case (1-4): "))
                
                match scenario:
                    #This follows the same pattern where it is the best case for Radix Sort
                    case 1:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillBestCase(arr, n)
                            
                            start = time.time()
                            radixSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillBestCase(arr, n)

                                start = time.time()
                                radixsort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the average case for Radix Sort
                    case 2:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillAverageCase(arr, n)

                            start = time.time()
                            radixSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillAverageCase(arr, n)

                                start = time.time()
                                radixSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break
                    #This follows the same pattern where it is the worst case for Radix Sort
                    case 3:
                        n = 100
                        for _ in range(3):
                            arr = [0] * n
                            fillWorstCase(arr, n)

                            start = time.time()
                            radixSort(arr)
                            end = time.time()
                            print("For N = ", n, ", it takes ", end-start, " seconds")
                            completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            n*=10

                        while 1 == 1:
                            if input("Do you want to input another N (Y/N)? ") == "Y":
                                n = int(input("What is the N? "))
                                arr = [0] * n
                                fillWorstCase(arr, n)

                                start = time.time()
                                radixSort(arr)
                                end = time.time()
                                print("For N = ", n, ", it takes ", end-start, " seconds")
                                completeString += ("Radix Sort - N = " + str(n) + ", T = " + str(end-start) + "\n")
                            else:
                                break


    #Write the results to the file
    file.writelines(completeString)
    file.close()
    
    #Show closing statement
    print("Bye!")
