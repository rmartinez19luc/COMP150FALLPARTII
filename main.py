import random

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

count = 0

# Global variables for game state (e.g., player health, boss health)
player_health = 100
boss_health = 120


# Cyborg Boss Battle Logic (For simplicity, kept as a function)
def cyborg_boss_battle(action):
    global player_health, boss_health

    if action == "attack":
        damage = random.randint(10, 20)
        boss_health -= damage
        return f"You strike the Cyborg Boss for {damage} damage!"

    elif action == "defend":
        return "You brace for the boss's attack!"

    elif action == "run":
        return "You run away from the fight!"

    # Cyborg Boss attack (Random damage)
    if boss_health > 0:
        boss_damage = random.randint(5, 15)
        player_health -= boss_damage
        return f"The Cyborg Boss strikes you for {boss_damage} damage!"

    return ""


@app.route('/')
def index():
    return render_template('sound_demo.html')


@app.route('/portals')
def portals():
    return render_template('portals.html')


@app.route('/ancient')
def ancient():
    return render_template('ancient.html')


@app.route('/ancient_minigame')
def ancient_minigame():
    return render_template('ancient_minigame.html')


@app.route('/medieval')
def medieval():
    return render_template('medieval.html')

@app.route('/medieval_minigame')
def medieval_minigame():
    return render_template('medieval_minigame.html')

@app.route('/futuristic')
def futuristic():
    return render_template('futuristic.html')

@app.route('/futuristic_minigame')
def futuristic_minigame():
    return render_template('futuristic_minigame.html')

@app.route('/cyborg_boss')
def cyborg_boss():
    return render_template('cyborg_boss.html')

@app.route('/Boss')
def Boss():
    return render_template('Boss.html')

@app.route('/boss_minigame')
def boss_minigame():
    return render_template('boss_minigame.html')

@app.route('/bertak_boss')
def bertak_boss():
    return render_template('bertak_boss.html')

@app.route('/Boss')
def boss():
    # Display current health states for both player and boss
    return render_template('Boss.html', player_health=player_health, boss_health=boss_health)


@app.route('/futuristic_minigame')
def minigame():
    return render_template('futuristic_minigame.html')


@app.route('/battle', methods=['POST'])
def battle():
    global player_health, boss_health
    action = request.json.get('action')  # Get action from the POST request

    result = cyborg_boss_battle(action)  # Process the action

    # Check if the player or the boss has been defeated
    if player_health <= 0:
        result += " You have been defeated by the Cyborg Boss!"
    elif boss_health <= 0:
        result += " You have defeated the Cyborg Boss!"

    # Return battle status and updated healths
    return jsonify({
        'result': result,
        'player_health': player_health,
        'boss_health': boss_health
    })


@app.route('/increment', methods=['POST'])
def increment():
    global count
    count += 1
    return jsonify({'count': count})


@app.route('/flip_case', methods=['POST'])
def flip_case():
    text = request.json['text']
    flipped_text = ''.join(c.lower() if c.isupper() else c.upper() for c in text)
    return jsonify({'flipped_text': flipped_text})


if __name__ == '__main__':
    app.run(debug=True)
