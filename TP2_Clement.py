

"""# mar 8 2022"""



file = open("testFile.txt", "a")
file.write("\n Rajout")

file = open("testFile.txt", "r")
content = file.read()
print(content)

"""**Python programming practice:**

let a be: a four component vector of all zeros (floats).
"""

import numpy as np
np.zeros((4))

"""let b be: a vector of 9 True values."""

np.ones((9), dtype=bool)

"""let c be: a 3 × 6 matrix of ones."""

import numpy as np

np.ones((3,6))

"""d ∈ Z 2×4×3 ."""

A = np.random.randint(0, 10, size=(2, 4, 3))
print("A:\n{} \n\n shape={}".format(
  A, A.shape))

"""let e be: an array of 151 floating point values evenly spaced in the interval [-10, 10]."""

np.linspace(-10, 10, 151)

"""let f and g each be: an array of 100 random numbers using np.random.randn()"""

f = np.random.randn(100)

g = np.random.randn(100)

"""• let h be: an array of 11 random numbers in the interval [0, 5] using np.random.randint()"""

np.random.randint(0,5,11)

"""Q2) i) Use np.mean() and np.std() to calculate the mean and standard deviation of the
random numbers of f and g. Are they they the same? Similar?
"""

np.mean(f)

np.std(g)

"""the two results are different

ii) Use np.corrcoef() to find the Pearson correlation between f and g. Is it large? What is
the format of the output?
"""

import numpy as np
np.corrcoef(g)

"""No it is short
it is a float

**Q3)** 
***i)*** Use a for loop to print out all the elements of f .
"""

for element in f:
  print(element)

"""**ii)** Use a for loop to print out only the positive elements of g"""

for element in g:
  if element > 0:
    print(element)

"""**Q4)** Use a for-loop to make a new array m such that m i = f i g i , for all i."""

m = []
for fElement in f:
  for gElement in g:
    m.append(fElement*gElement)
    break
len(m)

"""Use the same loop to calculate the msum, the dot product of f and g."""

msum = 0
for fElement in f:
  for gElement in g:
    msum += fElement*gElement
    break
msum

"""Use a for-loop to make an array n of length 17, such that n[i] is +1 for even i, and −1
for odd i
"""

n = []
for i in range(0,17):
  if i%2 == 0:
    n.append(-1)
  else:
    n.append(1)
n

"""**Q7**) Make a 50 × 50 array p of a diagonal matrix whose nonzero diagonal values are the
square root of the row index. Make the upper half triangle elements be the sum of their
indices
"""

# 4*np.zeros((50,50),float)+np.eye(50,50)
v = []
for i in range(0,50):
  v.append(i**2)
np.diag(v)