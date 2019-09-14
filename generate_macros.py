import re
file='Reg_Map.txt'
f=open(file,'r')
content=f.readlines()
f.close()
for i in content:
    if i == '\n':
        content.remove(i)

macros={}
for i in content:
    key=i[:4]
    key=key.replace('0x','32\'h')
    val=(i[5:].replace(' ','_'))
    val=val.replace('\n','')
    macros[key]=val
    
for i in macros.keys():
    if 'RESERVED' not in macros[i]:
        print('`define'+4*' '+macros[i]+(25-len(macros[i]))*' '+i)
    

