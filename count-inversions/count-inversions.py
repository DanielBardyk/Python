import os

dir_path = os.path.dirname(__file__)

# changing of array arr_i relatively to arr_x
def reverse(arr_x, arr_i):

	n = len(arr_i)
	res = [0]*n

	for i in range(n):
		res_idx = arr_x[i]
		res[res_idx - 1] = arr_i[i]

	for i in range(n):
		arr_i[i] = res[i]

# merging and calculation of splitted inversions
def merge_and_count_split_inv(arr, left, mid, right):
	n1 = mid - left + 1
	n2 = right - mid

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[left + i]

	for j in range(0, n2):
		R[j] = arr[mid + 1 + j]

	i = 0
	j = 0
	k = left

	inv_count = 0

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			inv_count += (n1 - i)
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
		
	return inv_count

# calculation of inversions in the array
def merge_sort_count_inv(arr, left, right):
	inv_count = 0

	if left < right:
		mid = left+(right-left)//2

		inv_count += merge_sort_count_inv(arr, left, mid)
		inv_count += merge_sort_count_inv(arr, mid + 1, right)
		inv_count += merge_and_count_split_inv(arr, left, mid, right)

	return inv_count

""" creating a 2D array with rows of type: 
[<user number>, <inversions>] """

def users_and_inv(film_ranges):
	res_arr = []
	for count, row in enumerate(film_ranges):
		if count != X-1:
			reverse(D[X-1], row)
			n = len(row)
			res_arr.append([count+1, merge_sort_count_inv(row, 0, n-1)])

	return res_arr

""" merging subarrays of a 2D array with strings
of type [<user number>, <inversions>] """

def merge(arr, left, mid, right):
	n1 = mid - left + 1
	n2 = right - mid

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[left+i]

	for j in range(0, n2):
		R[j] = arr[mid+1+j]

	i = 0
	j = 0
	k = left

	while i < n1 and j < n2:
		if L[i][1] <= R[j][1]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

""" sorting of 2D array with rows of type:  
[<user number>, <inversions>]
by the second element of the rows """

def merge_sort(arr, left, right):
	if left < right:

		mid = left+(right-left)//2

		merge_sort(arr, left, mid)
		merge_sort(arr, mid+1, right)
		merge(arr, left, mid, right)

""" the calculation of the sorted array that will be recorded
to the file with rows like: [<user number>, <inversions>] """
def sort_favourites_list(fav_list):
	n = len(fav_list)
	merge_sort(fav_list, 0, n - 1)


# start
filename = input("Enter the filename: ")

D = []

# file reading
with open(f'{dir_path}/{filename}', 'r') as f:
	f_row = f.readline().strip().split(' ')
	U = int(f_row[0])
	M = int(f_row[1])
	for line in f:
		number = [int(item.strip()) for item in line.split(' ')[1:]]
		D.append(number)

X = int(input("Enter the user number for comparison: "))

# getting the array of rows like: [<user number>, <inversions>]
favourites_list = users_and_inv(D)

# sorting favourites_list by the second element of the rows
sort_favourites_list(favourites_list)

# writing the results to the file
with open(f'{dir_path}/{os.path.basename(__file__).split(".")[0]}_output', 'w') as f:
	f.write(f"{X}\n")
	for line in favourites_list:
		f.write(f"{line[0]} {line[1]}\n")
