from app.health.models.health_model import HealthLivePublic

class HealthService:
    def __init__(self):
        pass
    
    def isLive(self) -> HealthLivePublic:
        status = HealthLivePublic()
        return status
