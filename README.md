# 🐍 NumPy Journey

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  
[![NumPy](https://img.shields.io/badge/NumPy-1.26-orange)](https://numpy.org/)  

Welcome to my NumPy journey! This repository contains my daily learning notes and code examples while exploring NumPy in Python. Each day includes concepts learned, code examples, and tips for easier understanding.

---

## 📖 Table of Contents

1. [Day 1: Getting Started with NumPy Arrays](#📅-day-1-getting-started-with-numpy-arrays)  
2. [Day 2: Array Properties and Aggregation Functions](#📅-day-2-array-properties-and-aggregation-functions)  
3. [Day 3: Indexing, Fancy Indexing, and Filtering in NumPy](#📅-day-3-indexing-fancy-indexing-and-filtering-in-numpy)  
4. [Conclusion](#📌-conclusion)  

---

## 📅 Day 1: Getting Started with NumPy Arrays

Today, I focused on understanding how to **create arrays** in NumPy and perform **basic operations**.

### Functions Learned:
- `np.array()` – Convert Python lists to NumPy arrays  
- `np.zeros()` – Create arrays filled with zeros  
- `np.ones()` – Create arrays filled with ones  
- `np.full()` – Create arrays filled with a specific value  
- `np.eye()` – Create identity matrices  
- `np.arange()` – Create sequences of numbers  
- `np.mean()` – Calculate the average  

[See Day 1 Code](./Day1_code/)  

---

## 📅 Day 2: Array Properties and Aggregation Functions

Today, I explored **array properties** and **aggregation functions** to better understand NumPy arrays and perform numerical analysis.

### Array Properties:
- `arr.dtype` – Check the **data type** of array elements  
- `arr.astype()` – Convert array to a different **data type**  
- `arr.shape` – Get the **dimensions** of the array  
- `arr.size` – Get the **total number of elements**  
- `arr.ndim` – Get the **number of dimensions**  

### Aggregation / Math Functions:
- `np.sum(arr)` – Sum of all elements  
- `np.mean(arr)` – Average of elements  
- `np.min(arr)` – Minimum value  
- `np.max(arr)` – Maximum value  
- `np.std(arr)` – Standard deviation  
- `np.var(arr)` – Variance  

[See Day 2 Code](./Day2_code/)  

---

## 📅 Day 3: Indexing, Fancy Indexing, and Filtering in NumPy

Today, I explored **how to access elements** in 2D and 3D arrays, used **fancy indexing** to select multiple elements, and applied **filtering** to extract data based on conditions.

### Indexing:

#### 2D Arrays:
- `arr_2d[row, column]` – Access a specific element  
- Example: `arr_2d[0, 2]` → Access **3** from first row, third column  

#### 3D Arrays:
- `arr_3d[layer, row, column]` – Access element in a 3D array  
- Example: `arr_3d[1, 0, 2]` → Access element from 2nd layer, 1st row, 3rd column  

---

### Fancy Indexing:
- `arr[[index1, index2, ...]]` – Select multiple elements at once  
- Works in 1D and 2D arrays  
- Example 1D: `arr[[0, 2, 4]]` → Select elements at positions 0, 2, and 4  
- Example 2D: `arr_2d[[0, 2], [1, 2]]` → Select elements `(0,1)` and `(2,2)`  

---

### Filtering / Boolean Indexing:
- `arr[condition]` – Select elements based on a **condition**  
- Examples:
  - `arr[arr > 5]` → Elements greater than 5  
  - `arr[arr % 2 == 0]` → Select even numbers  
  - `arr[(arr > 5) & (arr < 10)]` → Multiple conditions  
- **3D arrays** work the same way:  
  - `arr_3d[arr_3d > 5]` → Returns elements greater than 5 (flattened)

---

### 💡 Tips & Tricks:
- Slicing: `arr[start:end:step]` works with 1D, 2D, and 3D arrays  
- Fancy indexing returns a **copy**, not a view  
- Filtering always returns a **1D array** unless using `np.where()` to keep shape  

[See Day 3 Code](./Day3_code/)  

---

## 📌 Conclusion

Over these three days, I built a strong foundation in **NumPy**, including:
- Creating arrays and understanding their **properties**  
- Performing **aggregation and mathematical operations**  
- Accessing and manipulating data with **indexing, fancy indexing, and filtering**  

This structured approach makes it easier to perform **numerical computations**, **data analysis**, and lays the groundwork for **machine learning projects**.  

---
