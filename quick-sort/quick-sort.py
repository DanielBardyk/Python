import os
import numpy as np
import random
from mat import mat
import sys
sys.setrecursionlimit(5000)


dir_path = os.path.dirname(__file__)

# ---- Realization of simple quick sort ----

def partition(arr, left, right, count):
	pivot = arr[right]
	i = left - 1

	for j in range(left, right):
		count += 1
		if arr[j] >= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[right] = arr[right], arr[i + 1]

	return i + 1, count

def quick_sort(arr, left, right, count):
	if left < right:
		partition_pos, count = partition(arr, left, right, count)
		count = quick_sort(arr, left, partition_pos - 1, count)
		count = quick_sort(arr, partition_pos + 1, right, count)

	return count

# ---- Realization of quick sort with the 3d median ----

def medianOfThree(a, b, c):
	if((b < a and a < c) or (c < a and a < b)):
		return a
	elif((a < b and b < c) or (c < b and b < a)):
		return b
	else:
		return c

def partition_median(arr, left, right, count):
	pl, pm, pr = arr[left], arr[((left+right)//2)], arr[right]

	pivot = medianOfThree(pl, pm, pr)

	if pivot == pl:
		arr[left], arr[right] = arr[right], arr[left]
	elif pivot == pm:
		arr[((left+right)//2)], arr[right] = arr[right], arr[((left+right)//2)]

	i = left - 1

	for j in range(left, right):
		count += 1
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[right] = arr[right], arr[i + 1]

	return i + 1, count

def insertion_sort(array, left, right, comparisons):
	for i in range(left+1, right+1):
		key = array[i]
		j = i-1
		while j >= left:
			comparisons += 1
			if array[j] > key:
				array[j+1] = array[j]
				j -= 1
				continue
			break
			
		array[j+1] = key
	return comparisons

def quick_sort_median(arr, left, right, count):
	if left < right:
		if (right - left + 1) > 3:
			partition_pos, count = partition_median(arr, left, right, count)
			count = quick_sort_median(arr, left, partition_pos - 1, count)
			count = quick_sort_median(arr, partition_pos + 1, right, count)
		else: 
			count = insertion_sort(arr, left, right, count)

	return count

# ---- Program execution ----
filename = input("Enter the filename: ")
arr = []

with open(f'{dir_path}/{filename}', 'r') as f:
	n = int(f.readline())
	for line in f:
		arr.append(int(line))
f.close()

arr2 = arr.copy()

comp1 = quick_sort(arr, 0, n - 1, 0)
comp2 = quick_sort_median(arr2, 0, n - 1, 0)

with open(f'{dir_path}/{os.path.basename(__file__).split(".")[0]}_output.txt', 'w') as f:
	f.write(f"{comp1} {comp2}\n")
f.close()

# ---- Plotting ----

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

sizes = [10, 100, 1000]
types = ["random", "best", "worst"]

data_plot = {'random':{'quick_sort':{}, 'quick_median':{}}, 'best':{'quick_sort':{}, 'quick_median':{}}, 'worst':{'quick_sort':{}, 'quick_median':{}}}

for size in sizes:
	print("\nDATA SIZE: ", size)
	for gen_type in types:
		print("\n\tDATA TYPE:", gen_type)

		data_simple = generate_data(size, gen_type)
		data_median = np.copy(data_simple)

		simple_count = quick_sort(data_simple, 0, size - 1, 0)
		print("\tSimple:", simple_count)
		data_plot[gen_type]['quick_sort'][size] = simple_count

		median_count = quick_sort_median(data_median, 0, size - 1, 0)
		print("\tMedian:", median_count)
		data_plot[gen_type]['quick_median'][size] = median_count

mat(data_plot)