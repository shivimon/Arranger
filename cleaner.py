import os
import shutil

Desktop = 'C:\\Users\\sksha\\Desktop'

for file in os.listdir(Desktop):
    filename, fextension = os.path.splitext(file)

    try:
        if not fextension:
            pass
        elif fextension in ('.txt', '.ppt', '.pptx', '.xlsx', '.doc', '.docx', '.pdf'):
            shutil.move(
                os.path.join(Desktop, f'{filename}{fextension}'),
                os.path.join(Desktop, 'Documents', f'{filename}{fextension}'))

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