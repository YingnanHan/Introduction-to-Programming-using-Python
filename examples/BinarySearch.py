# Use binary search to find the key in the list
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
      
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
      
    return -1 # Now high < low, key not found


lst=[1,2,3,4]
result=binarySearch(lst,1)
print(result)