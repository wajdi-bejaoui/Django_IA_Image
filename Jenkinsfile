pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "wajdi.bejaouui/django-app"
        DOCKER_TAG = "latest" // Or dynamically set with BUILD_NUMBER or GIT_COMMIT
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code to make sure the docker-compose.yml file is available
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    echo "Building Docker Images with Docker Compose"
                    ls -alh  # List directory contents for 
                    
                    echo "Checking directory contents"
                    docker run --rm -v $PWD:/app -v /var/run/docker.sock:/var/run/docker.sock docker/compose:latest ls /app

                    docker run --rm -v $PWD:/app -v /var/run/docker.sock:/var/run/docker.sock docker/compose:latest build
                    ls -alh  # List directory contents for debugging
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        // Push the image to Docker Hub
                        sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        '''
                    }
                }
            }
        }
    }
}
