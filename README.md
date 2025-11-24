# Password Hashing & Verification Script

This project demonstrates how to securely hash and verify passwords in Python using the built-in [`hashlib`](https://docs.python.org/3/library/hashlib.html) module and random salts.

It's a simple example to help understand how password hashing works and whyit's safer than storing plain-text passwords.

---

## Features

- Hashes passwords using **SHA256**
- Adds a **random salt** for each password to prevent hash collisions
- Verifies passwords safely by recomputing and comparing hashes
- Uses only built-in Python modules (`hashlib`, `os`)
- Includes **detailed inline comments** throughout the script to explain how each part works

---

## How It Works

1. When a user creates a password:
   - A random `salt` (16 bytes) is generated using `os.urandom()`
   - The salt is combined with the password before hashing
   - Both the salt and the resulting hash are stored (not the plain password)

2. When verifying a password:
   - The stored salt is retrieved
   - The user's entered password is hashed again with that same salt
   - If the new hash matches the stored one → ✅ access granted
  
---

## How to Run:

1. You can clone this repository:

```
git clone https://github.com/coder0name0dre/password_hash.git
```

2. Navigate to the folder:

```
cd password_hash
```

3. Run the file:

```
python3 password_hash.py
```

4. Follow the prompts to and verify a password.

---

## Notes

- This is a **learning example** - good for understanding hashing basics.
- The script contains inline comments explaining each step of the process, making it easier to follow along.
- **Never** store or transmit plain-text passwords.
 
## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/password_hash/blob/main/LICENSE).
