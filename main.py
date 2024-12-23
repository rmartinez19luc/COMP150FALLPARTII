import sqlite3
import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 't32%4p7^'  # Replace with a secure and unique key


# Initialize the database
def init_db():
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_state (
                        user_id INTEGER,
                        state TEXT,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    )''')
    conn.commit()
    conn.close()

init_db()








player_health = 100
boss_health = 100



@app.route('/cyborg_battle', methods=['POST'])
def cyborg_battle():
    global player_health, boss_health

    # Get action from the request
    action = request.json.get("action")
    result = ""  # Initialize the result as an empty string

    if action == "attack":
        damage = random.randint(10, 20)
        boss_health -= damage
        result = f"You strike the Boss for {damage} damage!"

    # Cyborg Boss attack (Random damage)
    if boss_health > 0:
        boss_damage = random.randint(5, 15)
        player_health -= boss_damage
        result += f" The Boss strikes you for {boss_damage} damage!" 

    # Return the updated battle state
    return jsonify({
        "player_health": player_health,
        "boss_health": boss_health,
        "message": result
    })

if __name__ == '__main__':
    app.run(debug=True)

# Define routes
count = 0


@app.route('/')
def index():
    return render_template('sound_demo.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('game_data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('portals'))  # Redirect to the portals page after successful login
        else:
            return "Invalid username or password", 403
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        try:
            conn = sqlite3.connect('game_data.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('portals'))  # Redirect to the portals page after successful registration
        except sqlite3.IntegrityError:
            return "Username already taken", 400
    return render_template('register.html')


@app.route('/portals')
def portals():
    return render_template('portals.html')


@app.route('/ancient')
def ancient():
    return render_template('ancient.html')


@app.route('/ancient_minigame')
def ancient_minigame():
    return render_template('ancient_minigame.html')

@app.route('/ancient_snakeboss')
def ancient_snakeboss():
    return render_template('ancient_snakeboss.html')

@app.route('/medieval')
def medieval():
    return render_template('medieval.html')

@app.route('/medieval_minigame')
def medieval_minigame():
    return render_template('medieval_minigame.html')

@app.route('/medieval_knightboss')
def medieval_knightboss():
    return render_template('medieval_knightboss.html')

@app.route('/futuristic')
def futuristic():
    return render_template('futuristic.html')

@app.route('/futuristic_minigame')
def futuristic_minigame():
    return render_template('futuristic_minigame.html')

@app.route('/cyborg_boss')
def cyborg_boss():
    return render_template('cyborg_boss.html')

@app.route('/Finalscreen.html')
def Finalscreen():
    return render_template('Finalscreen.html')

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
