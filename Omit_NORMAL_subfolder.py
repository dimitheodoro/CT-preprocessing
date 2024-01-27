import os
from tqdm import tqdm
import shutil
PATH_ORIGINAL = r'E:\PAGNI_CT_DEDOMENA\NORMAL'
PATH_TARGET = r'C:\Users\user1\Desktop'

if not os.path.exists(os.path.join(PATH_TARGET,'NORMAL')):
    os.mkdir(os.path.join(PATH_TARGET,'NORMAL'))


for patient in tqdm(os.listdir(PATH_ORIGINAL)[260::]):
    if not os.path.exists(os.path.join(PATH_TARGET,'NORMAL',patient)):
        os.mkdir(os.path.join(PATH_TARGET,'NORMAL',patient))
    for Brain_1_25_mm_SOFT in os.listdir(os.path.join(PATH_ORIGINAL,patient)):
        for slice in os.listdir(os.path.join(PATH_ORIGINAL,patient,Brain_1_25_mm_SOFT)):
            shutil.copyfile(os.path.join(PATH_ORIGINAL,patient,Brain_1_25_mm_SOFT,slice), os.path.join(PATH_TARGET,'NORMAL',patient,slice)  )
