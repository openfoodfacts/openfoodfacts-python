import enum
from typing import Optional

from pydantic import BaseModel


class Flavor(str, enum.Enum):
    """Flavor is used to refer to a specific Open*Facts project:

    - Open Food Facts
    - Open Beauty Facts
    - Open Pet Food Facts
    - Open Product Facts
    - Open Food Facts (Pro plateform)
    """

    off = "off"
    obf = "obf"
    opff = "opff"
    opf = "opf"
    off_pro = "off-pro"

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def get_base_domain(self) -> str:
        """Get the base domain (domain without TLD and without world/api
        subdomain) associated with the `Flavor`."""
        if self == self.off:
            return "openfoodfacts"
        elif self == self.obf:
            return "openbeautyfacts"
        elif self == self.opff:
            return "openpetfoodfacts"
        elif self == self.opf:
            return "openproductfacts"
        else:
            # Open Food Facts Pro
            return "pro.openfoodfacts"

    @classmethod
    def get_from_server_domain(cls, server_domain: str) -> "Flavor":
        """Get the `Flavor` associated with a `server_domain`."""
        subdomain, base_domain, tld = server_domain.rsplit(".", maxsplit=2)

        if subdomain == "api.pro":
            if base_domain == "openfoodfacts":
                return cls.off_pro
            raise ValueError("pro platform is only available for Open Food Facts")

        for server_type in cls:
            if base_domain == server_type.get_base_domain():
                return server_type

        raise ValueError(f"no Flavor matched for server_domain {server_domain}")

    def is_food(self) -> bool:
        """Return True if the server type is `off` or `off-pro`, False
        otherwise."""
        return self in (self.off, self.off_pro)


class APIVersion(str, enum.Enum):
    v0 = "v0"
    v1 = "v1"
    v2 = "v2"
    v3 = "v3"


class Facet(str, enum.Enum):
    additives = "additives"
    allergens = "allergens"
    brands = "brands"
    categories = "categories"
    countries = "countries"
    contributors = "contributors"
    code = "code"
    entry_dates = "entry_dates"
    ingredients = "ingredients"
    label = "label"
    languages = "languages"
    nutrition_grade = "nutrition_grade"
    packaging = "packaging"
    packaging_codes = "packaging_codes"
    purchase_places = "purchase_places"
    photographer = "photographer"
    informer = "informer"
    states = "states"
    stores = "stores"
    traces = "traces"


class Environment(str, enum.Enum):
    org = "org"
    net = "net"


class APIConfig(BaseModel):
    country: str = "world"
    environment: Environment = Environment.org
    flavor: Flavor = Flavor.off
    version: APIVersion = APIVersion.v2
    username: Optional[str] = None
    password: Optional[str] = None
    timeout: float = 10.0


class DatasetType(str, enum.Enum):
    csv = "csv"
    jsonl = "jsonl"
