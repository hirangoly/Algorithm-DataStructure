def swap_item(item1, item2, unsorted_list):
	store_extra = unsorted_list[item1]
	unsorted_list[item1] = unsorted_list[item2]
	unsorted_list[item2] = store_extra

# starts with 1th index and compare with each i-1th item, swap if ith is small
# NOTE: traverse backward, keep swaping with small item
def insertion_sort(unsorted_list):	
	for i in range(1, len(unsorted_list)):
		j = i
		while j>0 and unsorted_list[j] < unsorted_list[j-1]:
			swap_item(j, j-1, unsorted_list)
			j -= 1
	return unsorted_list

# find out smallest number and swap with ith item
# by comparing ith item with i+1th item, if i+1th is less than ith then move pinter to i+1th
# keep comparing till last item and then swap with ith element
# NOTE: traverse forward, swap when you find smallest item
def selection_sort(unsorted_list):
	for i in range(len(unsorted_list)):
		min = i
		for j in range(i+1, len(unsorted_list)):
			if unsorted_list[j] < unsorted_list[min]:
				min = j
		swap_item(i, min, unsorted_list)
	return unsorted_list
	
	
unsort_insertion_list = [53,61,8,10,23]
unsort_selection_list = [6,99,89,3,3]
unsort_list3 = ['hello','there','I am here','how are you','I will be there']

# Insertion Sort
print('unsort list')
print(unsort_insertion_list)
print('sorting by insertion sort')
sort_insertion_list = insertion_sort(unsort_insertion_list)
print('sort list')
print(sort_insertion_list)

# Selection Sort
print('unsort list')
print(unsort_selection_list)
print('sorting by selection sort')
sort_selection_list = selection_sort(unsort_selection_list)
print('sort list')
print(sort_selection_list)