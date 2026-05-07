from tabulate import tabulate
title=['Name','Age','Dept']
data=[['Anand',22,'Csm'],['Rihit',20,"cse"],['Deek',21,'Mech']]
res=tabulate(data,headers=title,tablefmt='grid')
with open('stdnts.txt',"w") as file:
    file.write(res)