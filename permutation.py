# permutation of input string 'abc' -> 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
def permutation(str):
	if len(str) == 1:
		return [str]

	if len(str) == 0:
		return []

	lst = []
	for i in range(len(str)):
		item = str[i]
		remaining = [x for x in str if x != item]
		combination = permutation(remaining)

		# print combination
		for combo in combination:
			lst.append([item] + combo)

	return lst
	
# sublist from list that sum makes target
def sum_permutation(str, target, partial=[]):
	# print partial
	sum_p = sum(partial)
	if sum_p == target:
		# new_lst1.append(partial)
		return partial
		
	if sum_p >= target:
		return

	for i in range(len(str)):
		item = str[i]
		remaining = str[i+1:]
		sum_permutation(remaining, target, partial + [item])

	return new_lst1

str = 'abc'
# str = [25, 10, 5, 1]
lst = permutation(str)
print lst

# new_lst1 = []
target = 4
lst1 = [1,2,3,4,5,6,7,8,9]
perm_lst = sum_permutation(lst1, target)
print perm_lst