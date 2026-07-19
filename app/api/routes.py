from fastapi import APIRouter

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from app.services.auth_service import AuthService

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
    
@router.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = AuthService.get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered.",
        )

    new_user = AuthService.create_user(
        db,
        user,
    )

    return new_user