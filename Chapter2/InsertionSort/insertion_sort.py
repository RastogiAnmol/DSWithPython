def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        element_to_be_placed = arr[i]
        place_holder = i
        while place_holder > 0 and arr[place_holder - 1] > element_to_be_placed:
            arr[place_holder] = arr[place_holder - 1]
            place_holder = place_holder - 1
        arr[place_holder] = element_to_be_placed
    print(f"after insertion sort----> {arr}")

arr = [3,5,1,7,4,9,2]
insertion_sort(arr)