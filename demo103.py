import numpy as np

Zero = np.array(10)
print(Zero)
print(type(Zero))
print("Dimension :", Zero.ndim)
print("Memory :", Zero.nbytes)

One = np.array([12, 24, 36, 48, 60])
print(One)
print(type(One))
print("Dimension :", One.ndim)
print("Memory :", One.nbytes)

Two = np.array([[1, 2, 3],
                [4, 5, 6]])

print(Two)
print(type(Two))
print("Dimension :", Two.ndim)
print("Memory :", Two.nbytes)