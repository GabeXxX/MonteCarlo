from scipy import random
import numpy as np
import matplotlib.pyplot as plt

#MONTE CARLO ESTIMATON FOR DEFINITE INTEGRAL

#Limit of integration
a = 0
b = np.pi

#Succession of random Variable
N = 1000 #number of random variable/point
xrand = random.uniform(a,b, N)

#Function to integrate
funcToPrint = "sin(x)"
def func(x):
    return np.sin(x)

#Evaluate the function on our random point
integral = 0.0

for i in range(N):
    integral += func(xrand[i])

#Get the result!
result = (b-a)/float(N)*integral
print("The definite integral of "+funcToPrint+" from "+str(a)+" to "+str(b)+" is:")
print(str(result))

#Ok, if we repeat over and over again, we never obtain the same result, but...
#...for N large, every area we calculate is sufficiently close to the real integral.
#That's  becouse, for the law of real number, the avarege of the succession (the result defined at line 27)
#converge to the definite integral we want to calculate.

#Now repeat the calculus of area many times and print the distribuition of our result

areas = []

for i in range(10000):

    xrand = random.uniform(a,b, N)

    integral = 0.0

    for i in range(N):
        integral += func(xrand[i])

    result = (b-a)/float(N)*integral
    areas.append(result)

plt.title("Distribuition of areas calculated:")
plt.hist(areas, bins=30, ec = 'black')
plt.xlabel("Areas")
plt.show()
