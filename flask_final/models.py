# models.py

from app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    template_name = db.Column(db.String(50), nullable=False, unique=True, default='booking.html')
    # Define other fields...

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    template_name = db.Column(db.String(50), nullable=False, unique=True, default='reservation.html')
    # Define other fields...

class Confirmation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    template_name = db.Column(db.String(50), nullable=False, unique=True, default='confirmation.html')
    # Define other fields...

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), nullable=False, unique=True)
    room_size = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    template_name = db.Column(db.String(50), nullable=False, unique=True, default='room.html')
    # Define other fields...
