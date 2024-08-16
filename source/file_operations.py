import os
import re
from pathlib import Path

class File:
    def __init__(self):
        pass
    
    def write_to_file(self, file_path, content):  
        with open(file_path, 'w') as f:
             f.write(content)

    def write_append_to_file(self, file_path, content):
        filename = file_path
        if not os.path.exists(filename):
            outfile_path = Path(filename)   
            outfile_path.touch()

        content = content + " \n"
        with open(filename, 'a') as f:
            f.write(content)

    def read_file_by_line(self, file_path):
        line_text = []
        with open(file_path, 'r') as file:
            for line in file:
                line_text.append(line)
        return line_text

    def list_directory_files(self, dir_path, extension):
        flist = []   
        for filename in os.listdir(dir_path):
            if filename.endswith(extension):
                filepath = os.path.join(dir_path, filename)
                flist.append(filepath)
        return flist

    def page_text_number(self, file_path):
        content_list = self.read_file_by_line(file_path)
        filecontent = ' '.join(content_list)
        filterContent = re.sub(r'\s+', ' ', filecontent)
        pnumber = 0
        file_without_extension = Path(os.path.basename(file_path)).stem    
        match = re.search(r'\d+', file_without_extension)
        if match:
           pnumber = int(match.group())
           
        return pnumber, filterContent

        
    def read_file_path(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    