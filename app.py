from flask import Flask
from bot import bot_functionality

app = Flask(__name__)

@app.route('/bot')
def bot():
    bot_functionality()

@app.route('/up')
def up():
    return 'Server is up and working'

if __name__ == '__main__':
    app.run()
