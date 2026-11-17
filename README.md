# LoanPulse — Loan Management & Risk Assessment System

> **A Production-Grade, Enterprise Three-Layer Fintech Web Application for Digital Lending, OCR Document Validation, Explainable Credit Risk Assessment, and Amortized Loan Disbursement.**

---

## 🏛️ System Architecture: Three-Layer Design

LoanPulse strictly enforces the **Three-Layer Architecture** pattern:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                              │
│  React 19 + Tailwind CSS + Lucide Icons + Real-Time WebSocket Client   │
│  - Customer Self-Service Portal                                        │
│  - Loan Officer / Employee Verification Workspace                      │
│  - Executive Credit Committee / Manager Approval Board                 │
│  - Real-Time Notification Bell & Interactive Audit Log Ledger          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  REST APIs / JSON / JWT / WebSockets
┌───────────────────────────────────▼────────────────────────────────────┐
│                       BUSINESS LOGIC LAYER                             │
│  Django 5 + Django REST Framework + Django Channels + ASGI Daphne      │
│  - Document Verification & OCR Classification Service                  │
│  - Transparent & Explainable Credit Risk Scoring Engine (0-100)        │
│  - Reducing-Balance EMI Amortization & Repayment Engine                │
│  - Role-Based Access Control (RBAC) & State Machine Workflow           │
│  - Notification Dispatcher (DB Persistence + WebSocket Broadcast)      │
│  - Banking-Grade Immutable Audit Logging Service                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │  Django ORM (Dual Backend Support)
┌───────────────────────────────────▼────────────────────────────────────┐
│                            DATA LAYER                                  │
│  Oracle Database (Enterprise 19c/21c/23c) / SQLite Default Fallback    │
│  - LP_USERS, LP_CUSTOMERS, LP_EMPLOYEES, LP_MANAGERS                   │
│  - LP_LOAN_PRODUCTS, LP_LOAN_APPLICATIONS, LP_DOCUMENTS                │
│  - LP_RISK_ASSESSMENTS, LP_VERIFICATION_REPORTS                        │
│  - LP_LOANS, LP_EMI_SCHEDULES, LP_PAYMENTS, LP_NOTIFICATIONS           │
│  - LP_AUDIT_LOGS                                                       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### 1. Unified Multi-Role Authentication
- Single landing page with **Customer Login**, **Employee Login**, and **Manager Login**.
- **1-Click Autofill Demo Buttons** for effortless presentation and evaluator testing.
- JWT-based authentication (`djangorestframework-simplejwt`) with strict Role-Based Access Control (RBAC).
- A customer cannot access employee or manager endpoints; employees cannot execute manager-only loan disbursements.

### 2. Multi-Step Loan Application (Customer)
- **Step 1 — Demographic / Personal Details**: Full Name, DOB, Phone, Email, Residential Address.
- **Step 2 — Financial Profile**: Monthly Income, Employment Type, Organization, Existing Loans & Monthly EMI Burden, Salary Bank Account.
- **Step 3 — Loan Configuration**: Dynamic amount slider, tenure selection, live reducing-balance EMI preview, total interest, and total repayment calculation.
- **Step 4 — Document Upload & OCR Validation**: File upload with automated content inspection.
- **Step 5 — Submission Dossier**: Automated preliminary risk score generation, unique Application ID creation (e.g. `LP10294`), and instant broadcast to loan officers.

### 3. Document Detection & OCR Validation Engine
- Automatic text extraction and semantic classifier for:
  - **Aadhaar Card**: Detects 12-digit UID pattern (`\d{4}\s\d{4}\s\d{4}`), UIDAI markers, extracts masked UID (`XXXX-XXXX-4410`).
  - **PAN Card**: Detects 10-character alphanumeric PAN format (`[A-Z]{5}[0-9]{4}[A-Z]`), Income Tax Department headers, extracts PAN number.
  - **Salary Slip**: Detects earnings, deductions, basic salary, HRA, and net pay markers.
  - **Bank Statement**: Detects account statements, IFSC, opening/closing balances, credit/debit records.
