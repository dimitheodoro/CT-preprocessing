1) PAGNI_CT DEDOMENA-> NORMAL
EINAI ΗΔΗ στην μορφή που χρειαζόμαστε
E:\PAGNI_CT_DEDOMENA\NORMAL\ADAMAKIS IOANNIS_01_03_23\Brain 1.25 mm SOFT
αυτά τα διαβαζω από την 
load_multiple_patients_LOAD_FROM_CLASS 
PATH_WITH_ALL_SCANS = r'E:\PAGNI_CT_DEDOMENA\NORMAL' 
THis works for 'E:\PAGNI_CT_DEDOMENA\NORMAL'  forlder. each patient has  inner folders
και αποθηκεύονται σαν patients me dict_keys(['volume', 'name', 'sex', 'age'])
all_slices

2) PAGNH-CT AI
MORE -OR-EQUAL -15 (88 περιστατικα)
δεν ειναι στην μορφή που θέλουμε 
έτσι τα ξεκαθαρίζω  και δημιουργώ έναν φάκελο PAGNI_TEST 
με την Data_cleaning  
PATH_DESKTOP = r'C:\Users\user1\Desktop\PAGNI_TEST' 
apply the function 
MORE_OR_EQ_PATH = r'E:\PAGNI_CT_DEDOMENA\PAGNH-CT-AI\MORE-OR-EQUAL-15' 
αυτόν το φάκελο τον διαβάζω με την
load_multiple_patients_LOAD_FROM_CLASS  

THis works for 'C:\Users\user1\Desktop\PAGNI_TEST' forlder. each patient has slices only and not inner folder
PATH_WITH_ALL_SCANS = r'C:\Users\user1\Desktop\PAGNI_TEST'
και αποθηκεύονται σαν patients me dict_keys(['volume', 'name', 'sex', 'age'])
all_slices


3) PAGNH-CT AI 
UNDER-15 NORMAL
