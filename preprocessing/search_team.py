def search_team(Player_table,data_norm,team_name,curve_method='poly3'):
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
