from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService

class RadioParadiseMain(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.audio_service = AudioService(self.bus)
        self.audio_service.play(' http://stream.radioparadise.com/mp3-320')

    @intent_file_handler('main.paradise.radio.intent')
    def handle_main_paradise_radio(self, message):
        self.speak_dialog('main.paradise.radio')
        

        


def create_skill():
    return RadioParadiseMain()



    
    

