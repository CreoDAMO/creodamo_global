# configuration.py

import os
import dj_database_url
from dynaconf import Dynaconf
from dotenv import load_dotenv
from creolang import CreoLangInterpreter
from ansible_manager import AnsibleManager
from cloud_services import CloudConfigManager
from blockchain_logger import BlockchainLogger
from dynamic_config_loader import DynamicConfigLoader
from chaos_engine import ChaosEngine
from controlplane import Metrics
from your_application import celery_app
from ci_cd_pipeline_manager import CICDPipelineManager
from rbac_manager import RBACManager
from centralized_logger import CentralizedLogger
from siem_manager import SIEMManager
from threat_intelligence_manager import ThreatIntelligenceManager
from bug_bounty_platform import BugBountyPlatform
from service_mesh_integration import ServiceMeshIntegration
from canary_deployment_manager import CanaryDeploymentManager
from grafana_dashboard_manager import GrafanaDashboardManager
from secure_communication import SecureCommunication
from audit_logger import AuditLogger
from security_compliance import SecurityCompliance

class AppConfig:
    def __init__(self):
        load_dotenv()

        self.DEBUG = os.getenv('DEBUG', False) 
        self.DATABASE_URL = dj_database_url.parse(os.getenv('DATABASE_URL'))
        self.REDIS_URL = os.getenv('REDIS_URL')

        self.settings = Dynaconf(
            environments=True,
            load_dotenv=True,
            settings_files=['settings.yaml', '.secrets.yaml']
        )

        self.creolang = CreoLangInterpreter()
        self.ansible_manager = AnsibleManager()
        self.cloud_manager = CloudConfigManager()
        self.blockchain_logger = BlockchainLogger()
        self.dynamic_config_loader = DynamicConfigLoader()
        self.chaos_engine = ChaosEngine()
        self.metrics = Metrics()
        self.ci_cd_pipeline_manager = CICDPipelineManager()
        self.rbac_manager = RBACManager()
        self.centralized_logger = CentralizedLogger()
        self.siem_manager = SIEMManager()
        self.threat_intelligence_manager = ThreatIntelligenceManager()
        self.bug_bounty_platform = BugBountyPlatform()
        self.service_mesh = ServiceMeshIntegration()
        self.canary_deployment_manager = CanaryDeploymentManager()
        self.grafana_dashboard_manager = GrafanaDashboardManager()
        self.secure_communication = SecureCommunication()
        self.audit_logger = AuditLogger()
        self.security_compliance = SecurityCompliance()

        celery_app.conf.broker_url = self.REDIS_URL

    def get_setting(self, key):
        return self.settings.get(key)

    # Additional methods for each manager
    # Security enhancements for each manager

# Instantiate AppConfig
app_config = AppConfig()
