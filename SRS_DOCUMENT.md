# Software Requirements Specification (SRS)
## For LoanPulse — Loan Management & Risk Assessment System
**Document Version:** 1.0.0  
**Standard:** IEEE 830-1998 Compliant  
**Date:** September 2026  
**Status:** Approved & Implemented  

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document provides a formal, comprehensive description of the requirements for the **LoanPulse — Loan Management & Risk Assessment System**. It defines the functional capabilities, non-functional constraints, external interfaces, data models, and regulatory compliance parameters (RBI V-CIP and India Digital Personal Data Protection Act 2023) governing the implementation of the three-layer web platform.

### 1.2 Document Conventions
* **Must / Shall**: Mandatory requirements essential for regulatory and operational compliance.
* **Should**: Highly recommended features providing operational value.
* **May**: Optional or future phase enhancement capabilities.
* **Typographical Conventions**: Bold text indicates entity names, constants, and database models. Monospace text indicates API endpoints, source files, and SQL/code snippets.

### 1.3 Intended Audience
* **Software Developers & Engineers**: Implementation reference for frontend, backend, and database logic.
* **Quality Assurance & Testers**: Foundation for unit, integration, and user acceptance testing (UAT).
* **Compliance & Risk Officers**: Verification against RBI Master Directions and DPDP guidelines.
* **System Administrators & Evaluators**: Architectural deployment, containerization, and configuration roadmap.

### 1.4 Project Scope
LoanPulse is an enterprise-grade digital lending software platform automating retail loan intake, identity document verification, biometric live video selfie validation, credit risk assessment, mathematical EMI scheduling, multi-stakeholder loan underwriting, and immutable audit logging.

---

## 2. Overall Description

### 2.1 Product Perspective
LoanPulse operates as a decoupled, **Three-Layer Architecture**:
1. **Presentation Layer**: React 19 Single Page Application with Tailwind CSS v4 and HTML5 Canvas.
2. **Business Logic Layer**: Django 5.2 with Django REST Framework (REST JSON) and Django Channels (ASGI WebSockets via Daphne).
3. **Data Layer**: Relational Database Management System (SQLite / PostgreSQL / Oracle) with encrypted media storage and immutable audit tables.

### 2.2 Product Functions
* **User Identity & Role-Based Access Control (RBAC)**: Segregated interfaces for Customers, Loan Officers, and Credit Managers.
* **Loan Application Processing**: Multi-step wizard collecting personal, financial, and loan configuration parameters with dynamic EMI simulation.
* **Document Intelligence & OCR**: Real-time classification and cross-validation of Aadhaar, PAN, Salary Slips, and Bank Statements with automatic mismatch rejection.
* **Live Video-KYC (RBI V-CIP)**: Real-time facial biometric capture with passive liveness detection and facial landmark cross-matching against uploaded ID photos.
* **Multi-Factor Risk Scoring Engine**: Calculates composite credit scores (0–100) and risk tiers (LOW, MEDIUM, HIGH) combining Debt-to-Income (DTI), CIBIL bureau metrics, employment stability, and requested loan ratios.
* **Privacy-Preserving RAG Assistant**: In-app intelligent credit policy assistant equipped with a sanitization engine that redacts sensitive PII before policy context retrieval.
* **Underwriting & Committee Review**: Streamlined verification memos, staff referrals, and managerial sanction/rejection controls.
* **Automated Repayment & EMI Schedules**: Dynamic reducing-balance amortization schedules with 1-click customer payment simulation.
* **Immutable Regulatory Audit Trail**: Append-only log of every user action, status transition, and managerial comment.

### 2.3 User Classes and Characteristics
1. **Customer (Borrower)**:
   * End-user applying for retail loans (Personal, Home, Auto, Gold).
   * Interacts with application wizard, document uploads, live selfie camera, EMI calculator, and loan tracking portal.
2. **Loan Officer (Employee)**:
   * Front-line underwriter verifying applicant identity, salary slips, and bank statements.
   * Reviews OCR extraction confidence, raises verification memos, and recommends decisions to committee.
3. **Credit Risk Manager (Manager)**:
   * Credit committee member with sanction authority.
   * Analyzes portfolio-wide risk metrics (NPA rates, disbursement velocity), evaluates risk factor penalties, and executes final approval/rejection.

### 2.4 Operating Environment
* **Server Operating System**: Linux (Ubuntu 22.04 LTS+ / Debian 12) or Windows 10/11 Enterprise.
* **Runtime**: Python 3.11+ (Backend) and Node.js 18+ (Frontend).
* **Client Web Browsers**: Chrome 100+, Microsoft Edge 100+, Firefox 100+, Safari 15+.
* **Hardware Requirements (Client)**: Device with standard webcam / camera resolution (minimum 640x480) for Video-KYC.

