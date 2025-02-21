from flask import Flask, render_template, request, jsonify

import json



app = Flask(__name__)



# Load career data

def load_career_data():

    with open('career_data.json', 'r') as file:

        return json.load(file)



career_data = load_career_data()



@app.route('/')

def index():

    return render_template('index.html', options=list(career_data.keys()))



@app.route('/subcategories', methods=['POST'])

def subcategories():

    data = request.json

    category = data.get('category')

    subcategories = career_data.get(category, {}).get('subcategories', [])

    return jsonify({"subcategories": subcategories})



@app.route('/roadmap', methods=['POST'])

def roadmap():

    data = request.json

    category = data.get('category')

    subcategory = data.get('subcategory')

    roadmap = (

        career_data.get(category, {})

        .get('roadmap', {})

        .get(subcategory, "Roadmap not available")

    )

    return jsonify({"roadmap": roadmap})



if __name__ == "__main__":

    app.run(debug=True)