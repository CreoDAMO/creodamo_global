# trading.py
import os
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from security import (
    enforce_https,
    authenticate_request,
    apply_headers,
    enable_rbac,
    encrypt_data,
    TwoFactorAuth,
    AdaptiveHoneypots,
    QuantumResistantEncryption
)
from infrastructure import (
    init_microservices,
    setup_zero_trust_network
)
