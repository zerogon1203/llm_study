class HealthService:
    def check_health(self):
        return {"status": "healthy"}
    
    def get_welcome_message(self):
        return {"message": "Welcome to FastAPI Project"} 