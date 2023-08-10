import os
import glob
import shutil

sourcepath = str(input("Enter source path of file you want to move:- "))
destinationpath = str(input("Enter Destination Path of file of u want to move to:- "))

print("\n")
print(f"Source Path of files is {sourcepath},Destination Path of Files is {destinationpath}")
print("\n")


class MoveFiles:

    def __init__(self,sourcepath,desinationpath):
        self.sourcepath = sourcepath
        self.destinationpath = desinationpath

    def check_error(self):
        """
        Check if Dictionary EXists
        """
        try:
            if os.path.isdirr(self.sourcepath) and os.path.isdir(self.destinationpath) == True:
                pass
        except FileNotFoundError:
            print("File Not Found")
    def move_file(self):
        source_files = os.listdir(self.sourcepath)
        for files in source_files:
            shutil.move(os.path.join(self.sourcepath,files),os.path.join(self.destinationpath,files))

    folder_path  =  os.getcwd()

    def text_files(self):
        text_files = glob.glob('*.txt')
        if text_files:
            os.mkdir('Text')
            for i in text_files:
                shutil.move(i,'Text')

    def video_files(self):
        video_files = glob.glob('*.mp4')
        video_files2 = glob.glob('*.mkv')
        if video_files or video_files2:
            os.mkdir('Videos')
            for i in video_files:
                shutil.move(i,'Videos')
            for i in video_files2:
                shutil.move(i,'Videos')

    def code_files(self):
        python_files = glob.glob('*.py')
        html_files = glob.glob('*.html')
        css_files = glob.glob('*.css')
        if python_files or html_files or css_files:
            os.mkdir('Code')
            for i in python_files:
                shutil.move(i,"Code")
            for i in html_files:
                shutil.move(i,"Code")
            for i in css_files:
                shutil.move(i,"Code")

    def image_files(self):
        image_files = glob.glob('*.jpg')
        image_files2 = glob.glob('*.png')
        if image_files or image_files2:
            os.mkdir('Images')
            for i in image_files:
                shutil.move(i,'Images')
            for i in image_files2:
                shutil.move(i,'Images')


files = MoveFiles(sourcepath,destinationpath)
files.code_files()
files.move_file()
files.text_files()
files.video_files()
files.image_files()
files.code_files()