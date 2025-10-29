import hashlib      # Provides access to secure hash algorithms like SHA256
import os           # Used to generate random bytes for the salt


# -------------------------------------------------
# Function: hash_password()
# Purpose: Hashes a password with a random salt
# -------------------------------------------------
def hash_password(password):
    # Generate a random 16-byte salt (this ensures every hash is unique)
    salt = os.urandom(16) 

    # Combine the salt with the password (converted to bytes)
    # and compute a SHA256 hash
    hash_value = hashlib.sha256(salt + password.encode()).hexdigest()

    # Return both the salt (in hex form) and the resulting hash
    # You need a store both when saving a password
    return salt.hex(), hash_value

# -------------------------------------------------
# Function: check_password()
# Purpose: Verifies a password attempt by re-hashing it with the stored salt
# -------------------------------------------------
def check_password(stored_salt, stored_hash, password_attempt):
    # Convert the stored salt (which was saved as hex) back to bytes
    salt = bytes.fromhex(stored_salt)

    # Hash the attempted password using the same salt
    hash_value = hashlib.sha256(salt + password_attempt.encode()).hexdigest()

    # Compare the new hash with the stored hash
    # If they match, the password is correct
    return stored_hash == hash_value

# -------------------------------------------------
# Example usage
# -------------------------------------------------
if __name__ == "__main__":
    # Step 1: Create a hash for a new password
    salt, stored_hash = hash_password("mysecret123")
    print("Salt:", salt)
    print("Stored hash:", stored_hash)
    print("Altogether: ", salt + stored_hash)

    # Step 2: Ask user for their password to verify
    attempt = input("Enter your password: ")

    # Step 3: Check if the entered password matches
    if check_password(salt, stored_hash, attempt):
        print("✅ Access granted!")
    else:
        print("❌ Access denied.")