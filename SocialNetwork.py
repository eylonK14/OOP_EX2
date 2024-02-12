import User
class SocialNetwork:
    users = {}  # iniat map of names so we won't have any name  more than once
    def sign_up(name: str, password: str):
        key = name + ", " + password
        if (not len(password) in range(4, 9) or  users.__contains__(name)):
            user = User(name,password)

            return user