import numpy as np


def load_data(X_train,y_train):
    #X_train(N,10)
    X_train = np.asarray(X_train,dtype=np.float32)
    y_train = np.asarray(y_train,dtype=np.float32)
    num_all = X_train.shape[0]
    num_train = 27000
    num_val = 3000
    num_test = 2900
    
#     mm = MinMaxScaler()
#     mm_data = mm.fit_transform(X_train)
#     temp = X_train.flatten()
#     max = np.max(temp)
#     max = 16
#     min = np.min(temp)
#     N,D = X_train.shape
#     for i in range(0,N-1):
#         for j in range(0,D-1):
#             if X_train[i,j] > 16:
#                 X_train[i,j] = 16
#     X_train = (X_train - min)/(max - min)
    
    
    
    X_val = X_train[num_train:num_train+num_val,:]
    y_val = y_train[num_train:num_train+num_val,:]
    
    mask = range(num_train+num_val,num_train+num_val+num_test)
    X_test = X_train[num_train+num_val:,:]
    y_test = y_train[num_train+num_val:,:]

    mask = range(num_train)
    X_train = X_train[:num_train,:]
    y_train = y_train[:num_train,:]

    
    return X_train,y_train,X_val,y_val,X_test,y_test
    