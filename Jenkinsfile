pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "wajdibejaoui/django-app"
        DOCKER_TAG = "latest" // Or dynamically set with BUILD_NUMBER or GIT_COMMIT
        DOCKER_TAG = "${env.BUILD_NUMBER ?: 'latest'}" // Use BUILD_NUMBER if available, fallback to 'latest'

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
                    ls -l /usr/local/bin/docker-compose
                    /usr/local/bin/docker-compose --version
                    
                    
                    docker-compose build
                    '''
                }
            }
        }

         stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker tag ${DOCKER_IMAGE}:latest ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        '''
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    echo "Setting up Minikube context for kubectl"
                    minikube start
                    
                    echo "Applying Kubernetes manifests"
                    sed -i "s|DOCKER_IMAGE|${DOCKER_IMAGE}:${DOCKER_TAG}|g" k8s/deployment.yml
                    kubectl apply -f k8s/deployment.yml
                    kubectl apply -f k8s/service.yml

                    echo "Checking deployed resources"
                    kubectl get pods
                    kubectl get svc
                    '''
                }
            }
        }
    }
}
