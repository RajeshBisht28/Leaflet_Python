import re

class EntityMatcher:
    def __init__(self):
       pass

    def find_matches(self, text, regexList):
        match_list = []
        index_list = []
        counter=-1
        for regex in regexList:
            counter=counter+1
            ent_type = ENTITY_TYPE[counter]           
            for match in re.finditer(regex, text, re.IGNORECASE):
                if(match):
                    match_list.append(match)
                    index_list.append(ent_type)
    
        return match_list, index_list
    
    def match_iteration(self, regex, text):
        for match in re.finditer(regex, text, re.IGNORECASE):
            if(match):
               return match
        return None


    def create_regex_cloud(self, file_path):
        regex_list = []
        text_list = read_file_by_line(file_path)
        for lst in text_list:
            rtext = lst.rstrip()
            reg = create_regex(rtext)                
            regex_list.append(reg)
    
    def create_regex(self, word):    
        spaced_word = r'\s*'.join(list(word))
        pattern = rf'\b\w*{spaced_word}\w*\b'    
        return pattern
