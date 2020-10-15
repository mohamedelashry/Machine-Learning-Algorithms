import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'C:\\Users\\decim\\Desktop\\review with practice on machine learning algorithms\\Classification\\code\\python from scratch\\data.txt'

data = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
# print('data = ')
# print(data.head(10) )
# print()
# print('data.describe = ')
# print(data.describe())

# seperate positive and negative data 
positive = data[data['Admitted'].isin([1])]
negative = data[data['Admitted'].isin([0])]   
# print(positive)
# print(negative)

# plot positive and negative points as ascatter 
fig, ax = plt.subplots(figsize=(12,10))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')

#define h(X) 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
#set interval to plot sigmoid 
nums = np.arange(-10, 10, step=1)
#plot sigmoid 
fig, ax = plt.subplots(figsize=(12,10))
ax.plot(nums, sigmoid(nums), 'r')
#dfine cost function 
def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

# add a ones column X0
#- this makes the matrix multiplication work out easier
data.insert(0, 'Ones', 1)
# print(data)

# set X (input data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]

# convert to numpy arrays and initalize the parameter array theta
X = np.array(X.values)
y = np.array(y.values)
theta = np.zeros(3)

# print()
# print('X.shape = ' , X.shape)
# print('theta.shape = ' , theta.shape)
# print('y.shape = ' , y.shape)

thiscost = cost(theta, X, y)
print("@#@##@#@#@#@#@#@#@")
print('cost = ' , thiscost)

#ddfine the gradiant 
#how to get the best(lowest) cost 
def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)
    
    error = sigmoid(X * theta.T) - y
    # print("error = ", error)
    for i in range(parameters):
        term = np.multiply(error, X[:,i])
        grad[i] = np.sum(term) / len(X)
    print(":::::::::::::::::::::::::::")
    print(grad)
    return grad

#repeat to get minimum cost 
import scipy.optimize as opt
result = opt.fmin_tnc(func=cost,
                      x0=theta,
                      fprime=gradient,args=(X, y))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(result)
#show for best cost with suitable theta
costafteroptimize = cost(result[0], X, y)
print('cost after optimize = ' , costafteroptimize)


def predict(theta, X):
    probability = sigmoid(X * theta.T)
    print(probability.shape)
    return [1 if x >= 0.5 else 0 for x in probability]

theta_min = np.matrix(result[0])
predictions = predict(theta_min, X)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
accuracy = (sum(map(int, correct)) % len(correct))
print ('accuracy = {0}%'.format(accuracy))
