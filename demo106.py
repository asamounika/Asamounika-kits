import numpy as np

a = np.array([10, 15, 20, 25, 30, 35, 40])

print("Original array:", a)

print("Array:", a + 10)
print("Array " \
":", a * 2)

print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))
print("Median:", np.median(a))
print("75th Percentile:", np.percentile(a, 75))