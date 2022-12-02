import glob
import pandas
import re

def get_glob_list():
    glob_list = glob.glob('*.log') + glob.glob('*.log.*')
    return glob_list

def read_files(glob_list):
    for file in glob_list:
        with open(file) as f:
            for line in f.readlines():
                #print(line)
                parse_line(line)


#TODO: regex
def parse_line(line):
    # try:
        x = re.search('\(Number\sof\sconcurrent\ssessions:\s',line)
        if x:
            #try:
            print (line[:23], end = ' ')
            y = re.search("\ssessions:\s", line)
            if y:
                print(line[y.end():-3])
            else:
                print('ISSUE '+ line )
            
            #print()
    #except:
    #    print('no')
    #if x:
    #    print(line)

if __name__ == '__main__':
    print('testing')
    read_files(get_glob_list())