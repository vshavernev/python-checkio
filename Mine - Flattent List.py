def flat_list(a):
    r[:] = []
    return P(a)

def P(l):
    for i in l:
        if isinstance(i,int): r.append(i)
        else: P(i)
    return(r)

r = []


#def flat_list(l):
#    r = []
#    def f(l):
#        for i in l:
#            r.append(i) if type(i) is int else f(i)
#    f(l)
#
#    return r


