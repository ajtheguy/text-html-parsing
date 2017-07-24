#Python 3.5+
#http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
#http://stackoverflow.com/questions/12842997/how-to-copy-a-file-using-python

import glob
import os
import shutil

dstroot = 'C:\JAHH-65C-R3B-V2_GP'
os.makedirs(dstroot) # create all directories, raise an error if it already exists

for filename in glob.iglob('C:\JAHH-65C-R3B-V2\**\*.vwa',recursive=True):
	#print(filename)
	shutil.copy(filename, dstroot)
	
	