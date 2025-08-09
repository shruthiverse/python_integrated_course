
---

### Code Sample for Day 10
Below is a single Python file (`Day10_Samples_001.py`) with five sample programs tailored to Module 10: Statistical Analysis (Days 46-50), focusing on Day 10's topics of statistical analysis with Python, creating models, and data interpretation. Note that R integration via `rpy2` is mentioned conceptually due to setup complexity.

```python
# Day10_Samples_001.py
# Program 1: Calculating Mean with scipy
from scipy import stats
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
mean_value = stats.tmean(data)
print("Mean of the data:", mean_value)

# Program 2: Calculating Variance
variance = stats.tvar(data)
print("Variance of the data:", variance)

# Program 3: Simple Linear Model with statsmodels
import statsmodels.api as sm
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
X = sm.add_constant(X)  # Add a constant term for the intercept
model = sm.OLS(y, X).fit()
print("Model Summary:")
print(model.summary())

# Program 4: Predicting with the Model
prediction = model.predict(sm.add_constant(np.array([6])))
print("Prediction for X=6:", prediction[0])

# Program 5: Visualizing Model Fit with Matplotlib
import matplotlib.pyplot as plt
plt.scatter(X[:, 1], y, color='blue', label='Data')
plt.plot(X[:, 1], model.predict(X), color='red', label='Fit')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Model Fit")
plt.legend()
plt.show()