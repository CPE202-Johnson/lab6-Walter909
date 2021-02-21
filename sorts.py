import random
import time

def selection_sort(list):
    count = 0
    # Traverse through all list elements
    for i in range(len(list)):

        # Find the minimum element in remaining
        # unsorted list
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
            count +=1
        # Swap the found minimum element with
        # the first element
        list[i], list[min] = list[min], list[i]

    return count

def insertion_sort(list):
    count = 0

    #start at 1
    for i in range(1, len(list)):
        count+=1
        #if i is less than last element
        #terminate after comparing to first index
        while list[i] < list[i-1] and i > 0:
            #Swap
            list[i], list[i-1]  = list[i-1], list[i]
            i-=1
            #increment count
            count+=1
    return count

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

