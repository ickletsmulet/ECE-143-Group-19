def data_norm(data_t):
    '''
    this module is to do data normaliazation(first turn to normal distribution and then put them into range[0,1])
    
    input:data_t
    type: numpy.array() in which the first column is the minutes one player played total season
    output:data_t
    type: numpy.array() in which all the data is normalized without the first column
    '''
    import numpy as np
    import math
    # do data normaliazation to put all data in range of [0,1]
    minu = data_t[:,0].reshape([-1,1])
    # the contribution of a player is decided by his time on game
    data_t *=minu
    for i in range(data_t.shape[1]):

        mean_col = np.mean(data_t[:,i])
        var_col = np.var(data_t[:,i])
        for j in range(data_t.shape[0]):
            
            #normal distribution
            data_t[j,i] = float(data_t[j,i] - mean_col)/math.sqrt(var_col)
        
        min_col = np.min(data_t[:,i])
        max_col = np.max(data_t[:,i])
        for j in range(data_t.shape[0]):
            #uniform
            data_t[j,i] = float(data_t[j,i] - min_col)/(max_col- min_col)

    return data_t