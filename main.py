import sys
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

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

    yesorno = input("\nDo you want to sort the numbers? (Y/N): ")
    if yesorno == 'Y':
        bubble_sort(numbers)
    else:
        sys.exit("Exiting the program.")
        

def bubble_sort(list):
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

    for i in list:
        print(i, end =' ')

    print("total passes: ", passnum)
    print("total swaps: ", swapnum)

    plt.clf()
    plt.bar(range(len(list)), list, color='blue')
    plt.show()

if __name__ == "__main__":
    main()