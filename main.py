import sys
from matplotlib import colors, pyplot as plt
import time

plt.style.use('seaborn-v0_8-darkgrid')

def main():
    numbers = []

    answer = None

    while answer != 'N':
        answer = input("Enter a number, press 'N' to stop: ")
        if answer == 'N':
            break
        else:
            try:
                numbers.append(int(answer))
            except ValueError:
                print("Invalid input. Please enter a number.")

    for i in numbers:
        print(i, end =' ') 

    plt.bar(range(len(numbers)), numbers, color='blue')
    plt.show(block=False)

    sort = input("\nSelect a sorting algorithm to use (Bubble Sort/Merge Sort/Insertion Sort): ")
    if sort == 'Bubble Sort':
        bubble_sort(numbers)
    elif sort == 'Merge Sort':
        #merge_sort(numbers)
        return
    elif sort == 'Insertion Sort':
        insertion_sort(numbers)
        return
    else:
        sys.exit("Invalid sorting algorithm selected.")
        

def insertion_sort(list):
    start = time.perf_counter()
    n = len(list)
    swapnum = 0
    for i in range(1, n):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            temp = list[j]
            list[j] = list[j - 1]
            list[j - 1] = temp
            print("--------One swap completed.--------")
            swapnum += 1
            j -= 1

            colors = ['blue'] * len(list)
            colors[j] = 'red'
            plt.clf()
            plt.bar(range(len(list)), list, color=colors)
            plt.pause(0.1)

    elapsed = time.perf_counter() - start
    for i in list:
        print(i, end =' ')

    print("\nElapsed time: ", elapsed, "seconds")
    print("total swaps: ", swapnum)

    plt.clf()
    plt.bar(range(len(list)), list, color='blue')
    plt.show()
    

def bubble_sort(list):
    start = time.perf_counter()
    n = len(list)
    sorted = False
    passnum = 0
    swapnum = 0
    while sorted == False:
        sorted = True
        for i in range(n-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swapnum += 1
                print("--------One swap completed.--------")
                sorted = False

                colors = ['blue'] * len(list)
                colors[i + 1] = 'red'
                plt.clf()
                plt.bar(range(len(list)), list, color=colors)
                plt.pause(0.1)

        print("--------One pass completed.--------")
        passnum += 1

    elapsed = time.perf_counter() - start
    for i in list:
        print(i, end =' ')

    print("\nElapsed time: ", elapsed, "seconds")
    print("total passes: ", passnum)
    print("total swaps: ", swapnum)

    plt.clf()
    plt.bar(range(len(list)), list, color='blue')
    plt.show()

if __name__ == "__main__":
    main()