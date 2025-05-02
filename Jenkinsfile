pipeline {
    agent  { label "shubham" }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/shubhambavaskar/DevOps-CI-CD-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t college-web-app .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker tag college-web-app $DOCKER_USER/college-web-app:latest'
                    sh 'docker push $DOCKER_USER/college-web-app:latest'
                }
            }
        }

        stage('Deploy via Ansible') {
            steps {
                sh 'ansible-playbook -i hosts deploy.yml'
            }
        }
    }
}

