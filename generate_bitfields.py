file='field_map.txt'
f=open(file,'r')
content=f.readlines()
f.close()
for i in content:
    if i == '\n':
        content.remove(i)

bitfield={}
reg='device_cpblty'
for i in content:
    key,val=i.split('\t')
    val=(val.replace(' ','_'))
    val=val.replace('\n','')
    bitfield[key]=val
    
for i in bitfield.keys():
    if 'RESERVED' not in bitfield[i]:
        print('`define'+4*' '+bitfield[i]+(25-len(bitfield[i]))*' '+i)
# Instead of this calculate the init value by plugging in the fields reset value        
for i in bitfield.keys():
	print(reg+'[`'+bitfield[i]+']<=0;')
