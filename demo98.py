def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr = [14,3,27,9,41,7,35]
target=41
idx = Linear_Search(arr,target)
print(f"Found at index {idx}")