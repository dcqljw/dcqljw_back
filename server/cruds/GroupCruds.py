from sqlalchemy.orm import Session

from models import GroupModels
from schemas import GroupSchema
from utils import TokenUtils


def get_group(db: Session, group: GroupSchema.GroupFind):
    db.query(GroupModels.Group.group_name)
