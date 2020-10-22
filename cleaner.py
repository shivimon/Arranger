import os
import shutil

Desktop = 'C:\\Users\\sksha\\Desktop'  #getting the desktop path into Desktop variable

for file in os.listdir(Desktop):        #scanning all the files present in the Desktop
    filename, fextension = os.path.splitext(file) #splitting the file-names and their file-extensions

    try:
        if not fextension:
            pass
        #grouping all the files belonging to a particular category by matching the file extensions mentioned in the tuple
        elif fextension in ('.txt', '.ppt', '.pptx', '.xlsx', '.doc', '.docx', '.pdf'):
            shutil.move(    #recursively move a file to an another location defined
                os.path.join(Desktop, f'{filename}{fextension}'),
                #picking the file from the current path 
                os.path.join(Desktop, 'Documents', f'{filename}{fextension}'))
                #moving the file into new path or the folder having similar files.

        elif fextension in ('.mp3', '.wma', '.wav'):
            shutil.move(
                os.path.join(Desktop, f'{filename}{fextension}'),
                os.path.join(Desktop, 'Music', f'{filename}{fextension}'))

        elif fextension in ('.jpeg', '.jpg', '.png', '.gif', '.bmp'):
            shutil.move(
                os.path.join(Desktop, f'{filename}{fextension}'),
                os.path.join(Desktop, 'Pictures', f'{filename}{fextension}'))

        elif fextension in ('.mp4', '.mov', '.mpeg', '.wmv', '.mpg', '.webm'):
            shutil.move(
                os.path.join(Desktop, f'{filename}{fextension}'),
                os.path.join(Desktop, 'Videos', f'{filename}{fextension}'))

        else:
            shutil.move(
                os.path.join(Desktop, f'{filename}{fextension}'),
                os.path.join(Desktop, 'Other files', f'{filename}{fextension}'))
    
    except (FileNotFoundError,PermissionError):
        pass