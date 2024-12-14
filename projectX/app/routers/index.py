from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/")
def index() -> str:
    return "hello_world"
