# Flask College Management App -- DevOps CI/CD Project

📌 **Project Objective**\
Build & deploy a **Flask + MySQL College Web App** using **Docker,
Docker‑Compose, Jenkins (CI/CD), and AWS EC2**.

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Category          Tools
  ----------------- -------------------------
  Frontend          HTML, CSS
  Backend           Python Flask
  Database          MySQL
  CI/CD             Jenkins
  Container         Docker & Docker‑Compose
  Cloud             AWS EC2
  Version Control   Git & GitHub

------------------------------------------------------------------------

## 🚀 Features

-   Student Registration (Name, Email, Course)
-   MySQL DB storage
-   View all registered students
-   Containerized deployment
-   CI/CD automated pipeline pushing to Docker Hub & deploying on EC2

------------------------------------------------------------------------

## 📂 Project Structure

    flask-college-app/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .env.example
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── register.html
    │   └── students.html
    └── static/
        └── style.css

------------------------------------------------------------------------

## ⚙️ Run App Locally

``` bash
pip install -r requirements.txt
python app.py
```

### ✅ Access App

http://localhost:5000

------------------------------------------------------------------------

## 🐳 Docker & Compose Commands

### Build & Run

``` bash
docker compose up --build
```

### Stop

``` bash
docker compose down
```

------------------------------------------------------------------------
## 🐳 Docker Hub Upload Steps

``` bash
docker login
docker build -t username/flask-college-app .
docker push username/flask-college-app
```

------------------------------------------------------------------------

## ☁️ AWS EC2 Deployment Guide

### ✅ Steps

1.  Launch Ubuntu EC2
2.  Install Docker & Docker‑Compose
3.  Clone project or pull image from Docker Hub
4.  Run

``` bash
docker compose up -d
```

### Security Group Ports

  Port   Purpose
  ------ ------------------
  22     SSH
  5000   Flask App
  3306   MySQL (optional)

------------------------------------------------------------------------

## 🖼️ Architecture Diagram
![WhatsApp Image 2025-11-05 at 18 06 46_8c6d6085](https://github.com/user-attachments/assets/89ff73e7-d47c-4f00-ac6d-54141f735c0a)
------------------------------------------------------------------------
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Python](https://img.shields.io/badge/Language-Python-yellow)
![Jenkins](https://img.shields.io/badge/CI/CD-Jenkins-red)
![AWS](https://img.shields.io/badge/Cloud-AWS-ff9900)
![Status](https://img.shields.io/badge/Build-Automated-success)


## 🎤 Interview Explanation

> "I created a Flask‑MySQL college web app and automated its deployment
> using Docker, Docker Hub, and Jenkins.\
> When I push code to GitHub, Jenkins pulls the code, builds a Docker
> image, pushes it to Docker Hub, and automatically deploys the updated
> container on AWS EC2 using SSH.\
> This demonstrates CI/CD automation, containerization, and cloud
> deployment skills."

------------------------------------------------------------------------
## 🙌 Author

**Shubham Bavaskar**  
*DevOps | AWS | Cloud Enthusiast*  

🔗 [GitHub Profile](https://github.com/shubhambavaskar) | 🔗 [LinkedIn Profile](https://www.linkedin.com/in/shubham-bavaskar-933a75195) | 📧 [Email](mailto:shubhamba97@gmail.com)




------------------------------------------------------------------------
