pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/ZawarHaiderDevops/flaskapp.git'
            }
        }

        stage('Build') {
            steps {
                // Add build steps if needed
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps here
                // Example: Copy files to the EC2 instance using SCP
                sshagent(['0292f24f-3cc5-4d46-b6b6-7e388f8872e9']) {
                    sh 'scp -r * ubuntu@3.235.164.4:/root/github'
                }
            }
        }
    }
}
