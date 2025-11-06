# importing the csv library
import csv
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# function to read the csv files
def read_cm_csv(classmark):
    try:
        with open(os.path.join(script_dir, "subject_class_mark_table.csv")) as CM:
            cmreader = csv.reader(CM)
            for row in cmreader:
                  if len(row[1]) == len(classmark) and classmark in row[1]:
                        #CMlist.append(row)
                        print("[Subject, Class Mark]: ", row)
                        yield row
            
    except FileNotFoundError:
        print("File Not Found")
    
            


def read_sub_csv(subject=None, classmark=None, i=0):
    try:
      with open(os.path.join(script_dir, "subject_class_mark_table.csv")) as sub:
            subreader = csv.reader(sub)
            for row in subreader:
                  if subject in row[i]:
                        classmark = row[1]
                        liblocation = read_loc_csv(classmark, CMlen= len(classmark))
                        '''try:
                              print("[Subject, Classmark, Location]: ", row, liblocation[1])
                              return row
                        except TypeError:
                              print("[Subject, Classmark, Location]: ", row, liblocation)
                              '''
    except FileNotFoundError:
        print("File Not Found")


def read_loc_csv(classm_or_loc, CMlen=1, j=0):
    try:
      with open(os.path.join(script_dir, "BookS.csv")) as loc:
            locreader = csv.reader(loc)
            for row in locreader:
                  if j == 0:
                        invalid = True
                        if classm_or_loc in row[j] and CMlen == 2:
                              #print("[Subject, Class Mark]")
                              for newrow in read_cm_csv(classm_or_loc):
                                    print("Location: ", row[1])
                                    invalid =False
                              #print(subjectname)
                              #return newrow
                        elif classm_or_loc in row[j] and CMlen == 1:
                              classmarks= row[0].strip('[]')
                              classmarks= classmarks.split(",")
                              #print(classmarks)
                              for classmark in classmarks:
                                    #print(classmark)
                                    if classm_or_loc in classmark and CMlen == len(classmark):
                                          for newrow in read_cm_csv(classm_or_loc):
                                                print("Location: ", row[1])
                                                invalid = False
                        elif classm_or_loc not in row[j]:
                              print("Invalid Reference")
                                    
            
                  elif j ==1:
                        if classm_or_loc in row[j]:
                              print(row)
                              classmarks= row[0].strip('[]')
                              classmarks= classmarks.split(",")
                              #classmarks= classmarks.replace(" ", "")
                              for classmark in classmarks:
                                    for newrow in read_cm_csv(classmark):
                                         print("\n")
    except FileNotFoundError:
         print("File Not Found")
      
                  






welcomeText=('''Welcome to Library Map text Appplication \n 
      Select one of the following options: \n 
      1. Enter the subject name or part-name \n
      2. Enter the subject classmark (CM) \n
      3. Enter the location of the subject that you are trying to find. 
      ''')
print(welcomeText)
option = int(input('Select from one of the following options above (1, 2, or 3): '))
# code to read the csv fie 
optionList=[1,2,3]
while option not in optionList:
    print("Wrong input entered!, Select one from the options above \n", welcomeText)
    option = int(input('Select from one of the following options above (1, 2, or 3):   '))
else:    
    if option == 1:
      subject= input("Enter the subject that you are looking for: e.g: English, Mathematics   ")
      #sublen = len(subject)
      read_sub_csv(subject)

    elif option == 2:
      CM = input("Enter the Classmark CM of the subject you are looking for: e.g: K, PL,JX   ").upper()
      CMlen= len(CM)
      read_loc_csv(CM, CMlen, j=0)
      #read_cm_csv(CM)

    elif option == 3:
      location= input("Enter the Location: e.g: Ground Floor, Middle Floor, Top FLoor  ")
      read_loc_csv(location,j=1)

    
