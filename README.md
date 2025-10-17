# DevOps CI/CD Project: CI/CD Pipeline Deployment using Jenkins and Docker 

## 📌 Project Objective
Automate the deployment of a college homepage web app using Docker, Jenkins, and AWS EC2.

---

## 🛠️ Tools Used
- **Git & GitHub** – for source code management
- **Jenkins** – for continuous integration and deployment
- **Docker** – to containerize the static website
- **AWS EC2** – to host Jenkins and run the container
- **Nginx** – as the web server

---

## 🔧 Project Workflow

1. **Create Static Website Files**
   - `index.html`: Contains basic website content (Welcome message)
   - `style.css`: Styles and design for the homepage
   - `Dockerfile`: Defines the Docker image and container setup using Nginx to serve the website

2. **Push code to GitHub**
   - A GitHub repository stores the project code

3. **Launch EC2 Instance**
   - Ubuntu instance with open ports: 22, 80
   - Install Jenkins, and Docker on EC2

4. **Setup Jenkins Job**
   - Pulls code from GitHub repository
   - Triggers Ansible playbook for server setup and deployment
   - Deploys the Docker containerized website to EC2

5. **Access Website**
   - Visit `http://` to view the deployed college homepage

---
## 📂 Project File Structure
```bash
shubhambavaskar/
├── Dockerfile          # Docker image definition for the web app
├── Jenkinsfile         # Jenkins pipeline configuration for CI/CD
├── README.md           # Project documentation
├── docker-compose.yml  # Defines container services and orchestration
├── index.html          # Main website content
└── style.css           # Styles and design for the web app
      
---


---

## 🙌 Author

**Shubham Bavaskar**  
*DevOps | AWS | Cloud Enthusiast*  

🔗 [GitHub Profile](https://github.com/shubhambavaskar) | 🔗 [LinkedIn Profile](https://www.linkedin.com/in/shubham-bavaskar-933a75195) | 📧 [Email](mailto:shubhamba97@gmail.com)

