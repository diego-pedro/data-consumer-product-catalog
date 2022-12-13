"""Service implementation."""

from fastapi import APIRouter
from services.data_management import get_latest_message_id, process_message
from schemas.user import UserSession

router = APIRouter(tags=["Service API"])


@router.post("/notification")
async def get_notification(user_session: UserSession):
    newest_message = get_latest_message_id(user_session.email)

    if newest_message:
        return {"Latest Message": process_message(newest_message)}
    else:
        return {"detail": "Notifications up to date."}
