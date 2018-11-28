def data_norm(data_t):
    import numpy as np
    import math
    # do data normaliazation to put all data in range of [0,1]
    minu = data_t[:,0].reshape([-1,1])
    # the contribution of a player is decided by his time on game
    data_t *=minu
    for i in range(data_t.shape[1]):
        min_col = np.min(data_t[:,i])
        max_col = np.max(data_t[:,i])
        mean_col = np.mean(data_t[:,i])
        var_col = np.var(data_t[:,i])
        for j in range(data_t.shape[0]):
            #uniform
            #data_t[j,i] = float(data_t[j,i] - min_col)/(max_col- min_col)
            #normal distribution
            data_t[j,i] = float(data_t[j,i] - mean_col)/math.sqrt(var_col)
        
        min_col = np.min(data_t[:,i])
        max_col = np.max(data_t[:,i])
        for j in range(data_t.shape[0]):
            #uniform
            data_t[j,i] = float(data_t[j,i] - min_col)/(max_col- min_col)
            #data_t[j,i]/=16
    #need_idx = [1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,20]
    #data_te = data_t[:,need_idx]
    return data_t
