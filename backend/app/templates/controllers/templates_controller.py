from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4

from app.common.dependencies.check_token_header import check_token_header
from app.templates.models.templates_model import Template, TemplateCreate
from app.templates.services.templates_service import templatesService


router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    dependencies=[Depends(check_token_header)],
)


@router.get("/{template_id}", response_model=Template)
async def get_template(template_id: UUID4):
    template = await templatesService.get_template(template_id)
    return template


@router.get("/")
async def list_templates():
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.post("/", response_model=Template)
async def create_template(template_create: TemplateCreate):
    template = await templatesService.create_template(template_create)
    return template


@router.patch("/{template_id}")
async def update_template(template_id: UUID4):
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.delete("/{template_id}")
async def delete_template(template_id: UUID4):
    raise HTTPException(status_code=405, detail="Method Not Allowed")


@router.put("/{template_id}")
async def replace_template(template_id: UUID4):
    raise HTTPException(status_code=405, detail="Method Not Allowed")
