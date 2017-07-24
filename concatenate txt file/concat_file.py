#Python 3.5+
#Concatenate txt files
#http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
#http://stackoverflow.com/questions/13613336/python-concatenate-text-files

import glob

with open ('cat_file.txt','w') as outfile:
    for filename in glob.iglob('.\*.txt',recursive=False):
	#print(filename)
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)
        infile.close()

outfile.close()
                
	
