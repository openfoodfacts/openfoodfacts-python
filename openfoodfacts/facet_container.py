import time
import logging
from typing import Generator, Any, Dict, Optional
from openfoodfacts.types import Facet

logger = logging.getLogger(__name__)

class FacetContainer:
    def __init__(self, api_instance, facet_name: str, page_size: int = 20, data_key: str = 'tags'):
        self.api = api_instance
        self.facet = Facet.from_str_or_enum(facet_name)
        self.data_key = data_key
        self.page_size = page_size

    def _fetch_page_with_retry(self, page: int, max_retries: int = 3) -> Dict[str, Any]:
        for attempt in range(max_retries):
            try:
                # The actual network request
                return self.api.get(
                    facet_name=self.facet.value, 
                    page=page, 
                    page_size=self.page_size
                )
            except Exception as e:
                logger.warning(f"Network error on page {page}, attempt {attempt + 1}: {e}")
                if attempt == max_retries - 1:
                    raise ConnectionError(f"Failed to fetch page {page} after {max_retries} attempts.") from e
                time.sleep(2)
        return {} 

    def __iter__(self) -> Generator[Dict[str, Any], None, None]:
    
        page = 1
        while True:
            response = self._fetch_page_with_retry(page)
            
            items = response.get(self.data_key, [])
            if not items:
                break
            yield from items
            
            page += 1

