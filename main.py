from src.utils.functions import convert_to_html 
import os.path
import os
import shutil

def copy_from_static():
    if not os.path.exists('static'):
        raise Exception("Caught an error while trying to copy source files from static directory: no directory named static was found!")
    if not os.path.exists('public'):
        raise Exception("Caught an error while trying to copy source file to public directory: no directory named public was found!")
    copy_recursive()


def copy_recursive(path=''):
    for file in os.listdir('static/'+path):
        if os.path.isfile('static/'+path+'/'+file):
            shutil.copy('static/'+path+'/'+file, 'public/'+path+'/'+file)
        else:
            os.mkdir('public/'+path+'/'+file)
            copy_recursive(path+"/"+file)

def clear_public_folder():
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.mkdir('public') 


def main():
    clear_public_folder()
    copy_from_static()


if __name__ == "__main__":
    main()
