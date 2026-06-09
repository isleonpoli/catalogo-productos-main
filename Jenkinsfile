pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Mostrar archivos') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy Docker') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Verificar API') {
            steps {
                sh '''
                curl -f http://host.docker.internal:5000/productos
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }

        failure {
            echo 'Pipeline falló'
        }
    }
}