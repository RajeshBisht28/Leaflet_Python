
import json
from entity_match import EntityMatcher


class JsonEntityResult:
      def __init__(self, entity, synonyms, value, pageno, startindex, endindex):
          self.entity = entity
          self.synonyms = synonyms
          self.value = value
          self.pageno = pageno
          self.startindex = startindex
          self.endindex = endindex

class JsonUtil:
      def __init__(self):
          pass
      
      def load_wordclouds_info(self, file_path):
            objEntmatch = EntityMatcher()
            entity_names = []
            entity_types = []
            with open(file_path, 'r') as file:
                content = file.read()
            data = json.loads(content)     
            for item in data:
                name = item['name']
                ENTITY_NAME.append(name)
                ENTITY_TYPE.append(item['type'])
                rtext = name.rstrip()
                #REGEX_LIST.append(create_regex(rtext))  
        
      def get_json_data(self, file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            data = json.loads(content)     
            return data

      def update_wordclouds_info(self, file_path):
            print(f"jsonpath: {file_path}")
            objEntmatch = EntityMatcher()
            try:
                with open(file_path, 'r') as file:
                     content = file.read()
                data = json.loads(content)   
                for item in data:
                    name = item['name']                
                    rtext = name.rstrip()
                    print(f"rgn: {name}")
                    pregex = objEntmatch.create_regex(rtext)                    
                    item['pattern'] = pregex
                    print("updated pattern")
            except:
                  print("excep")
            finally:
                    updated_json = json.dumps(data, indent=4)
                    with open(file_path, "w") as file:
                         file.write(updated_json)
       

      def json_list_data_write(self, result_list, file_path):
          json_string = json.dumps([result.__dict__ for result in result_list], indent=4)          
          with open(file_path, "w") as file:
               file.write(json_string)
            
    