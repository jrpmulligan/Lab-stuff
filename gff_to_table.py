#! /usr/bin/env python
import sys
import re

f=open(sys.argv[1]) #open file and make into array
farray=f.readlines()
del farray[1],farray[0]
f.close()



def Gettheinfo(gffarray): #get the information needed for the table
    theinfo=[]
    for i in gffarray:
        u=[]
        z=i.split()
        if 'CDS' in i: #helps make index numbers consistent
            z.remove('CDS')
        if len(z)>=8:
            gene=re.search('ID=(.+?);',z[8])#getting the geneID 
            #print(z)
            gene2=re.search('gene=hcp;',z[8])
            if gene2!=None:
                u=[z[0],'hcp',z[3],z[4]]#information index numbers into new array
                if z[6]=='+':
                    u.append('forward')
                    u.append('1')
                else:
                    u.append('reverse')
                    u.append('-1')
                theinfo.append(u) #add array to matric
            elif gene !=None:
                u=[z[0],gene.group(1),z[3],z[4]]#information index numbers into new array
                if z[6]=='+':
                    u.append('forward')
                    u.append('1')
                else:
                    u.append('reverse')
                    u.append('-1')
                theinfo.append(u) #add array to matric
    return theinfo
theinfo=(Gettheinfo(farray))

orig_stdout=sys.stdout #print to file
g=open(sys.argv[2],'w')
sys.stdout=g
print('molecule\tgene\tstart\tend\tstrand\tdirection')
for h in theinfo:      
    print(h[0]+'\t'+h[1]+'\t'+h[2]+'\t'+h[3]+'\t'+h[4]+'\t'+h[5])
sys.stdout=orig_stdout
g.close()

