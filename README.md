
# DevOps CI/CD Project: CI/CD Pipeline Deployment using Jenkins and Docker

📌 **Project Objective**  
Automate the deployment of a college homepage web app using Docker, Jenkins, and AWS EC2.

---

🛠️ **Tools Used**  

* Git & GitHub – for source code management  
* Jenkins – for continuous integration and deployment  
* Docker – to containerize the static website  
* AWS EC2 – to host Jenkins and run the container  
* Nginx – as the web server  

---

🔧 **Project Workflow**  

**1️⃣ Create Static Website Files**  

* `index.html` – Contains basic website content (Welcome message)  
* `style.css` – Styles and design for the homepage  
* `Dockerfile` – Defines the Docker image and container setup using Nginx to serve the website  

**2️⃣ Push Code to GitHub**  

* A GitHub repository stores the project code  

**3️⃣ Launch EC2 Instance**  

* Ubuntu instance with open ports: 22 (SSH), 80 (HTTP)  
* Install Jenkins and Docker on EC2  

**4️⃣ Setup Jenkins Job**  

* Pulls code from GitHub repository  
* Builds Docker image from project files   
* Deploys the Docker containerized website to EC2 Using Docker-compose

**5️⃣ Access Website**  

* Visit `http://18.204.12.34` to view the deployed college homepage  

---

📂 **Project File Structure**  

```
shubhambavaskar/
├── Dockerfile          # Docker image definition for the web app
├── Jenkinsfile         # Jenkins pipeline configuration for CI/CD
├── README.md           # Project documentation
├── docker-compose.yml  # Defines container services and orchestration
├── index.html          # Main website content
└── style.css           # Styles and design for the web app
```

---

## 🙌 Author

**Shubham Bavaskar**  
*DevOps | AWS | Cloud Enthusiast*  

🔗 [GitHub Profile](https://github.com/shubhambavaskar) | 🔗 [LinkedIn Profile](https://www.linkedin.com/in/shubham-bavaskar-933a75195) | 📧 [Email](mailto:shubhamba97@gmail.com)


![WhatsApp Image 2025-10-18 at 14 02 58_07de631d](https://github.com/user-attachments/assets/cc720040-1ff3-4761-9fe3-b498933b19e3)


![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Python](https://img.shields.io/badge/Language-Python-yellow)
![Jenkins](https://img.shields.io/badge/CI/CD-Jenkins-red)
![AWS](https://img.shields.io/badge/Cloud-AWS-ff9900)
![Status](https://img.shields.io/badge/Build-Automated-success)
