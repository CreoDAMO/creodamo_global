# creodamo.py

import argparse
import asyncio
import logging
import signal
from concurrent.futures import ProcessPoolExecutor
from typing import Dict, Optional

# Import modules from creodamo_modules package
from creodamo_modules import (
    BlockchainService,
    DecentralizedCloudService,
    CommunityEngagementPlatform,
    CreoLang,
    Documentation,
    FeatureFlags,
    GardenWatering,
    Governance,
    IncidentResponse,
    Internationalization,
    KubernetesDeployment,
    Monitoring,
    Monetization,
    ProofOfCreo,
    RegulatoryComplianceManager,
    CryptoSecurityManager,
    SecurityPipeline,
    ServiceMesh,
    Strategies,
    Trading,
    UserManagement,
    Utils,
    VenturesFund,
    WebSocket,
    RealmOfCreo,
)

# Import creodamo_ecommerce module
import creodamo_ecommerce

class CreoDAMO:
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.services: Dict[str, Service] = self.initialize_services()
        self.executor: Optional[ProcessPoolExecutor] = None
        self.event_loop: Optional[asyncio.AbstractEventLoop] = None

    def initialize_services(self) -> Dict[str, Service]:
        return {
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
            "monetization": Monetization(),
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
            "realm_of_creo": RealmOfCreo(),
            "creodamo_ecommerce": creodamo_ecommerce.CreoDAMOEcommerce(),  # E-commerce module
        }

    async def start_services(self):
        await asyncio.gather(*(service.start() for service in self.services.values()))

    async def stop_services(self):
        await asyncio.gather(*(service.stop() for service in self.services.values()))

    async def start(self):
        await self.start_services()
        # Main application logic here...

def configure_logging(debug: bool):
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

def handle_signals(loop: asyncio.AbstractEventLoop):
    loop.add_signal_handler(signal.SIGINT, loop.stop)
    loop.add_signal_handler(signal.SIGTERM, loop.stop)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    configure_logging(args.debug)

    creodamo = CreoDAMO(debug=args.debug)
    loop = asyncio.get_event_loop()
    handle_signals(loop)

    try:
        loop.run_until_complete(creodamo.start())
    except KeyboardInterrupt:
        print("CreoDAMO stopped by user.")
        loop.run_until_complete(creodamo.stop_services())
    configure_logging(args.debug)
    
    creodamo = CreoDAMO(debug=args.debug)
    loop = asyncio.get_event_loop()
    handle_signals(loop)

    try:
        loop.run_until_complete(creodamo.start())
    except KeyboardInterrupt:
        print("CreoDAMO stopped by user.")
        loop.run_until_complete(creodamo.stop_services())
