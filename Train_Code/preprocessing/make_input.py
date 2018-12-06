def make_input(data_norm,curve_method='poly3'):
    '''
    this module is to change the player tabel into a valid input of the train model, we should select a curve_method
    
    input:data_norm
    type:numpy.array() which contains the data normalized
    input:curve_method
    type:str
    
    output:data_team
    type:numpy.array() which contains the data normalized and using different curve method
    '''
    import numpy as np
    data_team=[]
    # when exist =0,it means we could not find the player who belongs to this team
    for i in range(data_norm.shape[0]):
        # we apply four kinds of curve, when 'ploy3',it means we curve x,x^2 and x^3

        if curve_method=='poly3':
            #poly
            poly = data_norm[i,need_idx]
            poly = np.stack((poly,(data_norm[i,need_idx])**2,data_norm[i,need_idx]**3),0)
            poly = poly.reshape([1,-1])[0]

            data_team.append(poly)
        elif curve_method=='poly2':
            poly = data_norm[i,need_idx]
            poly = np.stack((poly,(data_norm[i,need_idx])**2),0)
            poly = poly.reshape([1,-1])[0]

            data_team.append(poly)
        elif curve_method=='poly4':
            poly = data_norm[i,need_idx]
            poly = np.stack((poly,(data_norm[i,need_idx])**2,data_norm[i,need_idx]**3,data_norm[i,need_idx]**4),0)
            poly = poly.reshape([1,-1])[0]

            data_team.append(poly)
        elif curve_method=='linear':
            linear = data_norm[i,need_idx]

            data_team.append(linear)
            
return data_team
