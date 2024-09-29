# QR-based Document Transaction and Information System (QrDTIS)
### Software Engineering 1 Project

# QR Data Handler
## Overview
The QR Data Handler is a desktop application that plays a crucial role in processing transaction requests at Isabela State University's registrar. This application is responsible for handling data sent from the [QrDTIS Scanner](https://github.com/brynyz/QrDITS---Scanner) app, validating it against the local database, and processing the purchase requests. The system also includes a secure login system for the cashier to access the application.

## Features
- **Login System**: Secure login interface for cashiers to access the application.
- **Data Handling**: Processes data received from the cashier's QR Scanner mobile app via a local database.
- **Transaction Management**: Verifies and processes purchase requests such as Certificate of Assessment, Certificate of Enrollment, and Certificate of Grades.
- **Database Integration**: Connects to a local database for real-time transaction validation.

## Usage
1. **Login**: Cashiers use their credentials to log in securely to the desktop application.
2. **Receive Data**: The application receives transaction data from the cashier's QR Scanner mobile app via the local database.
3. **Validate and Process**: The app verifies the data against the local records, and if valid, processes the purchase request for the cashier to complete the transaction.

## Requirements
1. Python
2. Pyside6
3. MySQL

## Installing Repository
```bash
git clone https://github.com/brynyz/QrDTIS---QR-Database Processor.git
```

## Contact
Feedback or questions are welcomed. Contact bryllenyelm@gmail.com
