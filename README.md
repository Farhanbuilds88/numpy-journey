🐍 NumPy Learning Journey 🚀
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/NumPy-1.26-orange?style=for-the-badge&logo=numpy" /> <img src="https://img.shields.io/badge/Progress-6%20Days-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Focus-Data%20Science-informational?style=for-the-badge" /> </p>
📌 About This Repository

Welcome to my NumPy Learning Journey!
This repository documents my daily progress while learning NumPy — a powerful Python library for numerical computing and data manipulation.

Each day includes:

📘 Concepts learned
💻 Code implementations
💡 Practical insights
📖 Table of Contents
📅 Day 1: Getting Started with NumPy Arrays
📅 Day 2: Array Properties and Aggregation Functions
📅 Day 3: Indexing, Fancy Indexing, and Filtering
📅 Day 4: Array Reshaping and Manipulation
📅 Day 5: Advanced Array Operations
📅 Day 6: Broadcasting in NumPy
📌 Conclusion
📅 Day 1: Getting Started with NumPy Arrays

🎯 Goal: Learn how to create arrays and perform basic operations.

📘 Functions Learned:
np.array() → Convert Python lists into NumPy arrays
np.zeros() → Create arrays filled with zeros
np.ones() → Create arrays filled with ones
np.full() → Create arrays with a specific value
np.eye() → Generate identity matrix
np.arange() → Generate sequences
np.mean() → Calculate average

📂 Code: Day 1 Code

📅 Day 2: Array Properties and Aggregation Functions

🎯 Goal: Understand array structure and perform mathematical operations.

📘 Array Properties:
arr.dtype → Data type
arr.astype() → Convert data type
arr.shape → Dimensions
arr.size → Total elements
arr.ndim → Number of dimensions
📊 Aggregation Functions:
np.sum() → Sum
np.mean() → Average
np.min() → Minimum
np.max() → Maximum
np.std() → Standard deviation
np.var() → Variance

📂 Code: Day 2 Code

📅 Day 3: Indexing, Fancy Indexing, and Filtering in NumPy

🎯 Goal: Access and filter data efficiently.

🔍 Indexing:
arr[row, col] → Access element
3D indexing → arr[layer, row, col]
✨ Fancy Indexing:
Select multiple elements
Works in 1D & 2D arrays
🎯 Filtering:
arr[arr > 5]
arr[arr % 2 == 0]
Multiple conditions using &
💡 Tips:
Slicing: arr[start:end:step]
Fancy indexing returns copy
Filtering returns flattened array

📂 Code: Day 3 Code

📅 Day 4: Array Reshaping and Manipulation

🎯 Goal: Modify array shapes and structures.

📘 Functions Learned:
arr.reshape() → Change shape
arr.flatten() → Convert to 1D
arr.ravel() → Flatten (view if possible)
arr.T → Transpose
np.resize() → Resize array
🔄 Concepts Practiced:
1D → 2D conversion
2D → 1D flattening
Multi-shape transformations
Preparing data for ML

📂 Code: Day 4 Code

📅 Day 5: Advanced Array Operations

🎯 Goal: Perform complex array manipulations.

📘 Functions Learned:
np.append() → Add elements
np.concatenate() → Join arrays
np.delete() → Remove elements
np.insert() → Insert elements
np.vstack() → Vertical stack
np.hstack() → Horizontal stack
np.split() → Split arrays
⚙️ Concepts Practiced:
1D & 2D operations
Row & column concatenation
Data insertion & deletion
Splitting datasets

📂 Code: Day 5 Code

📅 Day 6: Broadcasting in NumPy

🎯 Goal: Learn how to perform operations between arrays of different shapes and understand rules for compatibility.

📘 Concepts Learned:
Rules of broadcasting: Two dimensions are compatible if they are equal or one of them is 1
Shape alignment is checked from the last dimension backward
Broadcasting allows operations with scalars, row vectors, column vectors, and matrices
Operations fail if shapes are incompatible, raising ValueError
Key takeaway: Check array shapes before operations
Practical work:
Created a Broadcasting folder to organize examples
Added files: single.py, 1d_to_2d.py, error.py
Practiced row-wise, column-wise, and scalar broadcasting
Explored common errors with mismatched shapes

📂 Code: Broadcasting Folder

📊 Progress Tracker
Day 1  ██████████ 100%
Day 2  ██████████ 100%
Day 3  ██████████ 100%
Day 4  ██████████ 100%
Day 5  ██████████ 100%
Day 6  ██████████ 100%
📌 Conclusion

By completing these 6 days, I have built a strong foundation in:

✔️ Array creation & properties
✔️ Mathematical operations
✔️ Indexing & filtering
✔️ Reshaping & transformation
✔️ Advanced array manipulation
✔️ Broadcasting and handling shape errors

This journey prepares me for:

📊 Data Analysis
🤖 Machine Learning
📈 Data Science Projects
⭐ Future Goals
Explore Linear Algebra operations
Work with real datasets
Integrate NumPy with Pandas & ML models
🤝 Connect With Me

If you like this project, feel free to ⭐ the repository and follow my journey!

This is now professional, concise, and portfolio-ready. ✅
