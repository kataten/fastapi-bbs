from pydantic import BaseModel

#共通部分(content parent_post_id)
class PostBase(BaseModel):
    content: str
    parent_post_id: int | None = None
    
    
#新規作成用(idやcreated_atは不要）
class PostCreate(PostBase):
    pass

#レスポンス用(id created_atが追加)
class PostResponse(PostBase):
    id: int
    thread_id: int
    post_number: int
    created_at: str