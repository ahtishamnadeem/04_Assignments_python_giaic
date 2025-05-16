
# Secure Data Encryption System

This is a simple **Secure Data Encryption System** built using **Streamlit** and **Cryptography** to securely encrypt, store, and retrieve sensitive data. 
It uses a fixed encryption key for encrypting the data and a passkey-based approach for secure access.

---

## Features

- **Store Data**: Users can securely encrypt their data using a passkey, which is then stored in a JSON file.
- **Retrieve Data**: Users can decrypt their encrypted data by providing the correct passkey.
- **Admin Login**: After multiple failed attempts, users are required to log in using a master password to access the decryption functionality.
- **Fail-Safe**: The system locks after three failed decryption attempts, requiring reauthorization by an admin.
- **Secure Storage**: The encrypted data is stored securely in a file, ensuring privacy.

---

## Technologies Used

- **Python**: Programming language used for backend logic.
- **Streamlit**: Framework used for building the interactive UI.
- **Cryptography**: Library used for secure data encryption and decryption.
- **JSON**: For storing encrypted data and passkeys.

---

## Setup Instructions

### Prerequisites

- Python 3.6+
- Install required Python packages using pip:

```bash
pip install streamlit cryptography



### Made and Managed By | CodeWithAhtii
