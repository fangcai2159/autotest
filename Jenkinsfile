pipeline {
    agent {
        docker {
            image 'python:3.13.5'   // 你也可以用自己定制的镜像
        }
    }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/fangcai2159/autotest.git', branch: 'main',
                credentialsId: 'github-token' 

            }
        }
        

        stage('Install dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    pytest tests/ --maxfail=2 --disable-warnings --tb=short --junitxml=pytest-report.xml
                '''
            }
        }

        stage('Archive Results') {
            steps {
                junit 'pytest-report.xml'
                archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            }
        }

        // 可选 Allure 报告
        // stage('Generate Allure Report') {
        //     when {
        //         expression { fileExists('allure-results') }
        //     }
        //     steps {
        //         sh '''
        //             allure generate allure-results -o allure-report --clean || true
        //         '''
        //         archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
        //     }
        // }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Tests failed! Please check the results.'
        }
    }
}
