import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QPushButton, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from jokedata import fetch_joke
from loadgif import fetch_laugh
from tts_worker import TTSWorker 

api_key = "YOUR ACCESS KEY"

class JokeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        # Set up layout
        self.setWindowTitle('Joke App')
        layout = QVBoxLayout()
        
        # Text display area
        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser)

        # GIF display area
        self.gif_label = QLabel(self)
        layout.addWidget(self.gif_label)
        
        # Button to start telling a joke
        self.joke_button = QPushButton('Tell me a joke!')
        self.joke_button.clicked.connect(self.tell_joke)
        layout.addWidget(self.joke_button)
        
        # Set the layout to the window
        self.setLayout(layout)
        self.setGeometry(300, 300, 600, 400)
        
        # Initialize timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_next_sentence)
        
        self.joke_sentences = []
        self.current_sentence_index = 0
        self.tts_worker = None

    def tell_joke(self):
        # Fetch joke from API
        joke_data = fetch_joke()
        fetch_laugh(api_key)
        
        # Prepare joke sentences
        if joke_data['type'] == 'twopart':
            self.joke_sentences = [joke_data['setup'], joke_data['delivery']]
        else:
            self.joke_sentences = [joke_data['joke']]
        
        self.current_sentence_index = 0
        self.text_browser.clear()
        self.gif_label.clear()
        self.display_next_sentence()
        

    def display_next_sentence(self):
        if self.current_sentence_index < len(self.joke_sentences):
            sentence = self.joke_sentences[self.current_sentence_index]
            
            self.text_browser.append(sentence)
            
            # Estimate TTS duration
            estimated_duration = len(sentence) / 5.0  # Roughly 5 characters per second
            if self.tts_worker:  # If there's already a worker, stop it before starting a new one
                self.tts_worker.stop()
            self.tts_worker = TTSWorker(sentence, estimated_duration)
            self.tts_worker.finished.connect(self.on_tts_finished)
            self.tts_worker.start()
            
            self.current_sentence_index += 1
            
            # Adjust timer interval based on estimated duration
            self.timer.start(int(estimated_duration * 1000))
        else:
            self.timer.stop()
            self.load_gif("laughing_gif.gif")

    def on_tts_finished(self):
        self.display_next_sentence()
    
    def closeEvent(self, event):
        if self.tts_worker:  # Ensure the worker thread is stopped when the application closes
            self.tts_worker.stop()
        event.accept()
    
    def load_gif(self, gif_path):
        self.movie = QMovie(gif_path)
        self.gif_label.setMovie(self.movie)
        self.movie.start()

def main():
    app = QApplication(sys.argv)
    window = JokeApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
