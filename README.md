# 🐍 NumPy Learning Journey 🚀

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/NumPy-1.26-orange?style=for-the-badge&logo=numpy" />
  <img src="https://img.shields.io/badge/Progress-8%20Days-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Data%20Science-informational?style=for-the-badge" />
</p>

---

## 📌 About This Repository

Welcome to my **NumPy Learning Journey**!  
This repository documents my **daily progress** while learning NumPy — a powerful Python library for numerical computing and data manipulation.

Each day includes:

* 📘 Concepts learned
* 💻 Code implementations
* 💡 Practical insights

---

## 📖 Table of Contents

* 📅 [Day 1: Getting Started with NumPy Arrays](#-day-1-getting-started-with-numpy-arrays)
* 📅 [Day 2: Array Properties and Aggregation Functions](#-day-2-array-properties-and-aggregation-functions)
* 📅 [Day 3: Indexing, Fancy Indexing, and Filtering](#-day-3-indexing-fancy-indexing-and-filtering-in-numpy)
* 📅 [Day 4: Array Reshaping and Manipulation](#-day-4-array-reshaping-and-manipulation)
* 📅 [Day 5: Advanced Array Operations](#-day-5-advanced-array-operations)
* 📅 [Day 6: NumPy Broadcasting](#-day-6-numpy-broadcasting)
* 📅 [Day 7: Vectorization in NumPy](#-day-7-vectorization-in-numpy)
* 📅 [Day 8: Handling Missing Values in NumPy](#-day-8-handling-missing-values-in-numpy)
* 📌 [Conclusion](#-conclusion)

---

## 📅 Day 1: Getting Started with NumPy Arrays

🎯 **Goal:** Learn how to create arrays and perform basic operations.

### 📘 Functions Learned:

* np.array() → Convert Python lists into NumPy arrays
* np.zeros() → Create arrays filled with zeros
* np.ones() → Create arrays filled with ones
* np.full() → Create arrays with a specific value
* np.eye() → Generate identity matrix
* np.arange() → Generate sequences
* np.mean() → Calculate average

📂 **Code:** [Day 1 Code](./Day1_code/)

---

## 📅 Day 2: Array Properties and Aggregation Functions

🎯 **Goal:** Understand array structure and perform mathematical operations.

### 📘 Array Properties:

* arr.dtype → Data type
* arr.astype() → Convert data type
* arr.shape → Dimensions
* arr.size → Total elements
* arr.ndim → Number of dimensions

### 📊 Aggregation Functions:

* np.sum() → Sum
* np.mean() → Average
* np.min() → Minimum
* np.max() → Maximum
* np.std() → Standard deviation
* np.var() → Variance

📂 **Code:** [Day 2 Code](./Day2_code/)

---

## 📅 Day 3: Indexing, Fancy Indexing, and Filtering in NumPy

🎯 **Goal:** Access and filter data efficiently.

### 🔍 Indexing:

* arr[row, col] → Access element
* 3D indexing → arr[layer, row, col]

### ✨ Fancy Indexing:

* Select multiple elements
* Works in 1D & 2D arrays

### 🎯 Filtering:

* arr[arr > 5]
* arr[arr % 2 == 0]
* Multiple conditions using &

### 💡 Tips:

* Slicing: arr[start:end:step]
* Fancy indexing returns **copy**
* Filtering returns **flattened array**

📂 **Code:** [Day 3 Code](./Day3_code/)

---

## 📅 Day 4: Array Reshaping and Manipulation

🎯 **Goal:** Modify array shapes and structures.

### 📘 Functions Learned:

* arr.reshape() → Change shape
* arr.flatten() → Convert to 1D
* arr.ravel() → Flatten (view if possible)
* arr.T → Transpose
* np.resize() → Resize array

### 🔄 Concepts Practiced:

* 1D → 2D conversion
* 2D → 1D flattening
* Multi-shape transformations
* Preparing data for ML

📂 **Code:** [Day 4 Code](./Day4_code/)

---

## 📅 Day 5: Advanced Array Operations

🎯 **Goal:** Perform complex array manipulations.

### 📘 Functions Learned:

* np.append() → Add elements
* np.concatenate() → Join arrays
* np.delete() → Remove elements
* np.insert() → Insert elements
* np.vstack() → Vertical stack
* np.hstack() → Horizontal stack
* np.split() → Split arrays

### ⚙️ Concepts Practiced:

* 1D & 2D operations
* Row & column concatenation
* Data insertion & deletion
* Splitting datasets

📂 **Code:** [Day 5 Code](./Day5_code/)

---

## 📅 Day 6: NumPy Broadcasting

🎯 **Goal:** Understand broadcasting and perform operations on arrays with different shapes.

### 📘 Concepts Learned:

* Broadcasting allows NumPy to perform operations on arrays of different shapes
* Arrays can operate together if their shapes are compatible
* If dimensions match → operations work directly
* If one dimension is 1 → NumPy stretches the array
* If dimensions do not match and none is 1 → broadcasting error occurs
* Broadcasting improves performance by avoiding unnecessary data copying

### ⚙️ Concepts Practiced:

* Broadcasting rules
* Shape compatibility
* Operations on different sized arrays
* Understanding dimension alignment
* Error when shapes are incompatible

📂 **Code:** [Day 6 Code](./Day6_code/)

---

## 📅 Day 7: Vectorization in NumPy

🎯 **Goal:** Learn how to perform operations on entire arrays efficiently without using traditional loops.

### 📘 Concepts Learned:

* Vectorization allows operations to be applied to complete arrays at once
* NumPy performs element-wise operations automatically
* Mathematical operations can be executed directly on arrays
* Vectorized code is shorter, cleaner, and easier to read
* Vectorization improves performance compared to manual looping
* It is one of the key reasons NumPy is widely used in data processing

### ⚙️ Concepts Practiced:

* Element-wise addition
* Element-wise subtraction
* Element-wise multiplication
* Element-wise division
* Power operations on arrays
* Modulus operations
* Comparison operations
* Applying scalar values to entire arrays
* Working with vectorized arithmetic expressions
* Understanding the difference between loops and vectorized operations

📂 **Code:** [Day 7 Code](./vectorization/)

---

## 📅 Day 8: Handling Missing Values in NumPy

🎯 **Goal:** Learn how to detect and handle missing, invalid, and infinite values in NumPy arrays.

### 📘 Functions Learned:

* np.isnan() → Detect missing values (NaN)
* np.isinf() → Detect positive and negative infinite values
* np.nan_to_num() → Replace NaN and infinite values with numerical values

### ⚙️ Concepts Practiced:

* Identifying missing values in arrays
* Detecting infinite values
* Handling invalid numerical entries
* Cleaning arrays for preprocessing
* Replacing NaN with valid numbers
* Replacing positive and negative infinity
* Preparing cleaner data for analysis and machine learning workflows

📂 **Code:** [Day 8 Code](./Handling_miss_values/)

---

## 📊 Progress Tracker

Day 1 ██████████ 100%  
Day 2 ██████████ 100%  
Day 3 ██████████ 100%  
Day 4 ██████████ 100%  
Day 5 ██████████ 100%  
Day 6 ██████████ 100%  
Day 7 ██████████ 100%  
Day 8 ██████████ 100%  

---

## 📌 Conclusion

By completing these 8 days, I have built a strong foundation in:

✔️ Array creation & properties  
✔️ Mathematical operations  
✔️ Indexing & filtering  
✔️ Reshaping & transformation  
✔️ Advanced array manipulation  
✔️ Broadcasting and array compatibility  
✔️ Vectorized operations for efficient computation  
✔️ Handling missing and invalid numerical values  

This journey prepares me for:

* 📊 Data Analysis
* 🤖 Machine Learning
* 📈 Data Science Projects
* ⚡ High-performance numerical computing

---

## ⭐ Future Goals

* Explore **Linear Algebra operations**
* Work with **real datasets**
* Integrate NumPy with **Pandas & ML models**
* Learn **NumPy optimization techniques**
* Practice **advanced vectorized operations**
* Move towards **Data Science & Machine Learning**

---

## 🤝 Connect With Me

If you like this project, feel free to ⭐ the repository and follow my journey!

---
