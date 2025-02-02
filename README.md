# Multilingual FAQ System

## Features
- ✨ Rich text editor (WYSIWYG) using CKEditor 5
- 🌐 Automatic translation to Hindi and Bengali
- 🔄 REST API with language selection
- ⚡ Caching for improved performance
- 🎨 User-friendly admin interface

## Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `.\venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## API Usage
### Get FAQs in different languages:
1. English (default):
   ```bash
   GET http://localhost:8000/api/faqs/
   ```

2. Hindi:
   ```bash
   GET http://localhost:8000/api/faqs/?lang=hi
   ```

3. Bengali:
   ```bash
   GET http://localhost:8000/api/faqs/?lang=bn
   ```

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request