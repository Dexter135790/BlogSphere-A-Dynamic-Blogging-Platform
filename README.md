# BlogSphere: A Dynamic Blogging Platform

A modern, responsive, and feature-rich blog platform developed using Flask, SQLAlchemy, and Bootstrap. This project showcases full-stack development skills with a focus on clean architecture, database management, and user-friendly design.

---

## Features

- **Complete Blog Management:**
  - Create new posts.
  - Edit and update existing content.
  - Delete posts seamlessly.
  - View all posts on a dynamically generated homepage.
- **Rich Content Editor:** Empowered by CKEditor for formatting blog content effortlessly.
- **Responsive UI:** Designed with Bootstrap for seamless viewing on all devices.
- **Robust Database Handling:** Built with SQLAlchemy ORM and SQLite for reliability and performance.
- **Secure Configuration:** Environment variables managed securely using Python-dotenv.

---

## Table of Contents

1. [Demo](#demo)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Project Structure](#project-structure)
5. [Screenshots](#screenshots)

---

## Demo

🌐 **Live Demo:** [https://drive.google.com/file/d/1Dzr41yuWk--9M0bTNJsaxb8T0doZjvhY/view?usp=sharing]

---

## Technologies Used

- **Backend:** Flask, Flask-WTF, Flask-CKEditor
- **Frontend:** Bootstrap 5
- **Database:** SQLite with SQLAlchemy ORM
- **Environment Management:** Python-dotenv

---

## Setup Instructions

Follow these steps to get the project up and running locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/blogsphere.git
   cd blogsphere
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   - Create a `.env` file in the root directory:
     ```env
     SECRET_KEY=your_secret_key
     SQLALCHEMY_DATABASE_URI=sqlite:///posts.db
     ```

5. **Run the Application**

   ```bash
   flask run
   ```

   Open `http://127.0.0.1:5000` in your browser to explore the platform.

---

## Project Structure

```
project/
├── static/        # CSS, JavaScript, Images
├── templates/     # HTML Templates
├── app.py         # Main Flask Application
├── requirements.txt # Python Dependencies
├── .env.example   # Example Environment Variables File
├── README.md      # Project Description
└── .gitignore     # Ignored Files
```

---

## Screenshots

### Homepage

![Alt text](https://github.com/Dexter135790/BlogSphere-A-Dynamic-Blogging-Platform/blob/main/images/home%20page.png)

### Add New Post

![Alt text](https://github.com/Dexter135790/BlogSphere-A-Dynamic-Blogging-Platform/blob/main/images/new%20post.png)

### Edit Post

![Alt text](https://github.com/Dexter135790/BlogSphere-A-Dynamic-Blogging-Platform/blob/main/images/edit%20post.png)

### Blog Detail

![Alt text](https://github.com/Dexter135790/BlogSphere-A-Dynamic-Blogging-Platform/blob/main/images/blog%20detail.png)

---

## Future Enhancements

- Add user authentication and roles.
- Implement search functionality for blog posts.
- Upgrade to PostgreSQL for production databases.
- Deploy the application to platforms like AWS, Heroku, or Vercel.

