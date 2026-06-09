pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validar estructura') {
            steps {
                sh 'ls -la'
                sh 'test -f docker-compose.yml'
                sh 'test -f backend/app.py'
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