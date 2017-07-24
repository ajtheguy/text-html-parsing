#Python 3.5+
#Concatenate txt files
#http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
#http://stackoverflow.com/questions/13613336/python-concatenate-text-files
#Remove txt file keyword lines and blank lines.
#http://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string
#http://stackoverflow.com/questions/6745854/one-liner-for-removing-blank-lines-from-a-file-in-python

import glob
import fileinput


def concat(cat_file):
    with open (cat_file,'w') as outfile:
        for filename in glob.iglob('.\*.txt',recursive=False):
            #print(filename)
            with open(filename) as infile:
                for line in infile:
                    outfile.write(line)
            infile.close()

    outfile.close()


def rmlines(cat_file):
    bad_words = ['Column Keys', 'Market SID', 'Worksheet Data']

    with open(cat_file) as oldfile, open('newfile.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                line = line.rstrip()
                if line != '':
                    newfile.writelines(line+'\n')

    oldfile.close(), newfile.close()

concat('cat_file.txt');
rmlines('cat_file.txt');
                
