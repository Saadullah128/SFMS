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
🌟 API Documentation
Students
Endpoint	Method	Description
/api/students/	POST	Create new student
/api/students/	GET	    Get student details
/api/students/?department={department}&status={status}  GET   fetch students details with filters
/api/students/{id}/	PUT	Update student
/api/students/{id}/	DELETE	Remove student

Transaction
Endpoint	                  Method	   Description
/api/transactions/payments	   POST	     Create new payment
/api/transactions/payments/{id}	GET	     payment details
