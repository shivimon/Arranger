
import os
import shutil
def moving():
    print("moving the file...")
def Documents():
    if not fextension:
            pass
        #grouping all the files belonging to a particular category by matching the file extensions mentioned in the tuple
    elif fextension in ('.txt', '.ppt', '.pptx', '.xlsx', '.doc', '.docx', '.pdf'):
        moving()
        shutil.move(    #recursively move a file to an another location defined
            os.path.join(Desktop, f'{filename}{fextension}'),
                #picking the file from the current path 
            os.path.join(Desktop, 'Documents', f'{filename}{fextension}'))
                #moving the file into new path or the folder having similar files.

def Music():
    if not fextension:
            pass
    elif fextension in ('.mp3', '.wma', '.wav'):
        moving()
        shutil.move(
            os.path.join(Desktop, f'{filename}{fextension}'),
            os.path.join(Desktop, 'Music', f'{filename}{fextension}'))

def Picture():
    if not fextension:
            pass
    elif fextension in ('.jpeg', '.jpg', '.png', '.gif', '.bmp'):
        moving()
        shutil.move(
            os.path.join(Desktop, f'{filename}{fextension}'),
            os.path.join(Desktop, 'Pictures', f'{filename}{fextension}'))


def Videos():
    if not fextension:
            pass
    elif fextension in ('.mp4', '.mov', '.mpeg', '.wmv', '.mpg', '.webm'):
        moving()
        shutil.move(
            os.path.join(Desktop, f'{filename}{fextension}'),
            os.path.join(Desktop, 'Videos', f'{filename}{fextension}'))

def Otherfiles():
    if not fextension:
            pass
    else:
        moving()
        shutil.move(
            os.path.join(Desktop, f'{filename}{fextension}'),
            os.path.join(Desktop, 'Other files', f'{filename}{fextension}'))
    
Desktop = 'C:\\Users\\sksha\\Desktop'  #getting the desktop path into Desktop variable

for file in os.listdir(Desktop):        #scanning all the files present in the Desktop
    print(file)
user_command=input("Do you want to move these files into their respective folders: press 'Y' to proceed else 'N' to decline:  ")
for file in os.listdir(Desktop):
    if(user_command=='Y' or user_command=='y'):
        filename, fextension = os.path.splitext(file) #splitting the file-names and their file-extensions

        try:
            Documents()
            Music()
            Picture()
            Videos()
            Otherfiles()
        except (FileNotFoundError,PermissionError):
            pass
    elif (user_command==' N' or user_command=='n'):
        exit()