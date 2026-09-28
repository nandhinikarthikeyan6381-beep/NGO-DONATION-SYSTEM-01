# NGO Donation System

A beginner-friendly full-stack NGO donation platform built with:
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
- Backend: Python Flask
- Database: SQLite by default (easy first run) / MySQL supported through DATABASE_URL
- Login: Flask-Login
- ORM: Flask-SQLAlchemy
- QR: qrcode
- Maps: Leaflet + OpenStreetMap

## Main roles
1. Donor
2. Volunteer
3. NGO
4. Admin

## Features included
- Separate role registration/login
- Donor product donation
- Money donation amount entry + QR payment demo
- Donor pickup address + map coordinates
- Volunteer dashboard with available pickup alerts
- Volunteer pickup status updates
- NGO dashboard with counts:
  volunteers, onboarded volunteers, received products, pending pickup, remaining distribution
- NGO image upload for distribution proof
- Donor impact page showing how many people benefited
- Volunteer badges and certificate download page
- Contact page
- Responsive navigation and dashboards

## First run

### Windows PowerShell
```powershell
cd ngo_donation_system
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
py app.py
```

Open:
http://127.0.0.1:5000

The first run creates `ngo_donation.db` automatically.

## MySQL
SQLite is used by default so the project runs without MySQL setup errors.

When you are ready for MySQL, create a database named `ngo_donation` and set:

DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/ngo_donation

in `.env`.

## Demo payment note
The QR payment screen is a working demo flow. It records the entered amount and lets you mark the payment as successful. It is NOT a real bank/UPI transaction. For real payments, connect Razorpay/Stripe/another approved payment gateway on the server.

## Important
Do not type Flask console output such as "Running on http://127.0.0.1:5000" into PowerShell. It is output, not a command.
