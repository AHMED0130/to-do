def buildApp() {
    sh 'echo "build the app"'
    withCredentials([usernamePassword(credentialsId: 'dockerhub', 
            usernameVariable: 'USERNAME', passwordVariable: 'PASS')]) {
        sh 'docker build -t ahmed0130/todo-app:x3 .'
        sh 'echo $PASS | docker login -u $USERNAME --password-stdin'  
        sh 'docker push ahmed0130/todo-app:x3'
    }
}

def testApp() {
    sh 'echo "test the application......"'
}

def deployApp() {
    sh 'echo "deploy the application to linode...."'
}
