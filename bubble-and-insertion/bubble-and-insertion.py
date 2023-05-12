import numpy as np
import random
from mat import mat


def bubble_sort(array):
    swaps = comparisons = 0
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            comparisons += 1
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swaps += 1
    return comparisons, swaps


def bubble_impr_sort(array):
    swaps = comparisons = 0
    for i in range(len(array)):
        swapped = False
        for j in range(len(array) - i - 1):
            comparisons += 1
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
                swaps += 1

        if not swapped:
            break
    return comparisons, swaps


def insertion_sort(array):
    swaps = comparisons = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j+1] = array[j]
            swaps += 1
            j -= 1

        comparisons += 1
        array[j+1] = key
    return comparisons, swaps


def generate_data(n, gen_type="random"):
    if gen_type == "best":
        a = [i+1 for i in range(n)]
        return a
    elif gen_type == "worst":
        a = [i+1 for i in reversed(range(n))]
        return a
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
        return a


def build_plots():
    sizes = [10, 100, 1000]
    types = ["random", "best", "worst"]

    data_plot = {'random': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
                 'best': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}},
                 'worst': {'bubble': {}, 'insertion': {}, 'bubble_impr': {}}}

    for n in sizes:
        print("\nDATA SIZE: ", n)
        for gen_type in types:
            print("\n\tDATA TYPE:", gen_type)
            data = generate_data(n, gen_type)
            data_bubble = np.copy(data)
            bubble_op_count = sum(bubble_sort(data_bubble))
            print("\tBubble sort operation count:", int(bubble_op_count))
            data_plot[gen_type]['bubble'][n] = bubble_op_count
            data_bubble_impr = np.copy(data)
            bubble_impr_op_count = sum(bubble_impr_sort(data_bubble_impr))
            print("\tImproved bubble sort operation count:",
                  int(bubble_impr_op_count))
            data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count
            data_insertion = np.copy(data)
            insertion_op_count = sum(insertion_sort(data_insertion))
            print("\tInsertion sort operation count:", int(insertion_op_count))
            data_plot[gen_type]['insertion'][n] = insertion_op_count
    return data_plot


def main():
    plot_data = build_plots()
    mat(plot_data)


if __name__ == '__main__':
    main()
