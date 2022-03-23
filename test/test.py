import os

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'download',"imgs")
file_path = os.path.join(dir_path,"test.txt")

with open(file_path) as f:
    f.write("123")





