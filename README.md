# Student Financial Management System (SFMS)

## 🚀 Features
- Student profile management
- Payment processing with QuickBooks integration
- Automated invoice generation
- Dues tracking

## ⚙️ Setup
1. Clone repository:
   ```bash
   git clone https://github.com/Saadullah128/SFMS.git
   cd SFMS


# Setting up Virtual Environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows


# Install Dependencies
pip install -r requirements.txt

# Configure Environment
cp .env.sample .env
# Edit .env with your credentials

# Run Migrations
python manage.py migrate


# Running the Server
python manage.py runserver

# API Documemtation

-----Student-----

create student
POST http://127.0.0.1:8000/api/students/
JSON 
{  "name" : "ather",
    "email": "ather@example.com",
    "department": "CS",
    "enrollment_date": "2025-01-01",
    "status": "Active",
    "fee_due": 4000.00
    }

student list
GET http://127.0.0.1:8000/api/students/

student detail
GET http://127.0.0.1:8000/api/students/?department=CS&status=Active

update student
PUT http://127.0.0.1:8000/api/students/4/
JSON
{
    "name": "Aalyan",
    "email": "aalyan_examplr@example.com",
    "department": "CS",
    "enrollment_date": "2025-01-01",
    "status": "Inactive",
    "fee_due": 0.00
}

delete student
DELETE http://127.0.0.1:8000/api/students/7/


-----Transaction-----

create transaction
POST http://127.0.0.1:8000/api/transactions/payments/
JSON 
{
    "student": 8,
    "amount": "200.00",
    "method": "Online",
    "remarks": "Tuition fee"
}

transaction detail
GET http://127.0.0.1:8000/api/transactions/payments/1
