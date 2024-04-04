
def connect():
    raise NotImplementedError("function connect() not implemented")


def display_users(users: dict[int, str]) -> None:
    """
    Display users in the system to the console.

    Args:
        users (dict[int, str]): system users

    Returns:
        None
    """
    for k, v in users.items():
        print(f"User ID: {k}, Name: {v}")
    return None


def upload(file: str, *, quality: str, privacy: str) -> None:
    print(f"Uploading file: {file} with quality: {
          quality} and privacy: {privacy}")
    return None


def join_text(*strings: str, sep: str):
    # sep é automaticamente uma keyword-only argument
    return sep.join(strings)
