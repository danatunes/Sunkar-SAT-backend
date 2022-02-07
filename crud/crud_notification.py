from typing import Optional, List

from app.crud.base import CRUDBase
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate


class CRUDNotification(CRUDBase[Notification, NotificationCreate, NotificationUpdate]):
    def read_notifications_by_user_id(self, db, *, skip, limit, user_id) -> Optional[List[Notification]]:
        notifications = db.query(Notification).filter(Notification.user_id == user_id).offset(skip).limit(
            limit).all()
        return notifications


notification = CRUDNotification(Notification)
