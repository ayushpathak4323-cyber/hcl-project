# LoanPulse — Running in VS Code Guide

Welcome to **LoanPulse — Loan Management & Risk Assessment System**! Follow this simple guide to run the entire project in Visual Studio Code.

---

## 🚀 Quickest Way (One-Click)

Inside the unzipped `loanpulse` folder:
* Simply double-click **`run_all.bat`**.
* It will automatically open two separate command prompt windows:
  1. **Backend Server** on `http://localhost:8000` (auto-creates venv & installs dependencies if needed)
  2. **Frontend Server** on `http://localhost:5173` (auto-runs `npm install` if needed)
* Open your browser and navigate to: **`http://localhost:5173`**

---

## 💻 Running Directly Inside VS Code Terminals

### Step 1: Open Project in VS Code
1. Open VS Code.
2. Click **File > Open Folder...** and select the unzipped `loanpulse` folder.

---

### Step 2: Start the Backend (Terminal 1)
1. Open a new terminal in VS Code: `Ctrl + \`` (or **Terminal > New Terminal**).
2. Run the following commands:
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
✅ Backend is now live at: `http://localhost:8000`

---

### Step 3: Start the Frontend (Terminal 2)
1. Split the terminal or click the **`+`** icon to open a second terminal.
2. Run the following commands:
```powershell
cd frontend
npm install
npm run dev
```
✅ Frontend is now live at: `http://localhost:5173`

---

## 🔑 Demo Login Accounts

| Role | Username | Password | Access / Capabilities |
| :--- | :--- | :--- | :--- |
| **Customer** | `customer` | `customer123` | Apply for loan, CIBIL score simulator, Live Video-KYC selfie, Original Aadhaar/PAN upload, Privacy RAG assistant |
| **Loan Officer (Employee)** | `officer` | `officer123` | Document verification desk, manual review, underwriting reports |
| **Credit Manager** | `manager` | `manager123` | Credit committee approval/rejection, risk engine matrix, audit trail |

---

## 🧪 Running Automated Unit Tests
To verify all 10 unit tests (including Original Aadhaar variants and Webcam Selfie API):
In the backend terminal with `venv` activated:
```powershell
cd backend
pytest
```
All 10 tests will run and pass!

---

## 📁 Key Features Implemented
1. **Live Video-KYC Selfie Verification**:
   * RBI V-CIP compliant facial capture & passive liveness detection.
   * Supports live webcam capture, file photo upload, or 1-click evaluator demo simulator.
2. **Smart Original Aadhaar Document Acceptance**:
   * Accepts mobile camera photos, scanned PDFs, and various file naming variants (`adhar.jpg`, `aadhar.png`, `IMG_*.jpg`).
   * 12-digit UID and masked UID detection (`XXXX-XXXX-****`).
   * Strict cross-document mismatch rejection (e.g. uploading PAN under Aadhaar).
3. **CIBIL Score Integration & Privacy-Preserving RAG**:
   * Live bureau pull simulator in personal details section.
   * DPDP Act-compliant PII redaction and masking before credit policy queries.
4. **Three-Layer Architecture**:
   * React 19 + Tailwind CSS + Lucide Icons frontend.
   * Django + DRF + Channels ASGI backend.
   * Comprehensive audit logs and real-time notifications.
