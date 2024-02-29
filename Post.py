import matplotlib.pyplot as plt
from PIL import Image
import User


class Post:
    """
    Initializes a Post instance with a type, information, and the user who published the post.

    Parameters:
        post_type (str): The type of the post.
        info (str): Additional information about the post.
        published (User): The user who published the post.

    Returns:
        None
    """
    def __init__(self, post_type, info, published):
        self.__post_type = post_type
        self.__info = info
        self.__published = published

    """
   Allows a user to like the post.

   Parameters:
       user (User): The user who likes the post.

   Returns:
       None

   Raises:
       Exception: If the user who published the post is offline.
   """
    def like(self, user):
        if self.__published.is_online():
            if self.__published is not user:
                print(f"notification to {self.__published.get_name()}: {user.get_name()} liked your post")
                notify = f"{user.get_name()} liked your post"
                self.__published.self_update(notify)
        else:
            raise Exception("Your user is disconnected")

    """
   Allows a user to comment on the post.

   Parameters:
       user (User): The user who comments on the post.
       text (str): The comment text.

   Returns:
       None

   Raises:
       Exception: If the user who published the post is offline.
   """
    def comment(self, user, text):
        if self.__published.is_online():
            if self.__published is not user:
                print(f"notification to {self.__published.get_name()}: {user.get_name()} commented on your post: {text}")
                notify = f"{user.get_name()} commented on your post"
                self.__published.self_update(notify)
        else:
            raise Exception("Your user is disconnected")

    """
    Returns the user who published the post.

    Parameters:
        None

    Returns:
        User: The user who published the post.
    """
    def get_published(self):
        return self.__published

    """
    Returns additional information about the post.

    Parameters:
        None

    Returns:
        str: Additional information about the post.
    """
    def get_info(self) -> str:
        return self.__info


class PostFactory:
    """
    Creates a new post of the specified type.

    Parameters:
        post_type (str): The type of post to create.
        published (User): The user who published the post.
        *args: Additional arguments required to create the post.

    Returns:
        Post: A Post object representing the newly created post.

    Raises:
        ValueError: If the specified post type is not supported.
    """
    def create_post(self, post_type, published, *args) -> Post:
        if post_type == "Text":
            info = args[0]
            return TextPost(info, published)
        elif post_type == "Image":
            image_name = args[0]
            return ImagePost(image_name, published)
        elif post_type == "Sale":
            # Unpack the arguments for SalePost
            title, price, location = args
            return SalePost(title, price, location, published)
        else:
            raise ValueError("Unsupported post type")


class TextPost(Post):
    """
    Initializes a TextPost instance with text information and the user who published the post.

    Parameters:
        info (str): Text information of the post.
        published (User): The user who published the post.

    Returns:
        None
    """
    def __init__(self, info, published):
        super().__init__("Text", info, published)
        print(self.__str__())

    """
    Returns a string representation of the TextPost instance.

    Parameters:
        None

    Returns:
        str: A string representing the TextPost instance.
    """
    def __str__(self):
        return f"{self.get_published().get_name()} published a post:\n\"{self.get_info()}\"\n"


class ImagePost(Post):
    """
    Initializes an ImagePost instance with image information and the user who published the post.

    Parameters:
        info (str): Filepath of the image.
        published (User): The user who published the post.

    Returns:
        None
    """
    def __init__(self, info, published):
        super().__init__("Image", info, published)
        print(self.__str__())

    """
   Displays the image post.

   Parameters:
       None

   Returns:
       None
   """
    def display(self):
        image = Image.open(self.get_info())
        plt.imshow(image)
        plt.axis('off')  # Turn off axis
        plt.show()
        print("Shows picture")

    """
    Returns a string representation of the ImagePost instance.

    Parameters:
        None

    Returns:
        str: A string representing the ImagePost instance.
    """
    def __str__(self):
        return f"{self.get_published().get_name()} posted a picture\n"



class SalePost(Post):
    """
    Initializes a SalePost instance with product information, price, location, and the user who published the post.

    Parameters:
        title (str): Title of the product.
        price (float): Price of the product.
        location (str): Pickup location of the product.
        published (User): The user who published the post.

    Returns:
        None
    """
    def __init__(self, title, price, location, published):
        super().__init__("Sale", title, published)
        self.__price = price
        self.__location = location
        self.__is_sold = False
        print(self.__str__())

    """
    Applies a discount to the product's price.

    Parameters:
        percent (float): The discount percentage.
        password (str): The user's password for verification.

    Returns:
        None

    Raises:
        Exception: If the product has already been sold or if the password is incorrect.
    """
    def discount(self, percent, password):
        if self.get_published().is_online():
            if self.__is_sold:
                print("The product has already been sold")
            else:
                if self.get_published().check_password(password):
                    self.__price -= (self.__price * percent) / 100
                    print(f"Discount on {self.get_published().get_name()} product! the new price is: {self.__price}")
                else:
                    raise Exception("The password is incorrect")
        else:
            raise Exception("Your user is disconnected")

    """
    Marks the product as sold.

    Parameters:
        password (str): The user's password for verification.

    Returns:
        None

    Raises:
        Exception: If the product has already been sold or if the password is incorrect.
    """
    def sold(self, password):
        if self.__is_sold:
            print("The product has already been sold")
        else:
            if self.get_published().check_password(password):
                self.__is_sold = True
                print(f"{self.get_published().get_name()}'s product is sold")
            else:
                raise Exception("The password is incorrect")

    # Returns a string representation of the SalePost instance.
    def __str__(self):
        if self.__is_sold:
            sold_str = "Sold!"
        else:
            sold_str = "For sale!"
        return f"{self.get_published().get_name()} posted a product for sale:\n{sold_str} {self.get_info()}, price: {self.__price}, pickup from: {self.__location}\n"
