# 🎨 Portfolio API

A powerful and clean RESTful API to power a personal portfolio website. Built with Django & Django REST Framework.

---

### 🌐 Live API & Documentation

-   **Base URL:** `https://portfolio-backend-9375.fly.dev/api/`
-   **Swagger Docs:** `https://portfolio-backend-9375.fly.dev/swagger/`
-   **ReDoc:** `https://portfolio-backend-9375.fly.dev/redoc/`

---

### ✨ Core Features

*   **👨‍💼 Profile Management:** API for managing personal information, bio, and contact details.
*   **🛠️ Skills & Technologies:** Endpoints for listing skills and categorizing them.
*   **👔 Work Experience:** Chronological order of your work history.
*   **📂 Projects Showcase:** Highlight your personal and professional projects.
*   **🏆 Rewards & Achievements:** Display your awards and recognitions.
*   **📧 Contact Form:** An endpoint to handle contact form submissions.

---

### 💻 Technology Stack

-   **Backend:** [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/)
-   **Database:** [PostgreSQL](https://www.postgresql.org/)
-   **Testing:** [Pytest](https://docs.pytest.org/)
-   **Deployment:** [Docker](https://www.docker.com/), [Fly.io](https://fly.io/)

---

### 🚀 Getting Started locally

1.  **Clone the project**
    ```bash
    git clone https://github.com/Ahmed3atef/Portfolio-Backend.git
    cd Portfolio-Backend
    ```

2.  **Set up the environment**
    ```bash
    pipenv install --dev
    pipenv shell
    ```

3.  **Set up your `.env` file**
    You'll need to create a `.env` file in the root of the project. A `.env.example` can be provided to show the required variables. For a basic local setup, you'll need at least:
    ```
    SECRET_KEY='a-super-secret-key'
    DEBUG=True
    ```

4.  **Run database migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the server**
    ```bash
    python manage.py runserver
    ```
    Your API is now running at `http://127.0.0.1:8000`!

---

### 🔑 API Endpoints

The main endpoints available are:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/profile-data/` | Retrieves profile information. |
| `GET` | `/api/skills/` | Retrieves a list of skills. |
| `GET` | `/api/experience/` | Retrieves work experience. |
| `GET` | `/api/projects/` | Retrieves projects. |
| `GET` | `/api/rewards/` | Retrieves rewards and achievements. |
| `POST`| `/api/contact/` | Submits the contact form. |

*Full CRUD operations are available for most endpoints for authenticated admins.*

---

### 📁 Project Structure

```
Portfolio-Backend/
├── core/             # Core app for base templates and static files
├── home/             # Main app containing all the portfolio models and API logic
├── portfolioServer/  # Django project settings and main URL configuration
├── manage.py         # Django's command-line utility
├── Pipfile           # Project dependencies
├── Dockerfile        # Docker configuration
└── fly.toml          # Fly.io deployment configuration
```
