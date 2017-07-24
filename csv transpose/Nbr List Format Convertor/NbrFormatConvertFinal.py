import csv

reader=csv.reader(file("RNC2NewIRATNbr.csv"))

f=open('./IRATNbrOutputRNC2.csv','w')
for line in reader:
    c=0
    for item in line:
            
                
            if item !='' and c>0:
                
                    print item
                    f.write(line[0]+','+item+'\n')
            c=c+1
f.close
