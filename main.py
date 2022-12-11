import glob
import pandas as pd
import re

def get_glob_list():
    glob_list = glob.glob('*.log') + glob.glob('*.log.*')
    return glob_list

def read_files(glob_list):
    df = pd.DataFrame(columns = ['date', 'users'])
    for file in glob_list:
        with open(file) as f:
            for line in f.readlines():
                parsed = parse_line(line)
                if parsed:
                    df.loc[len(df.index)] = [parsed[0], parsed[1]] 
    #convert the 'Date' column to datetime format
    df['date']= pd.to_datetime(df['date'])
    df.sort_values(by='date')
    return df
    #print(df.to_string(index=False))

#TODO: regex
def parse_line(line):
        x = re.search('\(Number\sof\sconcurrent\ssessions:\s',line)
        if x:
            d_time =  line[:23]
            y = re.search("\ssessions:\s", line)
            if y:
                c_users = line[y.end():-3]
                return (d_time, c_users)
            else:
                 print('ISSUE '+ line )
        else:
            return False

if __name__ == '__main__':
    
    '''
    print('Parsing data from files...')
    df = read_files(get_glob_list())

    print('Saving data to CSV...')
    df.to_csv('concurrent_users.csv', index = False)
    ''' 

    print('Read parsed data from CSV...')
    df = pd.read_csv('concurrent_users.csv')

    df['date']= pd.to_datetime(df['date'])
    print(df.info())
    print(df)
    date_max = df['date'].max()
    date_min = df['date'].min()
    print (date_min)
    print (date_max)


