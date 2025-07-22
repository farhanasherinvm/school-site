# School Project API

A Django RESTful API for managing teachers in a school system, featuring JWT authentication and admin/subadmin permissions.

---

## Features

- Teacher CRUD (Create, Read, Update, Delete)
- JWT authentication (using SimpleJWT)
- Admin-only write access, read access for all
- Search and ordering for teachers
- PostgreSQL database
- Image upload support for teacher profile pictures

---

## Requirements

- Python 3.10+
- PostgreSQL
- pip (Python package manager)

---

## Setup

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/school-project.git
    cd school-project
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv env
    env\Scripts\activate  # On Windows
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure environment variables**

    - Copy `.env.example` to `.env` and set your secret key and other secrets.
    - Example `.env`:
      ```
      SECRET_KEY=your-secret-key
      ```

5. **Configure your database**

    - Edit `school_project/settings.py` with your PostgreSQL credentials.

6. **Run migrations**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server**
    ```sh
    python manage.py runserver
    ```

---

## API Usage

### Authentication

- Obtain JWT token:
    ```
    POST /api/token/
    {
      "username": "your_admin_username",
      "password": "your_password"
    }
    ```
    Response:
    ```json
    {
      "refresh": "...",
      "access": "..."
    }
    ```

- Use the access token in the `Authorization` header for protected endpoints:
    ```
    Authorization: Bearer <access_token>
    ```

### Teacher Endpoints

- **List/Create Teachers:**  
  `GET/POST /teachers/`

- **Retrieve/Update/Delete Teacher:**  
  `GET/PATCH/PUT/DELETE /teachers/<id>/`

- **Search/Ordering:**  
  Use query params, e.g. `/teachers/?search=John&ordering=last_name`

---

## Notes

- Only admin/staff users can create, update, or delete teachers.
- All users can view teacher data.
- For image uploads, use `multipart/form-data` in your requests.

---

## Development

- All migrations are included.
- Static and media files are ignored in git.
- Do not commit your real `.env` file or secrets.

---

## License

MIT License

---
