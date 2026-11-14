import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    """Generates a secure password based on user preferences."""
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: You must select at least one character type!"

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password


def check_strength(password):
    """Evaluates the strength of a given password."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_num = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    feedback = []

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password is too short (minimum 8 characters recommended).")

    if has_upper:
        score += 1
    else:
        feedback.append("⚠️ Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        feedback.append("⚠️ Add lowercase letters.")

    if has_num:
        score += 1
    else:
        feedback.append("⚠️ Add numbers.")

    if has_symbol:
        score += 1
    else:
        feedback.append("⚠️ Add special characters/symbols.")

    if score >= 5 and length >= 12:
        rating = "Strong 🔒"
    elif score >= 3:
        rating = "Medium ⚡"
    else:
        rating = "Weak ❌"

    return rating, feedback


def main():
    print("=======================================")
    print("   🔐 Python Password CLI Tool 🔐      ")
    print("=======================================")

    while True:
        print("\nOptions:")
        print("1. Generate a secure password")
        print("2. Check password strength")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            try:
                user_input = input("Enter password length (default 12): ").strip()
                length = int(user_input) if user_input else 12
                if length < 4:
                    print("❌ Password length should be at least 4 characters.")
                    continue

                pwd = generate_password(length=length)
                print(f"\nGenerated Password: {pwd}")

                rating, _ = check_strength(pwd)
                print(f"Strength Rating: {rating}")
            except ValueError:
                print("❌ Please enter a valid number for length.")

        elif choice == "2":
            pwd_to_check = input("Enter password to check: ")
            rating, feedback = check_strength(pwd_to_check)
            print(f"\nStrength Rating: {rating}")
            if feedback:
                print("Suggestions to improve:")
                for tip in feedback:
                    print(f"  - {tip}")
            else:
                print("✨ Excellent! This password looks very secure.")

        elif choice == "3":
            print("Goodbye! Stay secure. 🚀")
            break
        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
