# creodamo.py

import argparse
import argparse
import asyncio
import logging
import signal
import sys
from concurrent.futures import ProcessPoolExecutor
from typing import Any, Dict, Optional

import aiohttp

from blockchain_integration import BlockchainService
from cloud_services import DecentralizedCloudService
from community_engagement import CommunityEngagementPlatform   
from creolang import CreoLang
from documentation import Documentation
from feature_flags import FeatureFlags
from garden_watering import GardenWatering
from governance import Governance
from incident_response import IncidentResponse   
from internationalization import Internationalization
from kubernetes_deployment import KubernetesDeployment
from monitoring import Monitoring
from monetization import Monetization
from proof_of_creo import ProofOfCreo
from regulatory_compliance import RegulatoryComplianceManager
from security_framework import CryptoSecurityManager
from security_pipeline import SecurityPipeline
from service_mesh import ServiceMesh
from strategies import Strategies
from trading import Trading
from user import UserManagement
from utils import Utils
from ventures_fund import VenturesFund
from websocket import WebSocket
from dynaconf import settings


class CreoDAMO:
    def __init__(self, debug: bool = False) -> None:
        self.services: Dict[str, Any] = {
            "blockchain_service": BlockchainService(),
            "decentralized_cloud_service": DecentralizedCloudService(),
            "community_engagement_platform": CommunityEngagementPlatform(),
            "creolang": CreoLang(),
            "documentation": Documentation(),
            "feature_flags": FeatureFlags(),
            "garden_watering": GardenWatering(),
            "governance": Governance(),
            "incident_response": IncidentResponse(),
            "internationalization": Internationalization(),
            "kubernetes_deployment": KubernetesDeployment(),
            "monitoring": Monitoring(),
            "proof_of_creo": ProofOfCreo(),
            "regulatory_compliance": RegulatoryComplianceManager(),
            "crypto_security_manager": CryptoSecurityManager(),
            "security_pipeline": SecurityPipeline(),
            "service_mesh": ServiceMesh(),
            "strategies": Strategies(),
            "trading": Trading(),
            "user_management": UserManagement(),
            "utils": Utils(),
            "ventures_fund": VenturesFund(),
            "websocket": WebSocket(),
            "monetization": Monetization(),
        }
        self.debug = debug
        self.executor: Optional[ProcessPoolExecutor] = None
        self.event_loop: Optional[asyncio.AbstractEventLoop] = None

    def initialize_service(self, name: str, service: Any) -> None:
        try:
            service.initialize()
            logging.info(f"{name} initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing {name}: {str(e)}")
            # Handle initialization errors here

    async def start_services(self) -> None:
        self.executor = ProcessPoolExecutor()
        self.event_loop = asyncio.get_event_loop()
        futures = []
        for name, service in self.services.items():
            future = self.event_loop.run_in_executor(self.executor, self.initialize_service, name, service)
            futures.append(future)

        # Wait for all service initialization to complete
        await asyncio.gather(*futures)

    def stop_services(self) -> None:
        if self.executor is not None:
            self.executor.shutdown()  # Properly terminate the executor and cleanup resources
            logging.info("All services stopped")

    async def start(self) -> None:
        if self.debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("Starting CreoDAMO in debug mode...")
        else:
            logging.basicConfig(level=logging.INFO)

        await self.start_services()

        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)
        logging.info("CreoDAMO started successfully")

        try:
            while True:
                await asyncio.sleep(3600)  # Keep the event loop running
        except asyncio.CancelledError:
            pass

    def stop(self, signum: int, frame: Any) -> None:
        logging.info("Stopping CreoDAMO...")
        self.stop_services()
        if self.event_loop is not None:
            self.event_loop.stop()
        logging.info("CreoDAMO stopped gracefully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Debug mode')
    args = parser.parse_args()

    creo_damo = CreoDAMO(debug=args.debug)

    try:
        asyncio.run(creo_damo.start())
    except KeyboardInterrupt:
        sys.exit(0)
