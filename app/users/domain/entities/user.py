import uuid
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True,slots=True)
class UserEntity:
    id: uuid.UUID
    username: str
    password: str
    created_at: datetime