def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)