- **Mismatch Rejection**: If an applicant selects *Aadhaar* but uploads an unrelated or mismatched document (e.g., a recipe or non-identity document), the system rejects the upload with an explicit error:
  > *"The uploaded document does not appear to be an Aadhaar document. The system detected: Unknown Document. Please upload the correct document."*

### 4. Transparent & Explainable Credit Risk Scoring Engine
- Computes a deterministic, explainable risk score from **0 to 100**:
  - **Debt-To-Income (DTI) Ratio** (25% Weight): Total monthly obligations divided by monthly income.
  - **Income Stability & Employment Type** (25% Weight): Salaried / MNC / Business profile stability.
  - **Existing Debt Burden** (20% Weight): Number of concurrent active loan obligations.
  - **Loan-to-Income (LTI) Multiplier** (15% Weight): Loan exposure vs annual earning capacity.
  - **Repayment Track Record & Tenure** (15% Weight): Past on-time credit track record.
- Categorizes risk into **LOW** (75–100), **MEDIUM** (50–74), and **HIGH** (0–49).
- Generates an explainable narrative and component breakdown. *(Human-in-the-loop: The algorithmic evaluation is advisory; final sanctions are reserved for Loan Officers and Managers).*

### 5. Real-Time WebSocket Notifications (Django Channels + ASGI)
- Live push notifications delivered instantly to connected browser sessions without page refresh:
  1. **Customer Submits Application** ➔ Broadcast to `role_EMPLOYEE`: *"🔔 New Loan Application Received — Application #LP10294 (Rahul Sharma, ₹3,50,000)"*.
  2. **Officer Rejects Document** ➔ Push to Applicant: *"Your Aadhaar document could not be verified. Please upload a valid document."*
  3. **Officer Submits Verification Report** ➔ Broadcast to `role_MANAGER`: *"Application LP10294 has been verified by Employee EMP104 and requires final review."*
  4. **Manager Sanctions Loan** ➔ Push to Applicant: *"🎉 Congratulations! Your loan #LP10294 has been approved and disbursed."*
  5. **EMI Approaching / Overdue** ➔ Real-time alert to Applicant and staff dashboards.

### 6. Mock Loan Disbursement & Amortization Repayment
- Reducing-balance monthly EMI formula:
  $$EMI = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1}$$
- Generates month-by-month amortization schedule with due dates, principal component, interest component, and remaining balance.
- **Simulate Payment ("Pay EMI")**: Customer can simulate instant installment payment, updates remaining balance, records payment transaction receipt, and logs audit trail.
- **Simulate Overdue**: Interactive button to simulate overdue installment and verify late alert triggers.

### 7. Banking Audit Trail
- Every critical action is immutably logged in `LP_AUDIT_LOGS`:
  - `User`, `Role`, `Action`, `Application Number`, `Previous Status`, `New Status`, `Remarks`, `Timestamp`.

---

## 🔑 Preloaded Demo Credentials

The database is seeded with realistic accounts for instant demonstration:

| Portal | Role | Username / Email | Password | Identifier / Code |
|---|---|---|---|---|
| **Customer Portal** | Customer / Borrower | `customer@loanpulse.com` | `password123` | Rahul Sharma (Noida) |
| **Employee Portal** | Loan Officer | `employee@loanpulse.com` | `password123` | Priya Desai (`EMP104`) |
| **Manager Portal** | Credit Committee / Underwriter | `manager@loanpulse.com` | `password123` | Vikramaditya Singh (`MGR001`) |

*(Use the 1-Click Autofill buttons on the login screen to toggle between accounts instantly).*

---

## 🗄️ Database Layer & Oracle Schema

