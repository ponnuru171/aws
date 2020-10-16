x={'a':10,'b':20,'c':30}
for dict_key,dict_value in x.items():
    print(dict_key,'-->',dict_value)
a={'ponnuru':5171}
b={'srinu':5162}
c={'ganesh':5142}
d={'chandu':5009}
e={}
for e in (a,b,c,d):
    e.update(e)
    print(e)
print(sum(x.values()))