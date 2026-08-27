from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route 1: The Root URL (Redirects immediately to login)
@app.route('/')
def home():
    return redirect(url_for('login'))

# Route 2: The Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user submitted the form
    if request.method == 'POST':
        # Extract the data from the modern form we built
        email = request.form.get('email')
        password = request.form.get('password')
        
        # TODO: Add actual database password checking here later
        print(f"Testing submission: User {email} tried to log in.")
        
        # For now, simulate a successful login by sending them to the dashboard
        return redirect(url_for('dashboard'))
    
    # If it's just a standard page load (GET request), show the HTML template
    return render_template('login.html')

# Route 3: The Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    # debug=True automatically restarts the server when you save Python files
    app.run(debug=True)