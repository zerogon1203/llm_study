from services.health_service import HealthService

class HealthController:
    def __init__(self):
        self.health_service = HealthService()
    
    async def health_check(self):
        return self.health_service.check_health()
    
    async def root(self):
        return self.health_service.get_welcome_message() 