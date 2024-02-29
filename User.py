# Ran Mizrahi 314809625
# Shmuel Ben-Attar 208007138
# User.py

import Post


class User:
    """
    Initializes a User instance with a username, password, and sets the user as online by default.

    Parameters:
        name (str): The username of the user.
        password (str): The password of the user.

    Returns:
        None
    """
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__online = True
        self.__posts = 0
        self.__followers = []
        self.__notifications = []

    """
    Allows the user to follow another user.

    Parameters:
        user (User): The user to be followed.

    Returns:
        None

    Raises:
        Exception: If the user is already following the specified user or if the user is offline.
    """
    def follow(self, user):
        if self.__online:
            if self not in user.__followers:
                user.__followers.append(self)
                print(self.__name, "started following", user.get_name())
            else:
                raise Exception("You are already following this user")
        else:
            raise Exception("Your user is disconnected")

    """
    Allows the user to unfollow another user.

    Parameters:
        user (User): The user to be unfollowed.

    Returns:
        None

    Raises:
        Exception: If the user has not followed the specified user or if the user is offline.
    """
    def unfollow(self, user):
        if self.__online:
            if self in user.__followers:
                user.__followers.remove(self)
                print(self.__name, "unfollowed", user.get_name())
            else:
                raise Exception("You have not followed this user")
        else:
            raise Exception("Your user is disconnected")

    """
    Publishes a new post by the user.

    Parameters:
        post_type (str): The type of post to be created.
        *args: Additional arguments required to create the post.

    Returns:
        Post: A Post object representing the newly created post.

    Raises:
        Exception: If the user is offline.
    """
    def publish_post(self, post_type, *args) -> Post:
        if self.__online:
            new_post = Post.PostFactory().create_post(post_type, self, *args)
            notify = f"{self.__name} has a new post"
            self.update_followers(notify)
            self.__posts += 1

            return new_post

        else:
            raise Exception("Your user is disconnected")

    """
    Notifies followers about updates.

    Parameters:
        notify (str): Notification message to be sent to followers.

    Returns:
        None
    """
    def update_followers(self, notify):
        for user in self.__followers:
            user.__notifications.append(notify)

    """
    Notifies the user about updates.

    Parameters:
        notify (str): Notification message to be sent to the user.

    Returns:
        None
    """
    def self_update(self, notify):
        self.__notifications.append(notify)

    """
    Checks if the provided password matches the user's password.

    Parameters:
        password (str): The password to be checked.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    def check_password(self, password) -> bool:
        if self.__password == password:
            return True

        return False

    """
    Returns the user's password.

    Parameters:
        None

    Returns:
        str: The password of the user.
    """
    def get_password(self) -> str:
        return self.__password

    """
    Returns the username of the user.

    Parameters:
        None

    Returns:
        str: The username of the user.
    """
    def get_name(self) -> str:
        return self.__name

    """
    Sets the online status of the user.

    Parameters:
        T_F (bool): True if the user is online, False otherwise.

    Returns:
        None
    """
    def set_online(self, T_F):
        self.__online = T_F

    """
    Checks if the user is online.

    Parameters:
        None

    Returns:
        bool: True if the user is online, False otherwise.
    """
    def is_online(self):
        return self.__online

    """
    Returns a string representation of the user, including username, number of posts, and number of followers.

    Parameters:
        None

    Returns:
        str: A string representing the user.
    """
    def __str__(self):
        return f"User name: {self.__name}, Number of posts: {self.__posts}, Number of followers: {len(self.__followers)}"

    """
   Prints notifications for the user.

   Parameters:
       None

   Returns:
       None
   """
    def print_notifications(self):
        if self.__notifications:
            print(f"{self.__name}'s notifications:")
            for notification in self.__notifications:
                print(notification)
        else:
            print(f"No notifications for {self.__name}")


