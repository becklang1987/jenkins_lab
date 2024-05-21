pipeline {
environment {
registry = "becklang1987/python_flask"
registryCredential = 'mygmail'
dockerImage = ''
}
    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/becklang1987/jenkins_lab.git'
                echo "Running Code Pulling from Github"
            }
            }
        stage('Docker_Build') {
            steps {
                script {
                    dockerImage = docker.build $registry + ":v1.0"
                }
            }
        stage('Deploy our image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
        }
    }
        stage('Cleaning up') {
            steps{
                sh "docker rmi $registry:v1.0"
            }
        }
        }
    }
}
