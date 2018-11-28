def make_team(Player_table,data_norm,team_idx,year,device,dtype,need_idx):
    '''
    put all players in one team to one matrix with size[n,m]
    n:number of players
    m: number of features
    '''
    import numpy as np
    import torch
    loader_train={}
    for name,rate in team_idx.items():
        data_temp,exist = search_team(Player_table,data_norm,name,need_idx,'poly2')
        # if exist==0,then it means we could not find players, it should not be added
        if exist==0:
            
            pass
        else:
            data_temp = np.array(data_temp,dtype = np.float)
            ltemp = rate
            ltemp = np.array(ltemp,dtype = np.float)
            # to use pytorch, the data must be torch type, so transform data form numpy to torch
            data_temp= torch.from_numpy(data_temp)
            ltemp= torch.from_numpy(ltemp)
            # move the data to device we use
            data_temp = data_temp.to(device=device, dtype=dtype)  
            ltemp = ltemp.to(device=device, dtype=torch.float)
            # combine the data and winrate to a tuple which is the value of dictionary(key is the team+year)
            loader_train[name+year] = (data_temp,ltemp)
    return loader_train
def search_team(Player_table,data_norm,team_name,need_idx,curve_method='poly3'):
    import numpy as np
    data_team=[]
    # when exist =0,it means we could not find the player who belongs to this team
    exist = 0
    for i in range(Player_table.shape[0]):
        # we apply four kinds of curve, when 'ploy3',it means we curve x,x^2 and x^3
        if Player_table[i,1]==team_name:
            exist = 1
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
                
                
    return data_team,exist