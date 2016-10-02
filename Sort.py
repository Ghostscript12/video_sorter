#import file names into a list
#
#
#
#

file_names = []
count = 0
fileDir = []
for name in file_names:
clean_fname = ''

    for pos in name:
       try:
           int(name[pos])
           clean_fname += ''
       except:
           if name[pos] == '.' or name[pos] == '_' or name[pos] == '-':
               clean_fname += ' '
       
           else:
               clean_fname += name[pos]

    fileDir.append(clean_fname)

for fname in fileDir:
    for a in range(0,len(fileDir) -1):
        
        
    

