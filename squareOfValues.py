# debugging code:
c=dict()
for i in range(1,16):
    c=i*i
print(c)  

# debuged code:
dict={}
for i in range(1,16):
    c=i*i
    dict[i]=c
print(dict)  