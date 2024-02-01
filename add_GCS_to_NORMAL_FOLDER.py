import os


PATH_TO_NORMAL = r'E:\PAGNI_CT_DEDOMENA\NORMAL'

for folder in os.listdir(PATH_TO_NORMAL):
    os.rename(os.path.join(PATH_TO_NORMAL,folder),os.path.join(PATH_TO_NORMAL,folder)+'^15')
