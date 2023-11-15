from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        ### v3t3 ###
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Use characters between a-z for username")
        ### v3t3 ###
        if not len(username) >= 3:
            raise UserInputError("Username need to be at least 3 characters")
        ### v3t3 ###
        if re.match("^[a-z]+$", username) and len(username) >= 3:
            
            if len(password) < 8:
                raise UserInputError("Password need to be 8 characters long")
            
            if re.match("^[a-z]+$", password):
                raise UserInputError("Password can not contain only characters between a-z")
        

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
