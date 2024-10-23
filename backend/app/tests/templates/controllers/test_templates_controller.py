import pytest

from app.templates.models.templates_model import TemplateCreate, AssistantType


@pytest.mark.asyncio
async def test_get_template(async_client, auth_header, test_template_id) -> None:
    # Act
    response = await async_client.get(
        f"/api/v1/templates/{test_template_id}", headers=auth_header
    )
    # Assert
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_template(async_client, auth_header, test_user_id) -> None:
    # Act
    template = TemplateCreate(
        user_id=test_user_id,
        title="Batman Template",
        prompt="Wie finde ich, Batman, einen neuen Job?",
        assistant_type=AssistantType.QUESTIONER,
    )
    response = await async_client.post(
        "/api/v1/templates", headers=auth_header, json={template.model_dump()}
    )
    # Assert
    assert response.status_code == 200


# +-------------------------+
# | Not Implemented Methods |
# +-------------------------+


@pytest.mark.asyncio
async def test_list_templates(async_client, auth_header) -> None:
    # Act
    response = await async_client.get("/api/v1/templates/", headers=auth_header)
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_update_template(async_client, auth_header, test_template_id) -> None:
    # Act
    response = await async_client.patch(
        f"/api/v1/templates/{test_template_id}", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_delete_template(async_client, auth_header, test_template_id) -> None:
    # Act
    response = await async_client.delete(
        f"/api/v1/templates/{test_template_id}", headers=auth_header
    )
    # Assert
    assert response.status_code == 405


@pytest.mark.asyncio
async def test_replace_template(async_client, auth_header, test_template_id) -> None:
    # Act
    response = await async_client.put(
        f"/api/v1/templates/{test_template_id}", headers=auth_header, json={}
    )
    # Assert
    assert response.status_code == 405
