from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the ingredient data from the form submission
        ingredients = request.form.get('ingredients')
        
        # Make a request to the Edamam API
        response = requests.get('https://api.edamam.com/search?q=' + ingredients + '&app_id=8f260c92&app_key=c4a3a7db2b2e97703acbfcefc1b4d0c7')
        
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Extract the recipe information
        recipes = data['hits']
        
        # Render the template with the recipe data
        return render_template('index.html', recipes=recipes)
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
