#http://stackoverflow.com/questions/11968998/remove-lines-that-contain-certain-string
#http://stackoverflow.com/questions/6745854/one-liner-for-removing-blank-lines-from-a-file-in-python
#Remove txt file keyword lines and blank lines.
import fileinput

bad_words = ['Column Keys', 'Market SID', 'Worksheet Data']

with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            line = line.rstrip()
            if line != '':
                newfile.writelines(line+'\n')

oldfile.close(), newfile.close()

            


