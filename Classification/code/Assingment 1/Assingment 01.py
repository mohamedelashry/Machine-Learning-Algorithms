import math
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LogisticRegression

def get_data(df):
    # load_svmlight_file loads dataset into sparse CSR matrix
    X,Y = load_svmlight_file(df)
    return X,Y

def split_data(n,train_size):
    tr_idx = np.random.choice(n, \
             int(np.round(n * train_size)),replace=False)
    te_idx = np.setdiff1d(np.arange(0,n), tr_idx)
    return tr_idx, te_idx


def standardize_para(X):
    Xmean = X.mean(axis=0)
    Xstd = X.std(axis=0)
    return {'X_mean' : Xmean, 'X_std': Xstd.T}


def standardize_X(X, stand_parms):
    return (X - stand_parms['X_mean']) / stand_parms['X_std']

# 1/ 1 + e^-score
def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))


def Hypothesis(theta, x):
	z = 0
	for i in range(len(theta)):
		z += x[i]*theta[i]
	return sigmoid(z)

def Cost_Function(X,Y,theta,m):
	sumOfErrors = 0
	for i in range(m):
		xi = X[i]
		hi = Hypothesis(theta,xi)
		if Y[i] == 1:
			error = Y[i] * math.log(hi)
		elif Y[i] == 0:
			error = (1-Y[i]) * math.log(1-hi)
		sumOfErrors += error
	const = -1/m
	J = const * sumOfErrors
	print ('cost is ', J )
	return J

        
def testLR(ntheta, X):
    theta=np.matrix(ntheta)
    probability = sigmoid(X * theta.T)
    # print(probability.shape)
    probability = [1 if x >= 0.5 else 0 for x in probability]
    # print(probability)
    return probability

def accuracy(x , y , w):
    yhat = testLR(w, x)
    accuracy = np.sum(y == yhat) / len(y)
    return accuracy

# $1 x1 + $2 x2 = 10


#Building the Logistic Regression Function
def trainLR(features, target, num_steps, learning_rate, add_intercept = False):
    m = len(target)
    AccArr =[]
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))
        
    weights = np.zeros(features.shape[1])
    
     # (768 , 8 ) (8 ,1 )
    for step in range(num_steps):
        scores = np.dot(features, weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient
        
        # Print log-likelihood every so often
        
        if step % 100 == 0:
             print("epoch # : " , step+100 )
             Cost_Function(features,target,weights,m)
             print('theta ', weights)	
             print("----------------------------------------")
             AccArr.append(accuracy(features,target,weights)) 
        
    return weights , AccArr



if __name__ == '__main__':

    X,Y = get_data("diabetes")

    
    X = X.toarray()
    Y = np.where(Y == -1, 0, 1)
    
    # print(type(X))
    # print(Y)
    
    print(X.shape)

    tr_idx, te_idx = split_data(X.shape[0],train_size = 0.8)
      
     
    Xtr = X[tr_idx,:]
    Ytr = Y[tr_idx];
    Xte = X[te_idx,:]
    Yte = Y[te_idx]

    #normalize the data
    stand_param = standardize_para(Xtr)
    Xtr = standardize_X(Xtr, stand_param)
    stand_param = standardize_para(Xte)
    Xte = standardize_X(Xte, stand_param)
    
    # print(Xtr)
    
    feature_name = ['Pregnancies', 'Glucose', 'BloodPressure', \
                'SkinThickness','Insulin', 'BMI',\
                'DiabetesPedigreeFunction', 'Age']
    ntr = Xtr.shape[0]
    feat1_neg = [Xtr[ii,3] for ii in range(0, ntr) if Ytr[ii]==0]
    feat2_neg = [Xtr[ii,6] for ii in range(0, ntr) if Ytr[ii]==0]
    feat1_pos = [Xtr[ii,3] for ii in range(0, ntr) if Ytr[ii]==1]
    feat2_pos = [Xtr[ii,6] for ii in range(0, ntr) if Ytr[ii]==1]

    plt.scatter(feat1_neg, feat2_neg, color = "r", label="label 0")
    plt.scatter(feat1_pos, feat2_pos, color = "b", label="label 1")
    plt.legend()
    plt.xlabel(feature_name[3])
    plt.ylabel(feature_name[6])
    plt.show()

    Xtr = np.hstack((Xtr,np.ones((Xtr.shape[0],1))))
    Xtr = np.insert(Xtr, 0, 1, axis=1)
    Xte = np.hstack((Xte,np.ones((Xte.shape[0],1))))
    Xte = np.insert(Xte, 0, 1, axis=1)

    
    
    #to run the model.
    weights , ave = trainLR(Xtr, Ytr,
                         num_steps = 1000, 
                         learning_rate = 0.0001,
                         add_intercept=False)
    
    #Comparing with Sk-Learn’s LogisticRegression   
    clf = LogisticRegression(fit_intercept=False, C = 0.0001)
    clf.fit(Xtr, Ytr)
    
    print("final sk_learn weights : " , clf.coef_)
    print("final trainLR weights : " , weights)
    print("----------------------------------------")

    
    # #Checking Accuracy
    acc = accuracy(Xte , Yte , weights)
    
    print('Accuracy from sk-learn:   ', clf.score(Xte, Yte))
    print('Accuracy from scratch:  ',acc)
    
    epoc = [100,200,300,400,500,600,700,800,900,1000]
    plt.scatter( epoc,ave, color = "g")
    plt.xlabel("# epoch")
    plt.ylabel("accurecy")
    plt.show()