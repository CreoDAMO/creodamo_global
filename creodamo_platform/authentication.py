import jwt
from flask import request, jsonify
from rate_limiter import RateLimiter
from config import AppConfig

class Authentication:

    def __init__(self):
        self.config = AppConfig()
        self.rate_limiter = RateLimiter()
        self.secret_key = self.config.get_setting('SECRET_KEY')

    def authenticate(self, token):
        if not self.rate_limiter.is_allowed(token):
            raise Exception("Rate limit exceeded")
        return jwt.decode(token, self.secret_key, algorithms=["HS256"])

    def require_role(self, role):
        pass