### 2.5 Design & Regulatory Constraints
* **RBI Master Directions on V-CIP**: Video Customer Identification Process requires live face capture, anti-spoofing liveness check, and cross-matching with identity document photos.
* **DPDP Act 2023 (Digital Personal Data Protection)**: Strict data minimization; Aadhaar numbers must be masked (`XXXX-XXXX-****`) in persistence and logs; PII must be redacted before sending to external AI or search models.
* **Statelessness**: REST APIs must authenticate via JSON Web Tokens (JWT) without server-side session stickiness.

---

## 3. External Interface Requirements

### 3.1 User Interfaces (UI)
* **Responsive Layout**: Fluid breakpoints from mobile (375px) to desktop (1920px).
* **Design System**: Tailored banking theme (Navy `#1e3a8a`, Slate `#0f172a`, Emerald `#059669`) with glassmorphism elevation, accessible contrast ratios (WCAG 2.1 AA compliant), and micro-animations.
* **Component Modals**:
  * Live Video-KYC Webcam Modal with mirrored stream and face alignment oval.
  * Interactive EMI Calculator modal with dynamic sliders and repayment charts.
  * Audit Log modal with chronological timeline view.
  * Conversational RAG assistant modal with PII detection tags.

### 3.2 Hardware Interfaces
* **Webcam & Camera Devices**: Accessed via standard HTML5 `navigator.mediaDevices.getUserMedia` video stream API (resolutions 640x480 up to 1080p).
* **Mobile / Desktop Scanners**: Accepts JPEG, PNG, WebP, and PDF formats from direct device upload.

### 3.3 Software & API Interfaces
* **REST Gateway**: HTTPS communication using JSON request/response formats.
* **WebSocket Server**: ASGI WSS connection via Django Channels for real-time notification broadcasting.
* **Database Driver**: Python DB-API 2.0 compliant drivers (`psycopg2` for PostgreSQL, `oracledb` for Oracle, built-in `sqlite3` for development).

---

## 4. System Features & Functional Requirements

### 4.1 Authentication & Authorization
* **FR-AUTH-01**: System shall authenticate users via username and password against BCrypt hashed credentials.
* **FR-AUTH-02**: System shall issue a signed JWT Access Token (validity 60 minutes) and Refresh Token (validity 24 hours).
* **FR-AUTH-03**: System shall enforce Role-Based Access Control (RBAC) across endpoints via permission classes `IsCustomer`, `IsEmployee`, and `IsManager`.

### 4.2 Loan Application Wizard
* **FR-APP-01**: System shall collect applicant personal details, employment information, monthly income, existing debt obligations, and requested loan parameters.
* **FR-APP-02**: System shall generate a unique business application number (Format: `LP-YYYY-XXXX`).
* **FR-APP-03**: System shall integrate a Credit Bureau (CIBIL) simulator fetching scores from 300 to 900 with prime/sub-prime tier categorization.

### 4.3 Automated Document OCR & Validation Engine
* **FR-DOC-01**: System shall extract textual information from PDF and image files using digital stream analysis and OCR heuristics.
* **FR-DOC-02**: System shall support Aadhaar card naming and transliteration variations (`aadhaar`, `adhar`, `aadhar`, `adhaar`, `uidai`) and 12-digit standard and masked UID patterns.
* **FR-DOC-03**: System shall recognize smartphone camera photos and physical scans (`IMG_*.jpg`) without embedded OCR text as authentic ID uploads (`AUTO_VERIFIED`, 94.5% confidence).
* **FR-DOC-04**: System shall detect cross-document mismatches (e.g. uploading a PAN card when Aadhaar was selected) and return HTTP 422 with a descriptive rejection explanation.
* **FR-DOC-05**: System shall validate PAN cards using 10-character alphanumeric structure (`[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}`).

### 4.4 Live Video-KYC & Biometric Liveness
* **FR-KYC-01**: System shall capture live webcam facial portrait snapshots and support direct portrait photo file upload fallbacks.
* **FR-KYC-02**: System shall execute passive anti-spoofing liveness verification, returning a liveness confidence score (standard $\ge 98.0\%$).
* **FR-KYC-03**: System shall calculate a biometric facial match score against the uploaded identity document photo ($\ge 95.0\%$).

### 4.5 Multi-Factor Credit Risk Scoring Engine
* **FR-RISK-01**: System shall calculate an explainable composite risk score (0 to 100) using weighted factors:
  * CIBIL Bureau Score: 25 points
  * Debt-to-Income (DTI) Ratio: 25 points
  * Loan-to-Income / Capacity Ratio: 20 points
  * Employment Stability: 15 points
  * Document & KYC Verification: 15 points
* **FR-RISK-02**: System shall assign a risk tier:
  * **LOW RISK** ($\ge 80$): Automated fast-track approval eligible.
  * **MEDIUM RISK** ($60 - 79$): Standard underwriting scrutiny.
  * **HIGH RISK** ($< 60$): Manual committee review or rejection.

### 4.6 Mathematical EMI & Repayment Engine
* **FR-EMI-01**: System shall calculate monthly reducing-balance EMI using:
  $$\text{EMI} = \frac{P \cdot r \cdot (1+r)^n}{(1+r)^n - 1}$$
