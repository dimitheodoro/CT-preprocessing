import os



def alter(PATH,ADD_GCS=False,ADD_CLASS=True):
    
    if ADD_GCS:
        for folder in os.listdir(PATH):
            os.rename(os.path.join(PATH,folder),os.path.join(PATH,folder)+'^15')
    elif ADD_CLASS:
        for folder in os.listdir(PATH):
            prefix = (os.path.join(PATH,folder)).split('^')[0]
            sufix =  (os.path.join(PATH,folder)).split('^')[-1]
            new_name = prefix +'_0'+'^'+ sufix
            os.rename(os.path.join(PATH,folder),new_name)


PATH = r'C:\Users\user1\Desktop\TEST2'
alter(PATH)