from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to GenAI TalentHub 🚀"
    }


@router.get("/about", tags=["General"])
def about():
    return {
        "project": "GenAI TalentHub",
        "backend": "FastAPI",
        "database": "PostgreSQL",
        "ai": "Coming Soon"
    }


@router.get("/health", tags=["General"])
def health():
    return {
        "status": "healthy"
    }