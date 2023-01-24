from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService
import time

class RadioParadiseMain(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_file_handler('main.paradise.radio.intent')
    def handle_main_paradise_radio(self, message):
        self.speak_dialog('main.paradise.radio')
        self.audio_service = AudioService(self.bus)
        time.sleep(1)
        self.audio_service.play('http://stream.radioparadise.com/mp3-320')
        

        


def create_skill():
    return RadioParadiseMain()



    
    

