from flask import Flask
from playsound import playsound

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Brutus Buckeye. Navigate to /touchdown to celebrate"

@app.route('/touchdown')
def touchdown():
    playsound('BuckeyeBattleCry-Music.mp3')
    return "Touchdown!"
