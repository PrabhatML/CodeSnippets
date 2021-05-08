from collections import Counter

def find_common(arr1,arr2):
    return set(arr1)&set(arr2)


Array1 = ["Article", "in", "Geeks", "for", "Geeks"]
Array2 = ["Geeks", "for", "Geeks"]

print(find_common(Array1,Array2))

def find_common_2(arr1,arr2):
    arr1 = Counter(arr1)
    arr2 = Counter(arr2)
    print(arr2,arr1)
    print(arr1 & arr2)
    return -1


Array1 = ["Article", "in", "Geeks", "for","for", "Geeks"]
Array2 = ["Geeks", "for", "Geeks"]

print(find_common(Array1,Array2))