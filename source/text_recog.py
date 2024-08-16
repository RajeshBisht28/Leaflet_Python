import spacy
import re

### Required: 
## pip install spacy
## python -m spacy download en_core_web_sm
 

class LeafletTypeRecog:
    def __init__(self):
       self.nlpmodel = spacy.load("en_core_web_sm")    

    def found_date(self, text, startIndex):
        date_result = ""
        endIndex = len(text)
        try:
            portion_after_endindex = text[startIndex:endIndex]
            #date_pattern = r'(?:^[^a-zA-Z0-9]*)?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{2,4})+'
            date_pattern = r'[^a-zA-Z0-9]*(?:\d{1,2}[-/th|st|nd|rd\s]*)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?[a-z\s,.]*(?:\d{1,2}[-/th|st|nd|rd)\s,]*)+(?:\d{2,4})+'
            match = re.search(date_pattern, portion_after_endindex)        
            if match:        
                start, end = match.span()
                if(start < 3):
                    date_result = match.group()
        except:
                date_result =""          
        finally:
                cleaned_part = re.sub(r'^[^a-zA-Z0-9]+', '', date_result)
                return cleaned_part

    def found_provider(self, text, startIndex):
        result = ""
        endIndex = len(text)
        portion_after_endindex = text[startIndex:endIndex] 
        text_4_words = portion_after_endindex.split()[:4]
        words_text = ' '.join(text_4_words)
        first_4_words = re.sub(r'\s+', ' ', words_text).strip()    
        #print(f"wordsss : {first_4_words}")
        try:               
            nlp = self.nlpmodel ### spacy.load("en_core_web_sm")    
            doc = nlp(first_4_words)
            count=0
            #print("nlp2222")
            for ent in doc.ents:
                count = count + 1            
                #print(f"XXX--- {ent.text} YYY: {ent.label_}")
                if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]:            
                   result = result + " " + ent.text
                elif not (result and result.strip()):
                    continue         
                elif ent.label_ not in ["PERSON", "ORG", "GPE", "LOC"]:
                    break        
        except:
                result =""
        finally:
                #print(f"resulss: {result}")                
                return result
    
    def found_hospital(self, text, start):
        result = ""
        try:
            result = hospital_provider_before(text, start)
            if(len(result) == 0):
                result = hospital_provider_after(text, start)
        except:
               print("except")
        finally:     
               return result

    def found_physician(self, text, startIndex):
        result = ""
        endIndex = len(text)
        portion_after_endindex = text[startIndex:endIndex] 
        text_3_words = portion_after_endindex.split()[:3]
        words_text = ' '.join(text_3_words)
        first_3_words = re.sub(r'\s+', ' ', words_text).strip()        
        try:               
            nlp = self.nlpmodel ### spacy.load("en_core_web_sm")    
            doc = nlp(first_3_words)
            count=0
            for ent in doc.ents:
                count = count + 1
                if ent.label_ in ["PERSON"]:            
                   result = result + " " + ent.text
                elif not (result and result.strip()):
                    continue         
                elif ent.label_ not in ["PERSON"]:
                    break        
        except:
                result =""
        finally:
                return result

    def hospital_provider_after(self, text, startIndex):
        result = ""
        endIndex = len(text)
        portion_after_endindex = text[startIndex:endIndex] 
        text_4_words = portion_after_endindex.split()[:4]
        words_text = ' '.join(text_4_words)
        first_4_words = re.sub(r'\s+', ' ', words_text).strip()        
        try:               
            nlp = self.nlpmodel ### spacy.load("en_core_web_sm")    
            doc = nlp(first_4_words)
            count=0
            for ent in doc.ents:
                count = count + 1
                if ent.label_ in ["ORG", "GPE", "LOC"]:            
                   result = result + " " + ent.text
                elif not (result and result.strip()):
                    continue         
                elif ent.label_ not in ["ORG", "GPE", "LOC"]:
                    break        
        except:
                result =""
        finally:
                return result

    def hospital_provider_before(self, text, startIndex):
        result = ""
        endIndex = len(text)
        portion_after_endindex = text[startIndex-6:startIndex] 
        text_4_words = portion_after_endindex.split()[:4]
        words_text = ' '.join(text_4_words)
        first_4_words = re.sub(r'\s+', ' ', words_text).strip()        
        try:               
            nlp = self.nlpmodel ### spacy.load("en_core_web_sm")    
            doc = nlp(first_4_words)
            count=0
            for ent in doc.ents:
                count = count + 1
                if ent.label_ in ["ORG", "GPE", "LOC"]:            
                   result = result + " " + ent.text
                elif not (result and result.strip()):
                    continue         
                elif ent.label_ not in ["ORG", "GPE", "LOC"]:
                    break        
        except:
                result =""
        finally:
                return result

    def entity_trace_bytype(self, entityType, text, startIndex):
        if(entityType == "date"):
           return self.found_date(text, startIndex)
        if(entityType == "provider"):           
           return self.found_provider(text, startIndex)
        if(entityType == "hospital"):
           return self.found_hospital(text, startIndex)
        if(entityType == "physician"):
           return self.found_physician(text, startIndex)

        return ""
