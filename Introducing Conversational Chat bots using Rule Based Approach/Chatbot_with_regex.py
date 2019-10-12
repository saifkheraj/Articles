import nltk
from nltk.corpus import wordnet
import re

def build_syn():
    ####YOU CAN MAKE THIS PART DYNAMIC ####
    list_words=['hello','describe','role','website','help', 'operate','refund','located']

    dict_syn={}

    for word in list_words:
        synonyms=[]
        for syn in wordnet.synsets(word):
            for lem in syn.lemmas():
                synonyms.append(lem.name())
        dict_syn[word]=set(synonyms)

    return dict_syn


def build_keyword_dict(dict_syn):
    ####YOU CAN MAKE THIS PART DYNAMIC ####
    keywords={}

    keywords['greet']=[]

    for synonym in list(dict_syn['hello']):
        keywords['greet'].append('.*\\b'+synonym+'\\b.*')

    keywords['about_chatbot']=[]

    keywords['about_chatbot'].append('.*who.*you.*')
    for synonym in list(dict_syn['describe']):
        keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byourself\\b'+'.*')
        keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byourself\\b'+'.*')

        keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byou\\b'+'.*')
        keywords['about_chatbot'].append('.*\\b'+synonym+'\\b.*'+'\\byou\\b'+'.*')

    keywords['role']=[]
    for synonym in list(dict_syn['role']):
        keywords['role'].append('.*\\byour.*\\b'+synonym+'\\b.*')


    keywords['about_site']=[]
    for synonym in list(dict_syn['website']):
        keywords['about_site'].append('.*\\b'+synonym+'\\b.*about.*')
        keywords['about_site'].append('.*\\babout.*'+synonym+'\\b.*')


    keywords['site_functionality']=[]
    for synonym_1 in list(dict_syn['operate']):
        for synonym_2 in list(dict_syn['website']):
            keywords['site_functionality'].append('.*\\b'+synonym_1+'\\b.*\\b'+synonym_2+'\\b.*')
            keywords['site_functionality'].append('.*\\b'+synonym_2+'\\b.*\\b'+synonym_1+'\\b.*')

    keywords['refund']=[]
    for synonym in list(dict_syn['refund']):
        keywords['refund'].append('.*\\b'+synonym+'\\b.*')


    keywords['located_in']=[]
    for synonym in list(dict_syn['located']):
        keywords['located_in'].append('.*\\b'+synonym+'\\b.*')

    return keywords

def build_patterns():
    dict_syn=build_syn()
    keywords_dict=build_keyword_dict(dict_syn)

    patterns={}
    for intent, keys in keywords_dict.items():
        patterns[intent]=re.compile('|'.join(keys))

    return patterns

def get_responses():
    responses={
    'greet':'Hello! How can I help you?',
    'about_chatbot':'Hi, My name is Sam. I am here to help you out',
    'role': 'I help people in understanding functionality of our product website. I also assist the end user in purchasing and refunding our product',
    'about_site':'We help people around the world to celebrate important occassions with a special gift.',
    'site_functionality':'Please use the menu on the top to navigate and explore different gift categories. We specialize in anniversary gifts, birthday gifts, and other types of gifts',
    'refund':'Well, we value our customers. You can refund the amount if you return it back within a day. For more information explore our refund section on this link: ____',
    'located_in':'We are based in ______ near _____',
    'default':'Please rephrase...'
    }
    return responses



class Chat:
    def __init__(self, patterns,responses):
        self.patterns=patterns
        self.responses=responses

    def match_intent(self,message):
        matched_intent = None

        for intent,pattern in self.patterns.items():
            if re.search(pattern,message):
                print(intent)
                #print(pattern)
                #print("matched")
                matched_intent=intent
                break
        return matched_intent

    def respond(self,message):
        intent=self.match_intent(message)

        key='default'

        if intent in responses:
            key=intent

        return responses[key]

    def send_message(self,message):
        return self.respond(message)


patterns=build_patterns()
responses=get_responses()

chat = Chat(patterns,responses)

chat.send_message("please tell me how to operate this website")
