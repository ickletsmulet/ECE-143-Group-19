def make_idx(dT,Abbr,teamName):
    # make the full team name into abbreviate
    dic = {}
    for i in range(dT.shape[0]):
        # .index when not found would return error, so use try
        try:
            dic[Abbr[teamName.index(dT[i,0])]]=dT[i,1]
        except:
            pass
    return dic
