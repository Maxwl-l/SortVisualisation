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
        merge_sort(numbers)
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


def draw(arr, k, lo, hi):
    colors = ['blue'] * len(arr)
    for x in range(lo, hi):
        colors[x] = 'orange'   # the section currently being merged
    colors[k] = 'red'          # the position just written
    plt.clf()
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.1)


def merge_sort(arr):
    start = time.perf_counter()
    stats = {"merges": 0, "writes": 0}

    merge_sort_range(arr, 0, len(arr), stats)

    elapsed = time.perf_counter() - start
    for i in arr:
        print(i, end=' ')

    print("\nElapsed time: ", elapsed, "seconds")
    print("total merges: ", stats["merges"])
    print("total writes: ", stats["writes"])

    plt.clf()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.show()


def merge_sort_range(arr, lo, hi, stats):
    # sorts arr[lo:hi] in place
    if hi - lo <= 1:
        return

    mid = (lo + hi) // 2
    merge_sort_range(arr, lo, mid, stats)
    merge_sort_range(arr, mid, hi, stats)
    merge(arr, lo, mid, hi, stats)


def merge(arr, lo, mid, hi, stats):
    left = arr[lo:mid]
    right = arr[mid:hi]
    i = j = 0
    k = lo

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        stats["writes"] += 1
        draw(arr, k, lo, hi)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        stats["writes"] += 1
        draw(arr, k, lo, hi)
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        stats["writes"] += 1
        draw(arr, k, lo, hi)
        k += 1

    stats["merges"] += 1
    print("--------One merge completed.--------")

    # def merge_sort(list):
    #     start = time.perf_counter()
    #     n = len(list)
    #     if n <= 1:
    #         return

    #     leftlist = merge_sort(list[:n//2])
    #     rightlist = merge_sort(list[n//2:])

    #     return merge(leftlist, rightlist)


    # def merge(lista, listb):
    #     listc = []

    #     while len(lista) > 0 and len(listb) > 0:
    #         if(lista[0] > listb[0]):
    #             listc.append(listb.pop(0))
    #         else:
    #             listc.append(lista.pop(0))

    #     while len(lista) > 0:
    #         listc.append(lista.pop(0))

    #     while len(listb) > 0:
    #         listc.append(listb.pop(0))

    #     return listc

    
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