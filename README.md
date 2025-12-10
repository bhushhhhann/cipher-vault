# 🔐 **Cipher Vault — Python CLI Password Manager**

Cipher Vault is a simple, lightweight **Python command-line password manager** that stores passwords in **XOR-encrypted form**.  
It allows you to add, update, delete, list, and securely access passwords saved for different websites.

Passwords are **never stored in plain text** — they are encrypted and can only be decrypted using your **PIN**.

---

## ⭐ **Features**

- 🔒 **Secure XOR-based encryption**
- 📄 Store website name, username, and encrypted password
- ➕ Add new passwords  
- ✏️ Update existing passwords  
- ❌ Delete saved passwords  
- 👁 View/decrypt password *(PIN required)*  
- 📁 Auto-creates & manages `password_manager.txt` JSON file  
- 🧠 Simple, easy-to-understand reversible encryption  
- 🖥 Fully terminal-based CLI app

---

## 🛠 **How the Encryption Works**

Cipher Vault uses a reversible XOR cipher:
  encrypted_value = ord(character) ^ key
  original_character = chr(encrypted_value ^ key)
- `key = 123`  
- Each character of the password is encrypted to a number  
- Only someone with the correct **PIN (6969)** can decrypt it  

This technique is lightweight and perfect for learning basic cryptography.

---

## 📁 **Project Structure**

cipher-vault/
│
├── cipher_vault.py # Main project code
├── password_manager.txt # JSON file storing encrypted passwords
└── README.md # Project documentation


---

## ▶️ **How to Run**

1. Install Python (3.x)
2. Download or clone this repository
3. Open a terminal in the project directory
4. Run:
    python cipher_vault.py
5. Use menu options (1–6) to manage your passwords.

---

##  **Menu Options**

1.List all saved website passwords
2.Add a new password
3.Update an existing password
4.Delete a password
5.Access (View) a password ← requires PIN
6.Exit the program


##  **Example Stored Data (`password_manager.txt`)**
```json
[
    {
        "website": "google.com",
        "username": "bhushan",
        "password": [171, 85, 90]
    }
]

👨‍💻 Author

Bhushan Bhutada
Python beginner exploring encryption techniques and building practical CLI tools.
