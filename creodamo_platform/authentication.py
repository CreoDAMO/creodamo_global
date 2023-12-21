from creolang import CreoLangInterpreter
import jwt
from flask import request, jsonify
from rate_limiter import RateLimiter
from config import AppConfig
from functools import wraps

class Authentication:
    def __init__(self):
        self.config = AppConfig()
        self.creolang_interpreter = CreoLangInterpreter()
        self.rate_limiter = RateLimiter()
        self.secret_key = self.config.get_setting('SECRET_KEY')

    def execute_auth_script(self, script_name, context):
        # Execute a CreoLang script for custom authentication logic
        return self.creolang_interpreter.execute_script(script_name, context)

    def authenticate(self, token):
        # Rate limiting to prevent brute force attacks
        if not self.rate_limiter.is_allowed(token):
            raise Exception("Rate limit exceeded")

        # Custom CreoLang script for enhanced authentication logic
        context = {"token": token, "secret_key": self.secret_key}
        return self.execute_auth_script("authenticate_user.cl", context)

    def require_role(self, role):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                token = request.headers.get('Authorization')
                if not token:
                    return jsonify({'message': 'No token provided'}), 401

                context = {"token": token, "role": role, "secret_key": self.secret_key}
                result = self.execute_auth_script("verify_role.cl", context)
                if not result.get('is_allowed', False):
                    return jsonify({'message': 'Permission Denied'}), 403
                return func(*args, **kwargs)
            return wrapper
        return decorator

# Example usage of the Authentication class with CreoLang integration
auth = Authentication()

@app.route('/protected')
@auth.require_role('admin')
def protected_route():
    return jsonify({'message': 'Admin access granted'})

# Further routes and logic

