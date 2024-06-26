from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost
import datetime

def create(db: Session , request: PostBase):
    new_post = DbPost(
    image_url = request.image_url,
    image_url_type = request.image_url_type,
    caption = request.caption,
    timestamp = datetime.datetime.now(),
    user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

