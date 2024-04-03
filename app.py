# app.py
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ['rock', 'paper', 'scissors']
    player_choice = request.json['choice']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result = 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = 'You win!'
    else:
        result = 'You lose!'
    
    return jsonify({'player_choice': player_choice, 'computer_choice': computer_choice, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
