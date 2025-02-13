def shift_left(arr, k):
    k %= len(
        arr)  # Reduce k to avoid unnecessary shifts (k shifts in a full cycle return the array to its original state)

    for _ in range(k):  # Repeat the shifting process k times
        first = arr[0]  # Store the first element to move it to the end

        for index in range(len(arr) - 1):  # Shift all elements to the left
            arr[index] = arr[index + 1]  # Move each element one position to the left

        arr[-1] = first  # Place the first element at the last position

    return arr  # Return the modified array


def shift_right(arr, k):
    k %= len(arr)  # Reduce k to avoid unnecessary shifts

    for _ in range(k):  # Repeat the shifting process k times
        last = arr[-1]  # Store the last element to move it to the front

        for index in range(len(arr) - 1, 0, -1):  # Shift all elements to the right
            arr[index] = arr[index - 1]  # Move each element one position to the right

        arr[0] = last  # Place the last element at the first position

    return arr  # Return the modified array


array = [1, 2, 3, 4, 5]  # Define an example array

print(shift_left(array[:], 2))  # Output: [3, 4, 5, 1, 2] (Shift left by 2)
print(shift_right(array[:], 2))  # Output: [4, 5, 1, 2, 3] (Shift right by 2)
