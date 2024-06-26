from pydantic import BaseModel
from typing import List, Optional

class CrawlRequest(BaseModel):
    search: List[str]
    quantity: Optional[int] = 20

    def __hash__(self):
        return hash((self.source, tuple(self.search), self.quantity))
    
class WordCloudRequest(BaseModel):
    text: str