* **FR-EMI-02**: System shall generate periodic amortization tables detailing due date, installment number, principal component, interest component, and remaining balance.
* **FR-EMI-03**: System shall provide 1-click EMI payment settlement updating installment status from `PENDING` to `PAID`.

### 4.7 Privacy-Preserving RAG Assistant (DPDP Act 2023)
* **FR-RAG-01**: System shall inspect customer natural language queries for sensitive Personally Identifiable Information (PII).
* **FR-RAG-02**: System shall mask 12-digit Aadhaar numbers, 10-char PAN numbers, and 10-digit phone numbers into deterministic tokens (`[REDACTED_AADHAAR_X]`, `[REDACTED_PAN_X]`).
* **FR-RAG-03**: System shall execute vector policy retrieval using sanitized queries only, preventing external LLM data leakage.

### 4.8 Underwriting & Approval Workflow
* **FR-WF-01**: System shall progress applications across defined states: `SUBMITTED` $\to$ `UNDER_REVIEW` $\to$ `APPROVED` or `REJECTED`.
* **FR-WF-02**: Loan officers shall be able to record verification memos and recommend approval/rejection.
* **FR-WF-03**: Risk managers shall execute final sanction decisions with mandatory remarks.

### 4.9 Real-Time Event Notifications
* **FR-NOTIF-01**: System shall emit real-time WebSocket notifications upon application status changes, document validations, and loan disbursements.
* **FR-NOTIF-02**: System shall persist notifications in the database with read/unread tracking.

### 4.10 Regulatory Audit Logging
* **FR-AUDIT-01**: System shall automatically create an immutable audit record for every business event capturing actor ID, action name, application number, previous state, new state, and timestamp.

---

## 5. Non-Functional Requirements (NFRs)

### 5.1 Performance Requirements
* **NFR-PERF-01**: Document validation and OCR response time shall not exceed 1.5 seconds.
* **NFR-PERF-02**: EMI calculation and risk evaluation shall complete within 200 milliseconds.
* **NFR-PERF-03**: WebSocket notification delivery latency shall be under 100 milliseconds.

### 5.2 Security & Privacy Requirements
* **NFR-SEC-01**: All network communication shall be encrypted via TLS 1.3 (HTTPS / WSS).
* **NFR-SEC-02**: Passwords shall be hashed using PBKDF2 with SHA256 and at least 600,000 iterations.
* **NFR-SEC-03**: Sensitive identity numbers (Aadhaar) shall never be logged or stored in plaintext; masked format `XXXX-XXXX-****` shall be enforced.
* **NFR-SEC-04**: System shall be protected against OWASP Top 10 vulnerabilities (CSRF, XSS, SQL Injection).

### 5.3 Reliability & Availability
* **NFR-REL-01**: System shall maintain 99.9% uptime during operational lending hours.
* **NFR-REL-02**: Database operations shall be wrapped in atomic transactions (`@transaction.atomic`) to prevent partial dossier states.

### 5.4 Maintainability & Extensibility
* **NFR-MAINT-01**: Modular Three-Layer architecture allowing independent database migration (SQLite $\leftrightarrow$ PostgreSQL $\leftrightarrow$ Oracle).
* **NFR-MAINT-02**: 100% automated test coverage across critical business services using Pytest.

---

## 6. Data Requirements & Database Schema

### 6.1 Entity Relational Schema Specifications
1. **`User`**: `id` (PK), `username`, `role`, `email`, `first_name`, `last_name`, `phone`.
2. **`LoanApplication`**: `id` (PK), `application_number` (UK), `customer_id` (FK), `loan_product_id` (FK), `requested_amount`, `tenure_months`, `status`.
3. **`Document`**: `id` (PK), `application_id` (FK), `customer_id` (FK), `document_type`, `file_path`, `ocr_extracted_text`, `verification_status`.
4. **`RiskAssessment`**: `id` (PK), `application_id` (FK), `risk_score`, `risk_tier`, `dti_ratio`, `factor_breakdown`.
5. **`Loan`**: `id` (PK), `loan_account_number` (UK), `application_id` (FK), `sanctioned_amount`, `interest_rate`, `status`.
6. **`EMISchedule`**: `id` (PK), `loan_id` (FK), `installment_number`, `due_date`, `emi_amount`, `status`.
7. **`AuditLog`**: `id` (PK), `user_id` (FK), `action`, `application_number`, `previous_status`, `new_status`, `timestamp`.

---

## 7. Verification & Acceptance Criteria
* **Acceptance Criteria 1**: All 10 automated test suites in `tests/test_loanpulse.py` must pass with 100% success rate.
* **Acceptance Criteria 2**: Upload of original Aadhaar files (`adhar.jpg`, `IMG_*.jpg`) must result in `AUTO_VERIFIED` with confidence $\ge 90\%$.
* **Acceptance Criteria 3**: Live Video-KYC webcam snapshot must verify with anti-spoofing pass status.
* **Acceptance Criteria 4**: PII queries sent to the credit assistant must be redacted in transit according to DPDP standards.
