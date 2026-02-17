from typing import List, Any, Optional

class FacetContainer:
    def __init__(self, facet_name: str = "unknown", data: Optional[List[Any]] = None, page_size: int = 20):
        self.facet_name = facet_name
        self.data = data or []
        self.page_size = page_size  
        self.current_page = 1  
    def get_page(self, page_number: int) -> list:
        if page_number < 1:
            return []  
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size 
        return self.data[start_index:end_index]

    @property
    def total_pages(self) -> int:
        if not self.data:
            return 0
        return (len(self.data) + self.page_size - 1) // self.page_size
