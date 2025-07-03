# Student Financial Management System (SFMS)

## 🚀 Features
- Student profile management
- Payment processing with QuickBooks integration
- Automated invoice generation
- Dues tracking

## ⚙️ Setup
1. Clone repository:
   ```bash
   git clone https://github.com/Saadullah128/SFME.git
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


