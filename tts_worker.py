import os
import random
from gtts import gTTS
from playsound import playsound
from PyQt5.QtCore import QThread, pyqtSignal

class TTSWorker(QThread):
    finished = pyqtSignal()

    def __init__(self, text, duration):
        super().__init__()
        self.text = text
        self.duration = duration

    def run(self):
        # Convert text to speech
        acc = random.choice(['com.au','co.uk','us','ca','co.in'])
        tts = gTTS(text=self.text, lang='en', tld=acc)
        filename = 'temp.mp3'
        tts.save(filename)
        
        playsound(filename)
        
        # Emit signal when finished
        os.remove(filename)
        self.finished.emit()
    
    def stop(self):
        self.is_running = False
        self.quit()  # Request the thread to exit
        self.wait()



