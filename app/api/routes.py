from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to GenAI TalentHub 🚀"
    }


@router.get("/about")
def about():
    return {
        "project": "GenAI TalentHub",
        "backend": "FastAPI",
        "database": "PostgreSQL",
        "ai": "Coming Soon"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }