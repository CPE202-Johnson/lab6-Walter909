import random
import time

def selection_sort(list):
    count = 0
    # Traverse through all list elements
    for i in range(len(list)):

        # Find the minimum element in remaining
        # unsorted list
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
            count +=1
        # Swap the found minimum element with
        # the first element
        list[i], list[min_idx] = list[min_idx], list[i]

    return count

def insertion_sort(list):
    count = 0
    # Traverse through 1 to len(list)
    for i in range(1, len(list)):

        key = list[i]

        # Move elements of list[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < list[j] :
            list[j+1] = list[j]
            j -= 1
            count+=1
        list[j+1] = key

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

