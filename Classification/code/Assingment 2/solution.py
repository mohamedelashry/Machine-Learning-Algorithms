import pandas as pd 
import numpy as np 
import random as rand
import matplotlib.pyplot as plt 
import scipy.optimize as op 
import seaborn as sbn
from sklearn.datasets import load_svmlight_file
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from random import randint

def get_data(df):
    # load_svmlight_file loads dataset into sparse CSR matrix
    data = np.loadtxt(df, delimiter=",")
    X = data[:,:-1];
    Y = data[:,-1];
    return X,Y

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / y_true.shape[0]
    return accuracy*100

def sgd_pegasos_svm(x, y, weights, lam, iterations):
    if type(weights) == type(None): weights = np.zeros(x[0].shape)
    num_S = len(y)
    for i in range(iterations):
        it = randint(0, num_S-1)
        step = 1/(lam*(i+1))
        decision = y[it] * weights @ x[it].T
        if decision < 1:
            weights = (1 - step*lam) * weights + step*y[it]*x[it]
        else:
            weights = (1 - step*lam) * weights
    return weights

def train_seqSVM(x, y, lam, max_iter):
    n,d = x.shape; 
    uniqlbl = np.unique(y)
    w = np.zeros((len(uniqlbl),d))
    ########
    for j in range(1, len(uniqlbl) + 1):
        theta = np.zeros(d)
        y_i = np.array([1 if label == j else 0 for label in y])
        y_i = np.reshape(y_i, (n, 1))        
        theta = sgd_pegasos_svm(x, y_i,theta,lam, max_iter)
        w[j-1,:] = theta   
    ########
    return w
   
def mini_batch_pegasos_svm(x, y,weights, lam, iterations,batch_size):
    if type(weights) == type(None): weights = np.zeros(x[0].shape)
    num_S = len(y)
    for i in range(iterations):
        step = 1/(lam*(i+1))
        # mini-batch sampling
        batch = np.random.choice(np.arange(0, num_S), batch_size)
        sum_vect = []
        for q in batch:
                sum_vect.append(y[q] * x[q])
        w =(1 - step*lam) * weights + ((step / batch_size) * sum(sum_vect))
    return w

def train_batchSVM(x, y, lam, max_iter,batch_size):
    n,d = x.shape; 
    uniqlbl = np.unique(y)
    w = np.zeros((len(uniqlbl),d))
    indx = np.arange(n)
    ######
    for j in range(1, len(uniqlbl) + 1):
        theta = np.zeros(d)
        y_i = np.array([1 if label == j else 0 for label in y])
        y_i = np.reshape(y_i, (n, 1))        
        theta = mini_batch_pegasos_svm(x, y_i,theta,lam,max_iter,batch_size)
        w[j-1,:] = theta 
    ######
    
    return w

def test_algorithm(x,y,w):
    pred = []
    uniqlbl = np.unique(y)
    ########
    prod= np.dot(x,np.transpose(w))
    ########
    return np.argmax(prod,axis=1)+1

