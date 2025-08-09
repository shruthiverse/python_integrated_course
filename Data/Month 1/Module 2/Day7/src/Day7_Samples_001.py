
---

### Code Sample for Day 7
Below is a single Python file (`Day7_Samples_001.py`) with five sample programs tailored to Module 7: Working with Libraries (Days 31-35), focusing on Day 7's topics of PyTorch and machine learning libraries like scikit-learn.

```python
# Day7_Samples_001.py
# Program 1: Creating a Tensor in PyTorch
import torch
x = torch.tensor([1, 2, 3])
print("Tensor:", x)

# Program 2: Basic Tensor Operation
y = torch.tensor([4, 5, 6])
z = x + y
print("Addition of tensors:", z)

# Program 3: Converting Tensor to NumPy
numpy_array = x.numpy()
print("Tensor as NumPy array:", numpy_array)

# Program 4: Simple Linear Regression with scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# Program 5: Predicting with the Model
prediction = model.predict(np.array([[5]]))
print("Prediction for X=5:", prediction[0])