import os

cwd_n = ''
cwd = os.getcwd()
path = cwd + '\\'

filepath = open(path + 'Path.txt' , 'r+')
user_path = filepath.read()

if user_path == '':
    user_path = 'NO PATH FOUND!'
choice = input('To use already saved path ' + '[ ' + user_path + ' ] press 1. For new path press 2. ')

if choice == '1':
    cwd_n = user_path
    
elif choice == '2':
    new_path = input('Enter new path: ')
    cwd_n = new_path
    filepath.write(new_path)
    
if cwd_n == '':
    print('Invalid path')
    input()
    quit()
    
path = '"' + cwd_n + '\\'

file_names = os.listdir(cwd_n)
filepath.close()

def remove_suf(ogname):
    pos_suffix = -1
    if ogname.find('.mp4') != -1:
        pos_suffix = ogname.find('.mp4')
    elif ogname.find('.mkv') != -1:
        pos_suffix = ogname.find('.mkv')
    elif ogname.find('.avi') != -1:
        pos_suffix = ogname.find('.avi')
    if pos_suffix != -1:
        new_name = ogname[0: pos_suffix]
        return new_name
    else:
        return ogname
    
def remove_s(ogname, r,k):
    for s_num in range(r,k):
        if s_num < 10:
            fill = '0'
        else:
            fill = ''
        if ogname.find('s' + str(s_num)) == -1:
            pos_s1 = ogname.find('s' + fill + str(s_num))
        elif ogname.find('s' + fill + str(s_num)) == -1:
            pos_s1 = ogname.find('s' + str(s_num))
        if pos_s1 != -1:
            new_name = ogname[0:pos_s1]
            name = new_name + 'S' + fill + str(s_num)
            return name
        
    return ogname
        
def remove_sea(ogname, r,k):
    for s_num in range(r,k):
        if s_num < 10:
            fill = '0'
        else:
            fill = ''
        pos_season1 = ogname.find('season ' + str(s_num))
        if pos_season1 != -1:
            new_name = ogname[0:pos_season1]
            name = new_name + 'S' + fill + str(s_num)
            return name
        
    return ogname

def move_files(tomove):                
    #folder_name is the file after editing, this is the name of the created folder
    for folder_name in tomove:
        os.system('md ' + path + folder_name + '"')
        #files_move is the original name of the file
        for files_move in tomove[folder_name]:
            os.system('move ' + path +  files_move + '"' + ' ' + path + folder_name + '"')
            print('\n')
            print('move ' + path +  files_move + '"' + ' ' + path + folder_name + '"')            
            
        

def sort(file_names):
    fileDir = {}
    for name_1 in file_names:
        if '.py' not in name_1 or name_1 != 'Path.txt':
            clean_fname = ''
            
            name_1 = name_1.lower()
            name_nsuf = remove_suf(name_1)
            name = remove_s(name_nsuf,10,30)
            if name == name_nsuf:
                name = remove_sea(name_nsuf,10,30)
                if name == name_nsuf:
                    name = remove_s(name_nsuf,1,10)
                    if name == name_nsuf:
                        name = remove_sea(name_nsuf,1,10)

            for pos in name:
                if pos == '.' or pos == '_' or pos == '-':
                    clean_fname += ' '
               
                else:
                    clean_fname += pos 

            fileDir[name_1] = clean_fname
    return fileDir

def delete(to_del, fileDir):
    for value in to_del:
        del fileDir[value]
    
def compare(fileDir):
    #Compare Files
    #fname is the original name of the file before editing
    
    for fname in fileDir:
        to_del = []
        tomove = {}
        for key in fileDir:
            if fileDir[fname] in fileDir[key]:
                    # fileDir[fname] is the name the folder will be given
                    # fileDir[key] is the file to be moved
                    if len(tomove)>0:   
                        tomove[fileDir[fname]].append(key)
                    else:
                        tomove[fileDir[fname]] = [fname]
                    to_del.append(key)


        move_files(tomove)
        delete(to_del, fileDir)
        break
        

filedir = sort(file_names)
for a in range(len(filedir)):
    compare(filedir)


