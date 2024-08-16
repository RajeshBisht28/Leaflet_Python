
import os
import json
from file_operations import File
from json_util import JsonUtil
from json_util import JsonEntityResult
from entity_match import EntityMatcher
from text_recog import LeafletTypeRecog

### virtual environment: leaflet_ent\Scripts\activate
###

def process_run(dir_path):
    # Collect all text files text and its page number. 
    # page_list : file page number
    # page_text: text of the page.
    # in find matches : using iterator 
    page_list, page_text = collecting_page_data(dir_path)
    regex_list = REGEX_LIST
    
    for tokenIndex in range(len(page_text)):
        main_str = page_text[tokenIndex]
        matches_collection, index_collection = find_matches(main_str, regex_list)
        indexCount = -1
        for match in matches_collection:
            indexCount = indexCount + 1
            #print(f"vvv: {index_collection[indexCount]}")                                
            if(match):
               etype = index_collection[indexCount]
               start, end = match.span()
               entity_value = entity_trace_bytype(etype, main_str, end)
               cont_txt = f"page: {page_list[tokenIndex]} Matched: {match.group()} value: {entity_value} start {start} end {end}"
               write_or_append_to_file(RESULT_FILE, cont_txt)


def run_process(dir_path, file_path):
    jsonObj.update_wordclouds_info(file_path)
    json_data = jsonObj.get_json_data(file_path)
    page_list, page_text = collecting_page_data(dir_path)
    print("after collecting data")
    page_number = 0
    for tokenIndex in range(len(page_text)):
         page_number = page_list[tokenIndex]
         text = page_text[tokenIndex]
         for data_item in json_data:
             regex = data_item['pattern']
             out_data = find_match_results(text, page_number, regex, data_item['type'], data_item['name'])
             if(out_data != None):
                RESULT_ENTITY.append(out_data)
    
    

def find_match_results(text, page_number, regex, etype, synonyms):
    objMatcher = EntityMatcher()
    match = objMatcher.match_iteration(regex, text)
    if(match == None):
      return None
    if(match):
        start, end = match.span()
        entity_value = objTextRecog.entity_trace_bytype(etype, text, end)
        response = JsonEntityResult(etype, synonyms, entity_value, page_number, start, end)
        return response

    return None    


def collecting_page_data(dir_path):
    files_list = FileObj.list_directory_files(dir_path, ".txt")
    text_list = []
    page_list = []
    for fpath in files_list:
        page_number, page_text = FileObj.page_text_number(fpath)
        text_list.append(page_text)
        page_list.append(page_number)

    return page_list, text_list

def test(file_path):
    fileObj = File(file_path)
    fileObj.write_append_to_file("vvvvvv")


if __name__ == '__main__':
   RESULT_ENTITY = []
   FileObj = File()
   jsonObj = JsonUtil()
   objTextRecog = LeafletTypeRecog()
   out_dir = r"E:\DELETES_9000\IndexingPython\resultfiles"
   dir_path = r"E:\\DELETES_9000\\IndexingPython\\datafiles"
   file_path = r"E:\\DELETES_9000\\IndexingPython\\jsonfiles\\word_infos.json"
   run_process(dir_path, file_path)
   print("Results___________")
   result_path = os.path.join(out_dir, "abc.json")

   json_string = json.dumps([result.__dict__ for result in RESULT_ENTITY], indent=4)
   print(json_string)
   jsonObj.json_list_data_write(RESULT_ENTITY, result_path)
   # print(RESULT_ENTITY)
   ### jsonObj.update_wordclouds_info(file_path)
  # test(r"E:\\DELETES_9000\\dddd\\abc.txt")
   
