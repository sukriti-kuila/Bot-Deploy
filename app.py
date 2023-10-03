from flask import Flask
from bot import bot_functionality

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    bot_functionality()
    return 'ROUTE @POST /bot'

@app.route('/up')
def up():
    return 'Server is up and working'

if __name__ == '__main__':
    app.run()