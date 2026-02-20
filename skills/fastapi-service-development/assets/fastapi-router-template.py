from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/v1/resources", tags=["resources"])

class CreateResourceRequest(BaseModel):
    name: str

class ResourceResponse(BaseModel):
    id: str
    name: str

@router.post("", response_model=ResourceResponse, status_code=201)
async def create_resource(payload: CreateResourceRequest, service=Depends(get_resource_service)):
    try:
        return await service.create(payload)
    except DomainConflictError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
