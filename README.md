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
-   **Database:** [PostgreSQL](https://www.postgresql.org/) on [Neon](https://neon.tech/)
-   **Testing:** [Pytest](https://docs.pytest.org/)
-   **Deployment:** [Docker](https://www.docker.com/), [Render](https://render.com/)

---

### 🚀 Deploying to Render

This project is configured for deployment on [Render](https://render.com/) using Docker.

1.  **Create a new PostgreSQL database on Neon**. You can follow the instructions on the [Neon website](https://neon.tech/docs/introduction/quickstart).
2.  **Create a new Web Service on Render** and connect it to your GitHub repository.
3.  **Ensure "Docker" is selected** as the environment. Render will automatically detect and build your `Dockerfile`.
4.  **Set the following environment variables** in the Render dashboard:
    -   `SECRET_KEY`: A strong, randomly generated secret key.
    -   `DATABASE_URL`: The connection string for your Neon database. You can find this in your Neon project settings.
    -   `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`: Your Cloudinary credentials.
    -   `MAIL_HOST`, `MAIL_HOST_USER`, `MAIL_HOST_PASSWORD`, `MAIL_PORT`: Your email provider's SMTP credentials.
5.  **The application will be deployed** and available at the URL provided by Render.

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
└── .dockerignore     # Files to ignore when building Docker image
```
