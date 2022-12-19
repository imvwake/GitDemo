prices =[7,6,4,3,1]
m1=[]
m2=[]
t=min(prices)
t_index = prices.index(t)
for i in prices:
    if (i > t) and (prices.index(i) > t_index):
        m2.append(i)
g = max(m2)
if m2 !=0:
    
print(g-t)