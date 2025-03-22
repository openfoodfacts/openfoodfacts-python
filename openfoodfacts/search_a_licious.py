import logging
from typing import Any, Dict, List, Optional, Union

import requests

from .types import APIConfig, SearchFilter, SearchFacet, JSONType

logger = logging.getLogger(__name__)


class SearchALiciousResource:
    """Resource class for interacting with the search-a-licious API."""

    def __init__(self, api_config: APIConfig):
        self.api_config = api_config
        self.base_url = "https://search.openfoodfacts.org"
        
    def search(
        self,
        query: Optional[str] = None,
        filters: Optional[List[Union[Dict[str, Any], SearchFilter]]] = None,
        sort_by: Optional[Union[str, List[str]]] = None,
        facets: Optional[List[Union[Dict[str, Any], SearchFacet]]] = None,
        page: int = 1,
        page_size: int = 20,
        langs: Optional[Union[str, List[str]]] = None,
        index_id: Optional[str] = None,
        **kwargs,
    ) -> JSONType:
        """
        Perform an advanced search using the search-a-licious endpoint.
        
        Parameters:
        -----------
        query : str, optional
            The search query text
        filters : list of dict or SearchFilter, optional
            Advanced filters to apply to the search
        sort_by : str or list, optional
            Field(s) to sort results by
        facets : list of dict or SearchFacet, optional
            Facets to retrieve with the search results
        page : int, optional
            Page number (default: 1)
        page_size : int, optional
            Number of results per page (default: 20)
        langs : str or list, optional
            Languages to search in (comma-separated string or list of strings)
        index_id : str, optional
            Index ID to use for the search
        **kwargs : dict
            Additional parameters to pass to the search-a-licious endpoint
        
        Returns:
        --------
        dict
            Search results
        """
        payload = {
            "page": page,
            "page_size": page_size,
        }
        
        if query:
            payload["query"] = query
            
        if filters:
            processed_filters = []
            for f in filters:
                if isinstance(f, SearchFilter):
                    processed_filters.append(f.model_dump(exclude_none=True))
                else:
                    processed_filters.append(f)
            payload["filters"] = processed_filters
            
        if sort_by:
            payload["sort_by"] = sort_by
            
        if facets:
            processed_facets = []
            for f in facets:
                if isinstance(f, SearchFacet):
                    processed_facets.append(f.model_dump(exclude_none=True))
                else:
                    processed_facets.append(f)
            payload["facets"] = processed_facets
            
        if langs:
            if isinstance(langs, list):
                payload["langs"] = ",".join(langs)
            else:
                payload["langs"] = langs
                
        if index_id:
            payload["index_id"] = index_id

        payload.update(kwargs)
        
        try:
            response = requests.post(
                f"{self.base_url}/search",
                json=payload,
                headers={"User-Agent": self.api_config.user_agent},
                timeout=self.api_config.timeout,
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Search request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"Error response: {error_data}")
                except ValueError:
                    logger.error(f"Error response: {e.response.text}")
            raise
    
    def search_get(
        self,
        query: Optional[str] = None,
        filters: Optional[List[Union[Dict[str, Any], SearchFilter]]] = None,
        sort_by: Optional[Union[str, List[str]]] = None,
        facets: Optional[List[Union[Dict[str, Any], SearchFacet]]] = None,
        page: int = 1,
        page_size: int = 20,
        langs: Optional[Union[str, List[str]]] = None,
        index_id: Optional[str] = None,
        **kwargs,
    ) -> JSONType:
        """
        Perform an advanced search using the search-a-licious GET endpoint.
        
        This method is useful for simpler queries and can be cached by browsers and proxies.
        
        Parameters:
        -----------
        query : str, optional
            The search query text
        filters : list of dict or SearchFilter, optional
            Advanced filters to apply to the search
        sort_by : str or list, optional
            Field(s) to sort results by
        facets : list of dict or SearchFacet, optional
            Facets to retrieve with the search results
        page : int, optional
            Page number (default: 1)
        page_size : int, optional
            Number of results per page (default: 20)
        langs : str or list, optional
            Languages to search in (comma-separated string or list of strings)
        index_id : str, optional
            Index ID to use for the search
        **kwargs : dict
            Additional parameters to pass to the search-a-licious endpoint
        
        Returns:
        --------
        dict
            Search results
        """
        params = {
            "page": page,
            "page_size": page_size,
        }
        
        if query:
            params["q"] = query
            
        if sort_by:
            if isinstance(sort_by, list):
                params["sort_by"] = ",".join(sort_by)
            else:
                params["sort_by"] = sort_by
                
        if langs:
            if isinstance(langs, list):
                params["langs"] = ",".join(langs)
            else:
                params["langs"] = langs
                
        if index_id:
            params["index_id"] = index_id
            
        # Note: GET requests are more limited and cannot handle complex filters/facets
        # We'll raise a warning if these are provided
        if filters:
            logger.warning("Filters may not be fully supported in GET requests. Consider using search() with POST instead.")
            # Convert filters to a simplified format if possible
            
        if facets:
            logger.warning("Facets may not be fully supported in GET requests. Consider using search() with POST instead.")
           

        params.update(kwargs)
        
        try:
            response = requests.get(
                f"{self.base_url}/search",
                params=params,
                headers={"User-Agent": self.api_config.user_agent},
                timeout=self.api_config.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Search GET request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"Error response: {error_data}")
                except ValueError:
                    logger.error(f"Error response: {e.response.text}")
            raise
            
    def autocomplete(
        self,
        q: str,
        taxonomy_names: Union[str, List[str]],
        langs: Optional[Union[str, List[str]]] = "en",
        size: int = 10,
        fuzziness: Optional[int] = None,
        index_id: Optional[str] = None,
    ) -> JSONType:
        """
        Use the autocomplete endpoint for taxonomy-based autocompletion.
        
        Parameters:
        -----------
        q : str
            The autocomplete query
        taxonomy_names : str or list
            Name(s) of the taxonomy to search in
        langs : str or list, optional
            Languages to search in (default: "en")
        size : int, optional
            Number of results to return (default: 10)
        fuzziness : int, optional
            Fuzziness level to use
        index_id : str, optional
            Index ID to use
            
        Returns:
        --------
        dict
            Autocomplete results
        """
        params = {"q": q}
        
        if isinstance(taxonomy_names, list):
            params["taxonomy_names"] = ",".join(taxonomy_names)
        else:
            params["taxonomy_names"] = taxonomy_names
        
        if langs:
            if isinstance(langs, list):
                params["langs"] = ",".join(langs)
            else:
                params["langs"] = langs
        
        params["size"] = size
        
        if fuzziness is not None:
            params["fuzziness"] = fuzziness
        
        if index_id:
            params["index_id"] = index_id
        
        try:
            response = requests.get(
                f"{self.base_url}/autocomplete",
                params=params,
                headers={"User-Agent": self.api_config.user_agent},
                timeout=self.api_config.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Autocomplete request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"Error response: {error_data}")
                except ValueError:
                    logger.error(f"Error response: {e.response.text}")
            raise
    
    def parse_search_response(self, response_data: JSONType) -> Dict[str, Any]:
        """
        Parse the search response into a more structured format.
        
        Parameters:
        -----------
        response_data : dict
            The raw response data from the search API
            
        Returns:
        --------
        dict
            A structured representation of the search results
        """
        if not response_data.get("is_success", False):
            raise ValueError(f"Search failed: {response_data.get('error', 'Unknown error')}")
        
        results = {
            "count": response_data.get("count", 0),
            "page": response_data.get("page", 1),
            "page_size": response_data.get("page_size", 20),
            "page_count": response_data.get("page_count", 0),
            "items": response_data.get("items", []),
        }
        
        if "aggregations" in response_data:
            results["facets"] = response_data.get("aggregations", {})
        
        return results
    
    def get_document(self, identifier: str, index_id: Optional[str] = None) -> JSONType:
        """
        Fetch a document from Elasticsearch with a specific ID.
        
        Parameters:
        -----------
        identifier : str
            The document identifier
        index_id : str, optional
            Index ID to use
            
        Returns:
        --------
        dict
            The document data
        """
        params = {}
        if index_id:
            params["index_id"] = index_id
            
        try:
            response = requests.get(
                f"{self.base_url}/document/{identifier}",
                params=params,
                headers={"User-Agent": self.api_config.user_agent},
                timeout=self.api_config.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Get document request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"Error response: {error_data}")
                except ValueError:
                    logger.error(f"Error response: {e.response.text}")
            raise