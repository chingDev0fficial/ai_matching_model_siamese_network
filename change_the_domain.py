def change_domain(email: str, new_domain: str) -> str:
    delimiter = "@"
    email_split = email.split(delimiter)
    new_email = email_split[0] + delimiter + new_domain
    return new_email

email: str = input("Enter email: ")
new_email: str = change_domain(email, "example.com")
print(f"Output: {new_email}")