The application uses Django ORM mapped to standard uppercase table names (`LP_*`) conforming to Oracle SQL standards.
The complete, production-ready Oracle DDL script is provided in [`backend/oracle_schema.sql`](file:///C:/Users/ayush/.gemini/antigravity/scratch/loanpulse/backend/oracle_schema.sql):

- `LP_USERS`: Master user accounts, passwords, and role constraints (`CUSTOMER`, `EMPLOYEE`, `MANAGER`).
- `LP_CUSTOMERS`: KYC demographics, income, employer, DTI liabilities.
- `LP_EMPLOYEES`: Officer codes, underwriting departments, designations.
- `LP_MANAGERS`: Manager approval limits and committee credentials.
- `LP_LOAN_PRODUCTS`: Minimum/maximum amounts, tenures, and interest rates.
- `LP_LOAN_APPLICATIONS`: Workflow state machine tracking applications.
- `LP_DOCUMENTS`: Document metadata, OCR text, confidence scores, verification status.
- `LP_RISK_ASSESSMENTS`: DTI metrics, component breakdown scores, explainability text.
- `LP_VERIFICATION_REPORTS`: Officer findings, recommendations, and audit remarks.
- `LP_LOANS`: Disbursed loan accounts, approved amounts, interest rates.
- `LP_EMI_SCHEDULES`: Reducing-balance amortization rows with due dates and statuses (`PENDING`, `PAID`, `OVERDUE`).
- `LP_PAYMENTS`: Transaction receipts, payment methods, settlement timestamps.
- `LP_NOTIFICATIONS`: Persistent notification inbox records.
- `LP_AUDIT_LOGS`: Immutable banking audit trail.

### Dual Database Setup:
- **Default (Zero-Configuration Demo)**: Runs seamlessly on SQLite out-of-the-box for instant local development and evaluation.
- **Oracle Database Connection**: Set `USE_ORACLE=True` in `backend/.env` with your Oracle service name, host, and user credentials. The backend automatically switches to `django.db.backends.oracle` with `oracledb`.

---

## 🛠️ Step-by-Step Installation & Running Guide

### Prerequisites
- Python 3.11+
- Node.js 18+ and npm
- Git

### 1. Start the Backend Server (Django + Channels ASGI)

```powershell
# Navigate to backend directory
cd backend

# Activate virtual environment
.\venv\Scripts\activate   # On Windows
# or: source venv/bin/activate (on Linux/macOS)

# Run database migrations
python manage.py migrate

# Seed database with sample customers, officers, and loans
python seed_data.py

# Start ASGI server on port 8000 (Supports WebSockets and HTTP)
python manage.py runserver 8000
```
Backend will be active at: `http://localhost:8000` (WebSocket endpoint: `ws://localhost:8000/ws/notifications/`).

### 2. Start the Frontend Application (React 19 + Vite)

```powershell
# In a new terminal, navigate to frontend directory
cd frontend

# Start the Vite development server
npm run dev
```
Frontend will be accessible at: `http://localhost:5173`.

### 3. Run Backend Test Suite

```powershell
cd backend
.\venv\Scripts\activate
pytest
```
*Expected output: 6 passed in < 1 second.*

---

## 🧪 End-to-End Live Demonstration Workflow

Follow these steps to demonstrate the full application lifecycle:

1. **Sign in as Customer**:
   - Open `http://localhost:5173`.
   - Click **Customer Login** (or click the **Customer** 1-click button). Click **Sign In**.
   - Notice the **Active Loan LN-2026-10088** with 2 paid EMIs and 10 pending.
2. **Apply for a Loan**:
   - Click **Apply for Loan** on the navigation bar.
   - Step 1: Review prefilled personal KYC information. Click **Proceed**.
   - Step 2: Review financial information (Monthly Income: ₹85,000, Company: Infosys). Click **Proceed**.
   - Step 3: Choose loan amount (e.g. ₹3,50,000) and tenure (24 months). Inspect live reducing-balance monthly EMI calculation. Click **Proceed**.
   - Step 4: **Document OCR Verification**:
     - Click **+ Test Valid Aadhaar**. Notice the system extracts text via OCR and marks status as `Document Type Verified: 98.5% confidence`.
     - Click **⚡ Test Rejection (Wrong File)**. Notice the system flags a mismatch: *"The uploaded document does not appear to be an Aadhaar document. Please upload the correct document."*
     - Click **+ Test Valid PAN** to attach the second document.
   - Step 5: Review the dossier summary and click **Submit Loan Application**.
   - Notice unique Application ID generated (e.g., `#LP10294`).
3. **Switch to Employee (Loan Officer)**:
   - Click Logout and sign in with **Employee Login** (or click **Loan Officer** 1-click button).
   - Notice the real-time notification alert toast without refreshing!
   - Locate the newly submitted application in the queue and click **Open Dossier**.
   - Review applicant's financial metrics and examine the **Credit Risk Assessment Engine (Score & Level)**.
   - Inspect uploaded documents and OCR extracted text snippets. Click **Verify**.
   - Select recommendation: *Recommended for Approval*, enter officer remarks, and click **Submit Verification Report to Manager**.
   - Status changes to `EMPLOYEE_VERIFIED`.
4. **Switch to Manager (Credit Committee)**:
   - Click Logout and sign in with **Manager Login** (or click **Manager** 1-click button).
   - Notice the real-time alert: *"Application LP10294 has been verified by Employee EMP104 and requires final review."*
   - Locate the application in the board and click **Final Review**.
   - Review employee report, risk score, and click **Approve & Disburse Loan**.
   - Loan record is generated (`LN-2026-XXXXX`), mock disbursement executed, and amortization schedule created.
5. **Back to Customer**:
   - Switch back to Customer. Notice the live notification: *"🎉 Loan Approved & Disbursed!"*
   - Open **Active Loans & EMI** tab to view the active loan and amortization schedule.
   - Click **Pay EMI** on installment #1 to simulate instant UPI/NetBanking payment.
   - Click **Set Overdue** on installment #2 to simulate overdue status and trigger an overdue alert notification!
6. **Audit Ledger Verification**:
   - Open **Audit Logs** from the top bar to inspect the immutable banking audit trail tracking all actions with timestamps, roles, and status changes.

---

## 🔀 Git Repository & Branches

The repository is structured with the required branch hierarchy:
- `main`: Production-ready release branch with stable deployment configuration.
- `develop`: Development integration branch.
- `feature/customer`: Customer self-service portal, multi-step application, and loan repayment.
- `feature/employee`: Loan officer verification queue, document inspection, and reporting.
- `feature/manager`: Credit committee approval dashboard and loan disbursement engine.

---

## ⚙️ DevOps & CI/CD Pipelines

### 1. Jenkins Pipeline (`Jenkinsfile`)
Includes declarative pipeline stages:
1. `Checkout Source`: Checks out latest commit from repository.
2. `Install Backend Dependencies`: Sets up Python virtual environment and installs dependencies from `requirements.txt`.
3. `Install Frontend Dependencies`: Installs npm packages.
4. `Backend Unit & Integration Tests`: Executes Pytest suite (`pytest`).
5. `Frontend Production Build`: Runs `npm run build` to verify client packaging.
6. `Security & Static Code Analysis`: Runs `flake8` and `bandit` security scans.
7. `Database Migration Dry-Run`: Tests Django ORM migration compatibility.
8. `Deploy to Staging / Production`: Builds and runs Docker containers on `main` branch.

### 2. GitLab CI/CD (`.gitlab-ci.yml`)
Configured with 5 pipeline stages: `lint`, `test`, `build`, `security`, and `deploy`.

### 3. Docker Support (`docker-compose.yml`)
Run the entire platform with containerization:
```bash
docker-compose up --build -d
```
- Backend container on port `8000`
- Frontend Nginx container on port `5173`

---

## 📄 License & Academic Attribution
Developed as an enterprise-grade Loan Management & Risk Assessment System demonstrating Three-Layer Architecture, OCR Verification, Explainable Underwriting, and Real-Time Event Driven Banking Architecture.
