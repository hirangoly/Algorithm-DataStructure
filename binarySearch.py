# binary search of sorted list
sort_list = [1,6,8,19,29,45]

def binary_search(slist, item):
	first = 0
	last = len(slist) - 1
	while 1:
		mid = (first + last) // 2
		if slist[mid] > item:
			# traverse left half
			last = mid - 1			
		elif slist[mid] < item:
			# traverse right half
			first = mid + 1
		else:
			return mid

print('binary search with sorted list')			
index = binary_search(sort_list, 1)
print(index)

def binary_search_recursive(slist, item):
	print(slist)
	print(len(slist))
	if len(slist) == 0:
		return 'blank list'
	elif len(slist) == 2:
		print('here')
		ls = slist
		return slist
	else:
		mid = len(slist) // 2
		if slist[mid] == item:
			return mid
		else:
			if slist[mid] > item:
				binary_search_recursive(slist[:mid-1], item)
			elif slist[mid] < item:
				binary_search_recursive(slist[mid+1:], item)
				
print('binary search using recursive')
index_rec = binary_search_recursive(sort_list, 29)
print(index_rec)