# creodamo.py

import argparse
from concurrent.futures import ThreadPoolExecutor
from blockchain_integration import BlockchainService
from ai_ml_services import EthicalAIML
from cloud_services import DecentralizedCloudService
from security_framework import CryptoSecurityManager
from community_engagement import CommunityEngagementPlatform
from regulatory_compliance import RegulatoryComplianceManager
from security_pipeline import SecurityPipeline

class CreoDAMO:
    """
    Main class for the CreoDAMO application, responsible for initializing
    and managing all services.
    """
    def __init__(self, debug: bool = False):
        """
        Initialize the CreoDAMO application.

        Args:
            debug (bool): If True, the application runs in debug mode.
        """
        self.debug = debug
        self.services = [
            BlockchainService(),
            EthicalAIML(),
            DecentralizedCloudService(),
            CryptoSecurityManager(),
            CommunityEngagementPlatform(),
            RegulatoryComplianceManager(),
            SecurityPipeline(),
        ]

    def start_services(self):
        """
        Start and manage all integrated services of the application.
        Using ThreadPoolExecutor to initialize services concurrently.
        """
        with ThreadPoolExecutor() as executor:
            future_to_service = {executor.submit(service.initialize): service for service in self.services}
            for future in future_to_service:
                service = future_to_service[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"Error initializing {service.__class__.__name__}: {str(e)}")

    def start(self):
        """
        Start the CreoDAMO application, initializing all services.
        """
        if self.debug:
            print("Starting CreoDAMO in debug mode...")
        self.start_services()

def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Run CreoDAMO Platform')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    creo_damo = CreoDAMO(debug=args.debug)
    creo_damo.start()
