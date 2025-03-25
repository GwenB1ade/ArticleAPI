import jwt
import datetime

from fastapi import HTTPException

from config import settings
from schemas.user_schemas import ViewUserSchema

class UserJwt:
    time = datetime.timedelta(days = 21)
    
    @classmethod
    def create_jwt_token(cls, data: ViewUserSchema, time: datetime.timedelta = time) -> str:
        """Creates a JWT token

        Args:
            data (ViewUserSchema): User data
            time (datetime.timedelta, optional): Token lifetime. Defaults to time.

        Returns:
            str: JWT token
        """
        payload = {
            'data': data.model_dump(),
            'exp': datetime.datetime.now(datetime.timezone.utc) + time
        }
        
        token = jwt.encode(
            payload = payload,
            key = settings.JWT_SECRET,
            algorithm = settings.JWT_ALGORITHM
        )
        
        return token
    
    @classmethod
    def decode_token(self, token: str) -> ViewUserSchema:
        """Decodes the token into the model

        Args:
            token (str): JWT token

        Raises:
            HTTPException: HTTP error, caused when the token's lifetime expires

        Returns:
            ViewUserSchema: User data
        """
        
        try:
            userdata = jwt.decode(
                jwt = token,
                key = settings.JWT_SECRET,
                algorithms = settings.JWT_ALGORITHM
            )
            
            schema = ViewUserSchema(
                uuid = userdata['data']['uuid'],
                username = userdata['data']['username']
            )
            
            return schema
        
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code = 400,
                detail = {
                    'error_message': 'The time of the token has expired. Log in again'
                }
            )