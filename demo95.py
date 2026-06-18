arr=[10,40,30,20,50]
def insersion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print("Original array: ",arr)
print("Sorted array: ",insersion_sort(arr))