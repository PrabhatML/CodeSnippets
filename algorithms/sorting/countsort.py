def count_sort_number(arr):
	mx = max(arr)
	mn = min(arr)

	count = {}
	out = []
	for i in range(mn,mx+1):
		if i in arr:
			count[i] = arr.count(i)
		else:
			count[i] = 0

	for i in count.keys():
		out.extend([i]*count[i])
	print(out)

def count_sort_word(arr):
	word = {}
	for i in arr:
		if i not in word:
			word[ord(i)] = arr.count(i)
	print(word)
	mx = max(word.keys())
	mn = min(word.keys())

	count = {}
	
	for i in range(mn,mx+1):
		if i in word.keys():
			count[i] = 1
	print(count)

	out = []
	
	for i in count.keys():
		out.extend([chr(i)]*word[i])
	print(out)

arr  = "geeksforgeeks"
count_sort_word(arr)