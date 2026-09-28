from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:nandhini2007@localhost/ngo_donation_system"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    donation_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(30), default="Pending")
@app.route("/donations", methods=["GET"])
def get_donations():
    donations = Donation.query.all()

    result = []

    for donation in donations:
        result.append({
            "id": donation.id,
            "donor_name": donation.donor_name,
            "donation_type": donation.donation_type,
            "amount": donation.amount,
            "description": donation.description,
            "status": donation.status
        })

    return result

    def __repr__(self):
        return f"<User {self.email}>"

@app.route("/")
def home():
    return "NGO Donation System Backend is Connected to MySQL!"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)