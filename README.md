# 🚀 Cyclic Shift (Array Rotation) in Python

## 📌 Overview
This repository contains Python implementations of **cyclic shift (array rotation)** algorithms. It allows shifting elements of an array either **left** or **right** by a given number of positions.

## ✨ Features
✅ Shift an array **left** by `k` positions.  
✅ Shift an array **right** by `k` positions.  
✅ Efficient in-place modification of the array.  
✅ Works with lists of any size.  

## 🛠 How It Works
The functions shift elements step-by-step and place the overflowed elements at the opposite end of the list. The operations are performed **in-place**, modifying the original array.

---

## 🔹 Implementation

### 🔄 Shift Left
```python
def shift_left(arr, k):
    k %= len(arr)  # Optimize k to avoid redundant shifts
    for _ in range(k):
        first = arr[0]  # Store the first element
        for index in range(len(arr)-1):
            arr[index] = arr[index+1]  # Shift elements left
        arr[-1] = first  # Place the first element at the last position
    return arr
```

### 🔄 Shift Right
```python
def shift_right(arr, k):
    k %= len(arr)  # Optimize k to avoid redundant shifts
    for _ in range(k):
        last = arr[-1]  # Store the last element
        for index in range(len(arr)-1, 0, -1):
            arr[index] = arr[index-1]  # Shift elements right
        arr[0] = last  # Place the last element at the first position
    return arr
```

---

## 📝 Usage
You can use these functions by passing an array and a shift value:

```python
array = [1, 2, 3, 4, 5]

print(shift_left(array[:], 2))   # Output: [3, 4, 5, 1, 2]
print(shift_right(array[:], 2))  # Output: [4, 5, 1, 2, 3]
```

---

## ❓ Why `k %= len(arr)`?
This optimization ensures that unnecessary shifts are eliminated. For example, shifting an array of length `5` by `7` is the same as shifting it by `7 % 5 = 2`.

---

## 📜 License
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it. See the `LICENSE` file for more details.

