#merge_sort
arr=[12,33,56,85,98,23,64,25]
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i]); i+=1
        else:
            result.append(right[j]); j+=1
    result+=left[i:]
    result+=right[j:]
    return result
sorted_arr=merge_sort(arr)
print("merge_sort:",sorted_arr)