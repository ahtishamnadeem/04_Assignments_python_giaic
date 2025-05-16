import streamlit as st
from cryptography.fernet import Fernet
import hashlib

<<<<<<< HEAD
# In-memory storage
stored_data = {}
failed_attempts = {}
session_auth = {"authorized": True}

# Generate a key for Fernet
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

=======
# Session states for persistence
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = {}

if "authorized" not in st.session_state:
    st.session_state.authorized = True

# Create Fernet instance
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
fernet = Fernet(st.session_state.fernet_key)

# Utility: Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Insert new data
def insert_data(user_id, text, passkey):
    encrypted_text = fernet.encrypt(text.encode()).decode()
    hashed_passkey = hash_passkey(passkey)
<<<<<<< HEAD
    stored_data[user_id] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
=======
    st.session_state.stored_data[user_id] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
    st.success(f"Data stored securely for user: {user_id}")

# Retrieve data
def retrieve_data(user_id, passkey):
<<<<<<< HEAD
    if user_id not in stored_data:
=======
    if user_id not in st.session_state.stored_data:
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
        st.error("No data found for this user.")
        return

    # Check failed attempts
<<<<<<< HEAD
    if failed_attempts.get(user_id, 0) >= 3:
        session_auth["authorized"] = False
=======
    if st.session_state.failed_attempts.get(user_id, 0) >= 3:
        st.session_state.authorized = False
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
        st.warning("Too many failed attempts. Redirecting to login.")
        st.experimental_rerun()
        return

    hashed_input = hash_passkey(passkey)
<<<<<<< HEAD
    if hashed_input == stored_data[user_id]["passkey"]:
        decrypted = fernet.decrypt(stored_data[user_id]["encrypted_text"].encode()).decode()
        st.success(f"Decrypted Data: {decrypted}")
        failed_attempts[user_id] = 0  # reset after success
    else:
        failed_attempts[user_id] = failed_attempts.get(user_id, 0) + 1
        attempts_left = 3 - failed_attempts[user_id]
=======
    if hashed_input == st.session_state.stored_data[user_id]["passkey"]:
        decrypted = fernet.decrypt(st.session_state.stored_data[user_id]["encrypted_text"].encode()).decode()
        st.success(f"Decrypted Data: {decrypted}")
        st.session_state.failed_attempts[user_id] = 0  # Reset on success
    else:
        st.session_state.failed_attempts[user_id] = st.session_state.failed_attempts.get(user_id, 0) + 1
        attempts_left = 3 - st.session_state.failed_attempts[user_id]
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
        st.error(f"Incorrect passkey. Attempts left: {attempts_left}")

# Login Page
def login_page():
    st.title("🔐 Reauthorization Required")
    username = st.text_input("Enter Admin Username")
    password = st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
<<<<<<< HEAD
            session_auth["authorized"] = True
            st.success("Login successful!")
            failed_attempts.clear()
=======
            st.session_state.authorized = True
            st.session_state.failed_attempts.clear()
            st.success("Login successful!")
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")

# Main App
def main():
<<<<<<< HEAD
    if not session_auth.get("authorized", True):
=======
    if not st.session_state.authorized:
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
        login_page()
        return

    st.sidebar.title("🔐 Secure Data Storage")
    menu = st.sidebar.radio("Navigate", ["Home", "Insert Data", "Retrieve Data", "Login"])

    if menu == "Home":
        st.title("Welcome to Secure Data Encryption System")
        st.write("Use the sidebar to insert or retrieve encrypted data.")

    elif menu == "Insert Data":
        st.title("📥 Store Your Secure Data")
        user_id = st.text_input("Enter User ID")
        data = st.text_area("Enter Data to Encrypt")
        passkey = st.text_input("Set a Passkey", type="password")
        if st.button("Store Data"):
            if user_id and data and passkey:
                insert_data(user_id, data, passkey)
            else:
                st.warning("All fields are required.")

    elif menu == "Retrieve Data":
        st.title("🔓 Retrieve Your Encrypted Data")
        user_id = st.text_input("Enter Your User ID")
        passkey = st.text_input("Enter Your Passkey", type="password")
        if st.button("Decrypt Data"):
            if user_id and passkey:
                retrieve_data(user_id, passkey)
            else:
                st.warning("Both User ID and Passkey are required.")

    elif menu == "Login":
        login_page()

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> cea9b41ca432aebec716a6b46941ec683c800bde
