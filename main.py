from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Hi bye

#hello

count = 0

@app.route('/')
def index():
    return render_template('sound_demo.html') #ask professor how to make it go from the begin page to the options for portals
    
@app.route('/ancient')
def ancient():
    return render_template('ancient.html')

@app.route('/medieval')
def medieval():
    return render_template('medieval.html')

@app.route('/futuristic')
def futuristic():
    return render_template('futuristic.html')

@app.route('/boss')
def boss():
    return render_template('boss.html')




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




