import pandas as pd 
import numpy as np 
import random
import random as rand
import matplotlib.pyplot as plt 
import scipy.optimize as op 
import seaborn as sbn
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

def initialize_betas(dim):
    b = random.random()
    w = np.random.rand(dim)
    return b,w

def sigmoid(b, w ,X_new):
    Z = b + np.matmul(X_new,w)
    return (1.0 / (1 + np.exp(-Z)))

def get_cost( y, y_hat):
        return - np.sum(np.dot(y.T,np.log(1-y_hat)+ np.dot((1-y).T,np.log(1-y_hat)))) / ( len(y))

def update_beta (b_0, w_0 , y , y_hat, X_new, alpha):
    db = np.sum( y_hat - y)/ len(y)
    b_0 = b_0 - alpha * db
    dw = np.dot((y_hat - y), X_new)/ len(y)
    w_0 = w_0 - alpha * dw
    return b_0,w_0

def trainLR(X,Y,Iterations,alpha):
    all_costs =[]
    acc_vse = []
    b,w= initialize_betas(X.shape[1])
    print("initial guess of b and w: " , b ,w)
    for i in range(Iterations):
        y_hat = sigmoid(b, w, X)
        current_cost = get_cost(Y, y_hat)
        prev_b = b
        prev_w = w 
        b ,w = update_beta(prev_b, prev_w, Y, y_hat, X, alpha)
        all_costs.append(current_cost)
        if i % 100 == 0 :
            print('Iteration: ', i+100 , 'Cost: ', current_cost)
            prr = testLR(X, w, b)
            acc_vse.append(accuracy(Y, prr))
    return w , b , acc_vse 

def testLR( X , theta , b ):
    # theta=np.matrix(ntheta)
    probability = sigmoid( b , theta , X )
    probability = [1 if x >= 0.5 else 0 for x in probability]    # print(probability)
    return probability

def accuracy(y, yhat):
    accuracy = np.sum(y == yhat) / len(y)
    return accuracy

if __name__ == '__main__':

    X,Y = get_data("diabetes")
    X = X.toarray()
    Y = np.where(Y == -1, 0, 1)


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
    
    feature_name = ['Pregnancies', 'Glucose', 'BloodPressure', \
                'SkinThickness','Insulin', 'BMI',\
                'DiabetesPedigreeFunction', 'Age']
    ntr = Xtr.shape[0]
    feat1_neg = [Xtr[ii,2] for ii in range(0, ntr) if Ytr[ii]==0]
    feat2_neg = [Xtr[ii,7] for ii in range(0, ntr) if Ytr[ii]==0]
    feat1_pos = [Xtr[ii,2] for ii in range(0, ntr) if Ytr[ii]==1]
    feat2_pos = [Xtr[ii,7] for ii in range(0, ntr) if Ytr[ii]==1]

    plt.scatter(feat1_neg, feat2_neg, color = "r", label="label 0")
    plt.scatter(feat1_pos, feat2_pos, color = "b", label="label 1")
    plt.legend()
    plt.xlabel(feature_name[2])
    plt.ylabel(feature_name[7])
    plt.show()

    Xtr = np.hstack((Xtr,np.ones((Xtr.shape[0],1))))
    Xtr = np.insert(Xtr, 0, 1, axis=1)
    Xte = np.insert(Xte, 0, 1, axis=1)
    Xte = np.hstack((Xte,np.ones((Xte.shape[0],1))))

    W,bias,Av_sE= trainLR(Xtr, Ytr, Iterations=1000 , alpha=0.1)
    clf = LogisticRegression(fit_intercept=False, C = 0.1)
    clf.fit(Xtr, Ytr)
    
    
    pred = testLR(Xte, W ,bias )
    print("Classification accuracy: ", accuracy(Yte, pred))       
    print('Accuracy from sk-learn:  ', clf.score(Xte, Yte))
    
    
    epoc = [1,2,3,4,5,6,7,8,9,10]
    plt.scatter( epoc,Av_sE, color = "y")
    plt.xlabel("# epoch")
    plt.ylabel("accurecy")
    plt.show()
 