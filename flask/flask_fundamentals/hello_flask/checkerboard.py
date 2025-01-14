# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask, render_template  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<x>/<y>')          # The "@" decorator associates this route with the function immediately following
def checkerboard(x, y):
    return render_template('checkerboard.html', rows=int(x), cols=int(y))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

