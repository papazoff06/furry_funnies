def validate_name(name):
    for char in name:
        if not char.isalpha():
            raise ValueError("Your name must contain letters only!")

def validate_passcode_length(password):
    if not (5 < len(password) < 7):
        raise ValueError("Your passcode must be a combination of 6 digits")
