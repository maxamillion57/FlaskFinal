from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # SQLite database path
db = SQLAlchemy(app)

# Define view functions
def index():
    return render_template('index.html')

def booking():
    return render_template('booking.html')

def reservation():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        check_in = request.form.get('check-in')
        check_out = request.form.get('check-out')
        
        # Assuming you want to pass the reservation data to the confirmation page
        return redirect(url_for('confirmation', name=name, email=email, check_in=check_in, check_out=check_out))
    else:
        return render_template('reservation.html')

def room_list():
    # Sample room data (replace with your actual data)
    rooms = [
        {"name": "Standard Room", "type": "Single", "price": "$100"},
        {"name": "Deluxe Room", "type": "Double", "price": "$150"},
        {"name": "Suite", "type": "Luxury", "price": "$250"}
    ]
    return render_template('rooms.html', rooms=rooms)

def confirmation():
    return render_template('confirmation.html')

# Add routes using add_url_rule()
app.add_url_rule('/', 'index', index)
app.add_url_rule('/booking', 'booking', booking)
app.add_url_rule('/reservation', 'reservation', reservation, methods=['GET', 'POST'])
app.add_url_rule('/rooms', 'room_list', room_list)
app.add_url_rule('/confirmation', 'confirmation', confirmation)

if __name__ == '__main__':
    app.run(debug=True)
