import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (min 8 characters)": length_error,
        "No uppercase letter": uppercase_error,
        "No lowercase letter": lowercase_error,
        "No digit": digit_error,
        "No special character": special_char_error
    }


    failed_criteria = sum(errors.values())


    if failed_criteria == 0:
        strength = "Very Strong "
    elif failed_criteria == 1:
        strength = "Strong"
    elif failed_criteria == 2:
        strength = "Moderate"
    else:
        strength = "Weak "

    print("\nPassword Analysis:")
    for issue, failed in errors.items():
        if failed:
            print(f"  -  {issue}")
        else:
            print(f"  -  {issue} satisfied")

    print(f"\n Password Strength: {strength}")

def main():
    print("===  Password Complexity Checker ===")
    password = input("Enter a password to check: ").strip()
    check_password_strength(password)

if __name__ == "__main__":
    main()
