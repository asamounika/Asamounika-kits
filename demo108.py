arr=[12,77,43,36,24,19]
def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
SelectionSort(arr)
print(arr)

def selection_sort(arr):
  n=len(arr)
  for i in range(n):
    min_index=i
    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
  return arr
print(selection_sort([1,5,6,2,7,8,9,10]))