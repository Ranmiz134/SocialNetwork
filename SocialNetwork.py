# Ran Mizrahi 314809625
# Shmuel Ben-Attar 208007138
# SocialNetwork.py

from User import User


class SocialNetwork:
    _instance = None

    """
    Constructs a new instance of the SocialNetwork class.

    Parameters:
        cls (class): The class itself.
        name (str): A string representing the name of the social network.

    Returns:
        SocialNetwork: An instance of the SocialNetwork class.
    """
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    """
    Initializes the SocialNetwork instance with a name and an empty list of users.

    Parameters:
        name (str): A string representing the name of the social network.

    Returns:
        None
    """
    def __init__(self, name):
        self.__name = name
        self.__users = []
        self.print_create()

    """
    Registers a new user to the social network.

    Parameters:
        user_name (str): A string representing the username of the new user.
        password (str): A string representing the password of the new user.

    Returns:
        User: A User object representing the newly created user if successful, otherwise None.
    """
    def sign_up(self, user_name, password) -> User:
        # Check if the username already exists
        for user in self.__users:
            if user_name == user.get_name():
                print("User with the same name already exists.")
                return None

        # Check password length
        if len(password) < 4 or len(password) > 8:
            print("Password must be between 4 and 8 characters.")
            return None

        # Create and add the new user
        new_user = User(user_name, password)
        self.__users.append(new_user)
        return new_user

    """
    Logs in a user to the social network.

    Parameters:
        user_name (str): A string representing the username of the user.
        password (str): A string representing the password of the user.

    Returns:
        None
    """
    def log_in(self, user_name, password):
        for user in self.__users:
            if user.get_name() == user_name and user.get_password() == password:
                if user.is_online():
                    raise Exception("The user is already logged in")
                else:
                    user.set_online(True)
                    print(user_name, "connected")

    """
    Logs out a user from the social network.

    Parameters:
        user_name (str): A string representing the username of the user.

    Returns:
        None
    """
    def log_out(self, user_name):
        for user in self.__users:
            if user.get_name() == user_name:
                if user.is_online():
                    user.set_online(False)
                    print(user_name, "disconnected")
                else:
                    raise Exception("The user is already logged out")

    """
    Prints a message indicating the creation of the social network.

    Parameters:
        None

    Returns:
        None
    """
    def print_create(self):
        print("The social network", self.__name, "was created!")

    """
    Returns a string representation of the social network and its users.

    Parameters:
        None

    Returns:
        str: A string representing the social network and its users.
    """
    def __str__(self):
        str = f"{self.__name} social network:\n"
        for user in self.__users:
            str += f"{user.__str__()}\n"

        return str






