"""Data management interactions."""

from fastapi import APIRouter
from services.data_management import generate_message
from schemas.message import MessageInput as Message

router = APIRouter(tags=["Management API"])


@router.post("/new-message/{service_uuid}/{target_username}")
async def message_service(
        message: Message,
        service_uuid: str,
        target_username: str
):
    return generate_message(target_service=service_uuid,
                            message_content=message.content,
                            target_username=target_username)