def cross_val(n_samples,n_splits):

    # reference: scikit-learn
    idx = np.arange(n_samples)
    fold_sizes = np.full(n_splits, n_samples // n_splits, dtype=np.int)
    fold_sizes[:n_samples % n_splits] += 1
    current = 0
    indices = []
    for fold_size in fold_sizes:
        start, stop = current, current + fold_size
        indices.append(idx[start:stop])
        current = stop
    return indices

def seq_model_select(X, Y,grid_, n_fold,max_iter):

    n_sample = X.shape[0]
    indices=cross_val(n_sample,n_fold)
    for fold in range(n_fold):
        indxte = indices[fold];
        indxtr = np.setdiff1d(np.arange(0,n_sample), indxte)

        Xtr_v = X[indxtr,:]
        Ytr_v = Y[indxtr]
        Xte_v = X[indxte,:]
        Yte_v = Y[indxte]

        #######
        acc = []
        for g in grid_:
            w = train_seqSVM(Xtr_v,Ytr_v,g,max_iter)
            gg = accuracy(Yte_v, test_algorithm(Xte_v,Yte_v , w))
            acc.append(gg)
        #######

    return grid_[np.argmax(acc)]

def batch_model_select(X, Y,grid_, n_fold,batch_size,max_iter):
    
    n_sample = X.shape[0]
    indices=cross_val(n_sample,n_fold)
    for fold in range(n_fold):
        indxte = indices[fold];
        indxtr = np.setdiff1d(np.arange(0,n_sample), indxte)

        Xtr_v = X[indxtr,:]
        Ytr_v = Y[indxtr]
        Xte_v = X[indxte,:]
        Yte_v = Y[indxte]

        ########
        acc = []
        for g in grid_:
            w = train_batchSVM(Xtr_v,Ytr_v,g,max_iter,batch_size)
            gg = accuracy(Yte_v, test_algorithm(Xte_v,Yte_v , w))
            acc.append(gg)
        #######
    return grid_[np.argmax(acc)]

df = 'dna.scale.tr'
Xtr,Ytr = load_svmlight_file(df)
Xtr = Xtr.toarray()
#Ytr = Ytr[:,np.newaxis]

df = 'dna.scale.val'
Xv,Yv= load_svmlight_file(df)
Xv = Xv.toarray()
#Yv = Yv[:,np.newaxis]

Xtr = np.vstack((Xtr,Xv))
Ytr = np.hstack((Ytr,Yv))

df = 'dna.scale.t'
Xte,Yte = load_svmlight_file(df)
Xte = Xte.toarray()
#Yte = Yte[:,np.newaxis]



Ytr = Ytr.reshape((-1))
Yte = Yte.reshape((-1))

Xtr = np.hstack((Xtr,np.ones((Xtr.shape[0],1))))
Xte = np.hstack((Xte,np.ones((Xte.shape[0],1))))

##########################################

grid_ = [1e-5,1e-3,1e-2,1e-1,1,10]
n_fold = 3
max_iter = 500

###
# Model selection
###
seq_lam = seq_model_select(Xtr, Ytr,grid_,n_fold,max_iter)
# Train best model on training set
W = train_seqSVM(Xtr, Ytr,seq_lam,max_iter)
# # Test the model on test set 
scores = test_algorithm(Xte,Yte,W)
print("SeqSVM accuracy on test set:", f'{accuracy(Yte, scores):2.2f}')

##########################################

###
# Model selection
###
batch_size = 100
grid_ = [1e-5,1e-1,1,5,10,100]
batch_lam = batch_model_select(Xtr, Ytr,grid_,n_fold,max_iter,batch_size)
# Train best model on training set
W = train_batchSVM(Xtr, Ytr,100,max_iter,batch_size)
# Test the model on test set 
scores = test_algorithm(Xte,Yte,W)
print("Mini-batch SVM accuracy on test set:", f'{accuracy(Yte, scores):2.2f}')

##########################################

maxiters = [50,100,200,500,700,800,1000,2000,4000,5000]
seq_acc =[];
batch_acc =[];
for itr in maxiters:
    W = train_seqSVM(Xtr, Ytr,seq_lam,itr)
    scores = test_algorithm(Xte,Yte,W)
    seq_acc.append(accuracy(Yte, scores))

    W = train_batchSVM(Xtr, Ytr,batch_lam,itr,batch_size)
    scores = test_algorithm(Xte,Yte,W)
    batch_acc.append(accuracy(Yte, scores))

plt.figure(1, figsize=(5, 3))
plt.clf()
seq_curve = plt.plot(maxiters,seq_acc)
batch_curve = plt.plot(maxiters,batch_acc)
plt.setp(seq_curve, color='r', marker='o',linewidth=2.0,linestyle='dashed')
plt.setp(batch_curve, color='b', marker='D',linewidth=2.0,linestyle='dashdot')
plt.legend(('SGD SVM', 'Mini-batch SVM'))
plt.xlabel('Iterations')
plt.ylabel('Accuracy %')
plt.tight_layout()
plt.show()