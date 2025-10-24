from fastapi import APIRouter, Depends, HTTPException
from app.models import GenerateRequest, ContentResponse
from app.services import ContentService, content_service

router = APIRouter()

@router.post("/generate", response_model=ContentResponse)
def generate_content(
    request: GenerateRequest,
    service: ContentService = Depends(lambda: content_service)
):
    try:
        result = service.generate_content(request)
        return ContentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))