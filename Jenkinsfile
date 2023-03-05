pipeline {
agent any
    stages {
      stage('Clone Git') {
            steps {
                git 'https://github.com/PrafullPandey06/spe'
            }
        }
      stage('Build Code') {
        steps {
                 sh "chmod u+x Prog.py"
                 sh "python3 Prog.py"
            }
        }
      stage('Test Code') {
        steps {
                 sh "chmod u+x Test.py"
                 sh "./Test.py"
        }
    }
 }  
}
