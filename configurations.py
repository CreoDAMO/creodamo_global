import os
import dj_database_url
from dynaconf import Dynaconf
from ai_ml import AIConfigAnalyzer
from iot import IoTConfigHandler
from plugin_store import PluginStore
from cloud_services import CloudConfigManager
from blockchain_logger import BlockchainLogger
from ansible_manager import AnsibleManager
from notification_system import NotificationSystem
from dynamic_config_loader import DynamicConfigLoader
from chaos_engine import ChaosEngine
from controlplane import Metrics
# Assuming celery_app is defined in your application
from your_application import celery_app

load_dotenv()

class AppConfig:

    metrics = Metrics()  # Initialize once and reuse

    def __init__(self):
        # Load and parse environment variables
        self.DEBUG = os.environ.get('DEBUG', False) 
        self.DATABASE_URL = dj_database_url.parse(os.environ['DATABASE_URL'])
        self.REDIS_URL = os.environ['REDIS_URL']

        # Expose metrics for Control Plane
        AppConfig.metrics.expose_metrics()

        # Configuration for Dynaconf
        self.settings = Dynaconf(
            environments=True,
            load_dotenv=True,
            settings_files=['settings.yaml', '.secrets.yaml']
        )

        # Initialize other components
        self.ai_analyzer = AIConfigAnalyzer()
        self.iot_handler = IoTConfigHandler()
        self.plugin_store = PluginStore()
        self.cloud_manager = CloudConfigManager()
        self.blockchain_logger = BlockchainLogger()
        self.ansible_manager = AnsibleManager()
        self.notification_system = NotificationSystem()
        self.dynamic_config_loader = DynamicConfigLoader()
        self.chaos_engine = ChaosEngine()

        # Configure Celery for Redis
        celery_app.conf.broker_url = self.REDIS_URL

    def get_setting(self, key):
        return self.settings.get(key)

# Additional configurations for logging, request tracing, etc. should be added here
