import re
file='ports.txt'
f=open(file,'r')
content_raw=f.readlines()
f.close()
rem_comments=True #If your code came with commments next to port declaration this will take them out
content=[]
#Removes empty lines
for i in content_raw:
    if (';' in i):
        content.append(i)

print(content)
content_comm=[]
for i in content:
    if rem_comments:
        a=i[:i.find('//')]
        content_comm.append(a)
                    
content=content_comm            
        
    

port=re.compile('\w*;')
ports=[]
inst_ports=[]
prefix=''

for i in content:
    a=port.findall(i)[0]
    a=a.replace(';','')
    ports.append(a)
    a=prefix+a
    inst_ports.append(a)


#Declaring the reg and wires needed to instantiate 
for i in content:
    if('input' in i):
        i=i.replace('input','reg')
    if('output' in i):
        i=i.replace('output','wire')
    #i=i.replace(';',',')
    i=i.replace('\n','')
    print(i)
        

        
#Instantiating inside your module
for i in range(len(ports)):
    print('.'+ports[i]+'('+inst_ports[i]+'),')
	

