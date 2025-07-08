# 📝 To-Do App API

🔧 **Description**

This project is a **simple yet robust To-Do REST API** built with **Django and Django REST Framework**, allowing users to manage tasks and notes efficiently.<br />
✅ Implements **Task** and **Note** models with user associations <br />
✅ Provides **CRUD API endpoints** secured with authentication <br />
✅ Includes **Dockerfile** for containerized deployment <br />
✅ Integrated with **Jenkins CI/CD pipeline** for automated testing, building, and deployment on AWS and Linode instances

---

## 📂 Project Structure

```
project/
├── core/                   # Django project settings
├── tasks/                  # App with models, views, serializers
│   ├── models.py           # Task and Note models
│   └── views.py            # ViewSets for APIs
├── todoapp/                # Django app configuration
├── .dockerignore           # Docker ignore file
├── .gitignore              # Git ignore file
├── Dockerfile              # Docker build configuration
├── jenkinsfile             # Jenkins CI/CD pipeline
├── manage.py               # Django management script
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── setup.py                # Setup script for sdist building
```

---

## 💡 Features

✨ **Task API**: Create, read, update, and delete tasks linked to authenticated users <br />
✨ **Note API**: Manage user notes with optional image uploads <br />
✨ **Authentication**: Secures all endpoints using Django REST Framework’s authentication system <br />
✨ **Testing**: Includes test cases for task endpoints using Pytest <br />
✨ **CI/CD Integration**: Jenkins pipeline to test, build Docker images, and deploy to AWS and Linode <br />
✨ **Dockerized**: Ready to build and run in containerized environments

---

## 🛠️ Technologies Used

* 🐍 **Python 3.12**
* 🌐 **Django & Django REST Framework**
* 🐳 **Docker**
* ⚙️ **Jenkins**
* ☁️ **AWS EC2**
* ☁️ **Linode**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AHMED0130/your-repo.git
cd your-repo
```

### 2️⃣ Build and run with Docker

```bash
docker build -t todo-app .
docker run -d -p 8000:8000 todo-app
```

The API will be accessible at **[http://localhost:8000](http://localhost:8000)**.

### 3️⃣ Running Tests

If running locally:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
pytest
```

---

## ✅ API Endpoints Overview

| Endpoint     | Methods          | Description                     |
| ------------ | ---------------- | ------------------------------- |
| /tasks/      | GET, POST        | List and create tasks           |
| /tasks/{id}/ | GET, PUT, DELETE | Retrieve, update, delete a task |
| /notes/      | GET, POST        | List and create notes           |
| /notes/{id}/ | GET, PUT, DELETE | Retrieve, update, delete a note |

🔒 **All endpoints require authentication.**

---

## 📌 CI/CD Pipeline Overview

✔️ **Test**: Runs Pytest for endpoint validation <br />
✔️ **Build**: Builds Docker image tagged with build number <br />
✔️ **Push**: Pushes image to Docker Hub <br />
✔️ **Deploy**: Deploys containers to AWS EC2 and Linode instances via SSH

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

### ✨ Author

Ahmed Elshnawy
[LinkedIn](https://www.linkedin.com/in/ahmed-elshnawy-9132ba2a4)
