from typing import Generator, Dict, Any

class FacetContainer:
    def __init__(self, api_instance, facet_name: str, page_size: int = 20):
        self.api = api_instance
        self.facet_name = facet_name
        self.page_size = page_size

    def __iter__(self) -> Generator[Dict[str, Any], None, None]:
        page = 1
        while True:
            response = self.api.get(
                facet_name=self.facet_name, 
                page=page, 
                page_size=self.page_size
            )
            items = response.get('tags', [])
            if not items:
                break
            for item in items:
                yield item
            page += 1

