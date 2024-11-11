from fastapi import APIRouter
from controllers.health_controller import HealthController
from controllers.tutorial_controller import TutorialController
router = APIRouter(prefix="/api/v1")

# 컨트롤러 인스턴스 생성
health_controller = HealthController()
tutorial_controller = TutorialController()
# Health 관련 라우트
router.add_api_route(
    "/health",
    health_controller.health_check,
    methods=["GET"],
    tags=["Health"]
)

# Root 라우트
router.add_api_route(
    "/",
    health_controller.root,
    methods=["GET"],
    tags=["Root"]
) 

# Tutorial 라우트
router.add_api_route(
    "/tutorial",
    tutorial_controller.get_model,
    methods=["GET"],
    tags=["Tutorial"]
)