from pydantic import BaseModel
from datetime import datetime

class PostsDisplay(BaseModel):
    id: int
    title: str
    image: str = None
    is_activ: bool
    text: str
    created_at: datetime
    post_category_id: int
    # post_category = relationship("DbPostCategory", back_populates="category")
    
    class Config():
        orm_mode = True