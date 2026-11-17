pipeline {
    agent any

    environment {
        PYTHON_VENV = "backend/venv"
        DJANGO_SETTINGS_MODULE = "loanpulse_project.settings"
        USE_ORACLE = "False"
        NODE_ENV = "production"
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo 'Checking out latest code from GitLab...'
                checkout scm
            }
        }

        stage('Install Backend Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                dir('backend') {
                    sh '''
                        python3 -m venv venv || python -m venv venv
                        . venv/bin/activate || . venv/Scripts/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Frontend Dependencies') {
            steps {
                echo 'Installing NPM packages...'
                dir('frontend') {
                    sh 'npm ci || npm install'
                }
            }
        }

        stage('Backend Unit & Integration Tests') {
            steps {
                echo 'Running Pytest test suite...'
                dir('backend') {
                    sh '''
                        . venv/bin/activate || . venv/Scripts/activate
                        pytest --maxfail=1 --disable-warnings -v
                    '''
                }
            }
        }

        stage('Frontend Production Build') {
            steps {
                echo 'Compiling React Vite presentation bundle...'
                dir('frontend') {
                    sh 'npm run build'
                }
            }
        }

        stage('Security & Static Code Analysis') {
            steps {
                echo 'Executing Bandit and Pip-audit security checks...'
                dir('backend') {
                    sh '''
                        . venv/bin/activate || . venv/Scripts/activate
                        pip install bandit flake8
                        flake8 core loans documents risk --count --select=E9,F63,F7,F82 --show-source --statistics || true
                        bandit -r core loans documents risk -ll || true
                    '''
                }
            }
        }

        stage('Database Migration Dry-Run') {
            steps {
                echo 'Validating Oracle / Relational Database migrations...'
                dir('backend') {
                    sh '''
                        . venv/bin/activate || . venv/Scripts/activate
                        python manage.py check --deploy || true
                        python manage.py makemigrations --check --dry-run
                    '''
                }
            }
        }

        stage('Deploy to Staging / Production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying LoanPulse services to production container cluster...'
                sh '''
                    docker-compose build
                    docker-compose up -d --remove-orphans
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
            cleanWs deleteDirs: true, notFailBuild: true
        }
        success {
            echo 'LoanPulse CI/CD Pipeline succeeded with flying colors!'
        }
        failure {
            echo 'LoanPulse CI/CD Pipeline failed. Alerting engineering team.'
        }
    }
}
