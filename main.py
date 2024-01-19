
# Import necessary modules
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define routes for the application
@app.route('/')
def home():
    # Render the home page (index.html)
    return render_template('index.html')

@app.route('/history')
def history():
    # Render the history page (history.html)
    return render_template('history.html')

@app.route('/geography')
def geography():
    # Render the geography page (geography.html)
    return render_template('geography.html')

@app.route('/culture')
def culture():
    # Render the culture page (culture.html)
    return render_template('culture.html')

@app.route('/tourism')
def tourism():
    # Render the tourism page (tourism.html)
    return render_template('tourism.html')

@app.route('/contact')
def contact():
    # Render the contact page (contact.html)
    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


This Python code generates the main application file (`main.py`) based on the provided design. It defines a Flask application and routes for each of the HTML pages (`index.html`, `history.html`, `geography.html`, `culture.html`, `tourism.html`, and `contact.html`). The routes are mapped to their corresponding HTML pages, ensuring that the application can serve these pages correctly. Additionally, the `if __name__ == '__main__'` block is included to allow the application to run when executed directly as the main program.