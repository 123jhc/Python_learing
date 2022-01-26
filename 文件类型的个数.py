import os
import os.path

count_txt = 0
count_py = 0
count_dir = 0
count_else = 0
count_ple = 0

def count(path):
    os.chdir(path)
    f_list = os.listdir('.')
    for each in f_list:
        if os.path.isdir(each):
            global count_dir
            count_dir += 1
            count(each)
            os.chdir('..')
        else:
            f_tuple = os.path.splitext(each)
            if f_tuple[1] == '.ple':
                global count_ple
                count_ple += 1

count("F://test")
print(count_dir,'\n',count_ple)
            

    
                
    

