![image](https://github.com/user-attachments/assets/e849d4c7-4e16-4a7a-92ea-2ed9bdef7dac)

![image](https://github.com/user-attachments/assets/a0efe00f-50a4-423d-aa9c-55bbd9593d8d)

![image](https://github.com/user-attachments/assets/92ae501d-7214-4cf2-a1d6-b44e038b79b9)

This is a blog website made using Django and MySQL. Users can sign up, log in, and write blogs. They can also like posts and leave comments. The site also includes a backend API and an admin panel to manage blogs and users.

🚀 Features
✅ User registration and login using JWT (JSON Web Token)

✅ Create, edit, and delete blog posts

✅ Like and comment on blog posts

✅ View all blog posts with a "Read More" feature

✅ Admin panel to manage users and blogs

✅ REST API with pagination

✅ Clean and responsive UI using Django templates

✅ MySQL used for storing data

🛠️ Technologies Used
Python 🐍

Django 🌐

Django REST Framework 🔗

MySQL 🛢️

HTML & CSS 🎨

JWT Authentication 🔐

📂 How to Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/blog-project.git
cd blog-project
2. Set up a Virtual Environment
bash
Copy
Edit
python -m venv env
env\Scripts\activate  # Windows
3. Install the Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Configure MySQL
Make sure MySQL is running.

Create a database (e.g., blog_db).

In settings.py, update the database section:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5. Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6. Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
7. Run the Server
bash
Copy
Edit
python manage.py runserver
Go to http://127.0.0.1:8000/ in your browser.

📬 API Endpoints
POST /api/token/ – Get JWT token

POST /api/token/refresh/ – Refresh token

GET /api/posts/ – List blog posts (with pagination)

POST /api/posts/ – Create new blog post

PUT /api/posts/<id>/ – Update a post

DELETE /api/posts/<id>/ – Delete a post
