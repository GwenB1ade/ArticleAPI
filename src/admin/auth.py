from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'root'

ADMIN_DATA = {
    'name': 'Admin',
}

users = {
    "admin": {
        "name": "Admin",
        "avatar": "admin.png",
        "company_logo_url": "admin.png",
        "roles": ["read", "create", "edit", "delete", "action_make_published"],
    },
    "johndoe": {
        "name": "John Doe",
        "avatar": None, # user avatar is optional
        "roles": ["read", "create", "edit", "action_make_published"],
    },
    "viewer": {"name": "Viewer", "avatar": "guest.png", "roles": ["read"]},
}


class UsernameAndPasswordProvider(AuthProvider):
    """
    This is only for demo purpose, it's not a better
    way to save and validate user credentials
    """

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        if len(username) < 3:
            """Form data validation"""
            raise FormValidationError(
                {"username": "Ensure username has at least 03 characters"}
            )

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            """Save `username` in session"""
            request.session.update({"username": username})
            return response

        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        if request.session.get("username", None) == ADMIN_USERNAME:
            """
            Save current `user` object in the request state. Can be used later
            to restrict access to connected user.
            """
            return True

        return False

    def get_admin_config(self, request: Request) -> AdminConfig:
        # Update app title according to current_user
        return AdminConfig()

    def get_admin_user(self, request: Request) -> AdminUser:
        return AdminUser(username=request.session.get('username'))

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response