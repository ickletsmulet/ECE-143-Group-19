def make_idx(dT,Abbr,teamName):
    '''
    
    this module is to build a dictionary in which key is the abbreviate name of the team(we need this to search for players in that team) and the 
    value is the total winning rate of the team whole season.
    
    input:dT:numpy.array() in which shows the whole name of teams and the total wining rate
    Abbr:list of the abbreviate name
    teamname: list of the whole name
    '''
    # make the full team name into abbreviate
    dic = {}
    for i in range(dT.shape[0]):
        # .index when not found would return error, so use try
        try:
            dic[Abbr[teamName.index(dT[i,0])]]=dT[i,1]
        except:
            pass
    return dic
