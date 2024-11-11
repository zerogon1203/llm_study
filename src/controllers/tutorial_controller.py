from services.tutorial_service import TutorialService

class TutorialController:
    def __init__(self):
        self.tutorial_service = TutorialService()
    
    async def get_model(self):
        return self.tutorial_service.get_model()