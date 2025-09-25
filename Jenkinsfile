pipeline {
    agent { label 'shubham' }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning code from Git"
                git url: "https://github.com/shubhambavaskar/DevOps-CI-CD-project.git", branch: "main"
                echo "Code cloning successful..."
            }
        }

        stage('Build') {
            steps {
                echo "Building project"
                sh 'docker build -t nginx:alpine .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "Pushing image to DockerHub"
                withCredentials([usernamePassword(
                    credentialsId: 'DockerHubCred',  // <-- Correct ID
                    usernameVariable: 'dockerHubUser', 
                    passwordVariable: 'dockerHubPass')]) {
                    sh '''
                        echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin
                        docker image tag nginx:alpine $dockerHubUser/college-web-app:latest
                        docker push $dockerHubUser/college-web-app:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application"
                sh 'docker-compose up -d --build'
            }
        }
    }
}
