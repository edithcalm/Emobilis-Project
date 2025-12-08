# EveShield - GBV Support, Legal Aid & Mental Health Web Application

EveShield is a comprehensive Django web application designed to support survivors of gender-based violence (GBV) by providing:
- Anonymous GBV reporting system
- Legal aid directory
- Mental health support directory
- Rule-based chatbots for legal and mental health support
- Educational resources
- Emergency contacts

## 🎯 Project Alignment

This project aligns with:
- **SDG 5**: Gender Equality
- **SDG 3**: Good Health and Well-being
- **SDG 16**: Peace, Justice and Strong Institutions

## 🛠️ Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: HTML + Bootstrap 5
- **Database**: SQLite (default)
- **Template Engine**: Django Templates

## 📁 Project Structure

```
EveShieldProject/
├── accounts/          # Authentication (signup, login, profile)
├── reports/           # Anonymous GBV reporting system
├── lawyers/           # Legal aid directory
├── mental_health/     # Therapists directory + mental health chatbot
├── chatbot/           # Legal aid chatbot
├── resources/         # Educational resource library
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # User uploads (reports, files)
├── manage.py
└── EveShieldProject/  # Project settings
```

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 2. Installation

#### Step 1: Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 2: Install Django

```bash
pip install django
```

#### Step 3: Navigate to project directory

```bash
cd EveShieldProject
```

#### Step 4: Run migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 5: Create superuser (Admin account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. You'll need this to access the admin dashboard.

#### Step 6: Load seed data (Optional but recommended)

Open Django shell:
```bash
python manage.py shell
```

Then copy and paste the contents of `seed_data.py` into the shell, or run:
```bash
python manage.py shell < seed_data.py
```

This will populate:
- Sample lawyers in the directory
- Sample therapists in the directory
- Sample educational resource articles

#### Step 7: Run the development server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 📱 Application Features

### 1. Authentication System
- User signup and login
- Password hashing (Django default security)
- User profile page
- **Note**: Only the reporting system allows anonymous submissions

### 2. Anonymous GBV Reporting
- Submit reports anonymously (no login required)
- Fields: type of violence, location, details, incident date, file upload
- Status tracking: Pending → Reviewed → In Progress → Resolved
- Admin dashboard to view and manage reports

### 3. Legal Aid Directory
- Searchable directory of lawyers and firms
- Filter by county
- Contact information: phone, WhatsApp, email
- Specialization areas
- Responsive card-based UI

### 4. Mental Health Support Directory
- Directory of therapists, psychologists, and counselors
- Filter by county
- Specialty areas
- Contact information
- Links to mental health chatbot

### 5. Legal Aid Chatbot
- Rule-based chatbot
- Answers common legal questions:
  - How to file a P3 form
  - Getting legal aid
  - Reporting GBV
  - Your rights
  - Protection orders
  - Evidence collection
  - Court processes
- Chat UI with Bootstrap styling

### 6. Mental Health Chatbot
- Rule-based chatbot
- Provides:
  - Grounding exercises
  - Self-care tips
  - Information about professional help
- **Important**: Does NOT provide clinical diagnosis
- Links to therapist directory

### 7. Educational Resource Library
- Articles on:
  - Know Your Rights
  - How to File a Complaint
  - Emergency Steps
  - Protection Orders
  - Self-Care
- Searchable and filterable by category

### 8. Emergency Contacts Page
- National GBV hotline (1195)
- Police emergency (999)
- Child helpline (116)
- Quick access to lawyer and therapist directories

### 9. Admin Dashboard
- Django admin interface
- Manage all models:
  - GBV Reports
  - Lawyers
  - Therapists
  - Resource Articles
  - User Profiles

## 🔐 Admin Access

1. Create a superuser (if not done already):
   ```bash
   python manage.py createsuperuser
   ```

2. Access admin panel:
   - URL: `http://127.0.0.1:8000/admin/`
   - Use your superuser credentials

3. Admin Dashboard for Reports:
   - URL: `http://127.0.0.1:8000/reports/admin/dashboard/`
   - Only accessible to staff users

## 📝 Key URLs

- Home: `/`
- Sign Up: `/accounts/signup/`
- Login: `/accounts/login/`
- Profile: `/accounts/profile/`
- Submit Report: `/reports/submit/`
- Admin Dashboard: `/reports/admin/dashboard/`
- Legal Aid Directory: `/lawyers/`
- Mental Health Directory: `/mental-health/`
- Legal Chatbot: `/chatbot/legal/`
- Mental Health Chatbot: `/mental-health/chatbot/`
- Resources: `/resources/`
- Emergency Contacts: `/resources/emergency-contacts/`
- Django Admin: `/admin/`

## 🎨 UI/UX Features

- Fully responsive (mobile-first design)
- Clean, modern Bootstrap 5 design
- Gradient navbar and footer
- Card-based layouts
- Chat bubble UI for chatbots
- Dashboard-style admin pages
- Light theme throughout

## 🔒 Security Features

- Django's built-in password hashing
- CSRF protection
- Anonymous reporting (no user tracking)
- Admin-only access to reports dashboard
- File upload security (media files)

## 📊 Database Models

### Accounts App
- `UserProfile`: Extended user profile

### Reports App
- `GBVReport`: Anonymous GBV incident reports

### Lawyers App
- `Lawyer`: Legal aid directory entries

### Mental Health App
- `Therapist`: Mental health professional directory

### Resources App
- `ResourceArticle`: Educational articles

## 🧪 Testing

To test the application:

1. **Anonymous Reporting**: Visit `/reports/submit/` (no login required)
2. **User Features**: Create an account and login
3. **Admin Features**: Login as superuser and access `/reports/admin/dashboard/`
4. **Chatbots**: Test both legal and mental health chatbots
5. **Directories**: Browse lawyers and therapists directories

## 📦 Dependencies

- Django 5.2.8
- Bootstrap 5.3.0 (via CDN)
- Bootstrap Icons 1.11.0 (via CDN)

## 🚨 Important Notes

1. **Production Deployment**: 
   - Change `SECRET_KEY` in settings.py
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use a production database (PostgreSQL recommended)
   - Set up proper static file serving
   - Configure media file storage

2. **File Uploads**: 
   - Files are stored in `media/reports/` directory
   - Ensure proper file size limits in production

3. **Chatbots**: 
   - Both chatbots are rule-based (no AI/ML)
   - Responses are stored in Python dictionaries
   - Can be easily extended with more Q&A pairs

4. **Anonymous Reporting**: 
   - Reports are completely anonymous
   - No user association is stored
   - Only admins can view reports

## 🤝 Contributing

This is a complete, production-ready application. To extend it:

1. Add more chatbot responses in `chatbot/views.py` and `mental_health/views.py`
2. Add more resource articles through Django admin
3. Customize templates in `templates/` directory
4. Add more models and features as needed

## 📄 License

This project is created for educational and social good purposes, aligned with SDG goals.

## 🆘 Support

For issues or questions:
- Check the Django documentation: https://docs.djangoproject.com/
- Review the code comments in each file
- Check the admin panel for data management

## ✅ Checklist for First Run

- [ ] Install Django
- [ ] Run migrations
- [ ] Create superuser
- [ ] Load seed data
- [ ] Test anonymous reporting
- [ ] Test user signup/login
- [ ] Test admin dashboard
- [ ] Test chatbots
- [ ] Browse directories

---

**Built with ❤️ for GBV survivors and support organizations**

