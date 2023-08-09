import enum
from typing import Any, Dict, Optional

from pydantic import BaseModel

#: A precise expectation of what mappings looks like in json.
#: (dict where keys are always of type `str`).
JSONType = Dict[str, Any]


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
    """Environment is used to specify Open Food Facts environment:

    - org: production (openfoodfacts.org)
    - net: staging (openfoodfacts.net)
    """

    org = "org"
    net = "net"


Country = enum.Enum(
    "Country",
    [
        ("af", "af"),
        ("ax", "ax"),
        ("al", "al"),
        ("dz", "dz"),
        ("as", "as"),
        ("ad", "ad"),
        ("ao", "ao"),
        ("ai", "ai"),
        ("aq", "aq"),
        ("ag", "ag"),
        ("ar", "ar"),
        ("am", "am"),
        ("aw", "aw"),
        ("au", "au"),
        ("at", "at"),
        ("az", "az"),
        ("bh", "bh"),
        ("bd", "bd"),
        ("bb", "bb"),
        ("by", "by"),
        ("be", "be"),
        ("bz", "bz"),
        ("bj", "bj"),
        ("bm", "bm"),
        ("bt", "bt"),
        ("bo", "bo"),
        ("ba", "ba"),
        ("bw", "bw"),
        ("bv", "bv"),
        ("br", "br"),
        ("io", "io"),
        ("vg", "vg"),
        ("bn", "bn"),
        ("bg", "bg"),
        ("bf", "bf"),
        ("bi", "bi"),
        ("kh", "kh"),
        ("cm", "cm"),
        ("ca", "ca"),
        ("cv", "cv"),
        ("bq", "bq"),
        ("ky", "ky"),
        ("cf", "cf"),
        ("td", "td"),
        ("cl", "cl"),
        ("cn", "cn"),
        ("cx", "cx"),
        ("cc", "cc"),
        ("co", "co"),
        ("km", "km"),
        ("ck", "ck"),
        ("cr", "cr"),
        ("ci", "ci"),
        ("hr", "hr"),
        ("cu", "cu"),
        ("cw", "cw"),
        ("cy", "cy"),
        ("cz", "cz"),
        ("cd", "cd"),
        ("dk", "dk"),
        ("dj", "dj"),
        ("dm", "dm"),
        ("do", "do"),
        ("ec", "ec"),
        ("eg", "eg"),
        ("sv", "sv"),
        ("gq", "gq"),
        ("er", "er"),
        ("ee", "ee"),
        ("et", "et"),
        ("fk", "fk"),
        ("fo", "fo"),
        ("fm", "fm"),
        ("fj", "fj"),
        ("fi", "fi"),
        ("fr", "fr"),
        ("gf", "gf"),
        ("pf", "pf"),
        ("tf", "tf"),
        ("ga", "ga"),
        ("gm", "gm"),
        ("ge", "ge"),
        ("de", "de"),
        ("gh", "gh"),
        ("gi", "gi"),
        ("gr", "gr"),
        ("gl", "gl"),
        ("gd", "gd"),
        ("gp", "gp"),
        ("gu", "gu"),
        ("gt", "gt"),
        ("gg", "gg"),
        ("gn", "gn"),
        ("gw", "gw"),
        ("gy", "gy"),
        ("ht", "ht"),
        ("hm", "hm"),
        ("hn", "hn"),
        ("hk", "hk"),
        ("hu", "hu"),
        ("is", "is"),
        ("in", "in"),
        ("id", "id"),
        ("ir", "ir"),
        ("iq", "iq"),
        ("ie", "ie"),
        ("im", "im"),
        ("il", "il"),
        ("it", "it"),
        ("jm", "jm"),
        ("jp", "jp"),
        ("je", "je"),
        ("jo", "jo"),
        ("kz", "kz"),
        ("ke", "ke"),
        ("ki", "ki"),
        ("xk", "xk"),
        ("kw", "kw"),
        ("kg", "kg"),
        ("la", "la"),
        ("lv", "lv"),
        ("lb", "lb"),
        ("ls", "ls"),
        ("lr", "lr"),
        ("ly", "ly"),
        ("li", "li"),
        ("lt", "lt"),
        ("lu", "lu"),
        ("mo", "mo"),
        ("mg", "mg"),
        ("mw", "mw"),
        ("my", "my"),
        ("mv", "mv"),
        ("ml", "ml"),
        ("mt", "mt"),
        ("mh", "mh"),
        ("mq", "mq"),
        ("mr", "mr"),
        ("mu", "mu"),
        ("yt", "yt"),
        ("mx", "mx"),
        ("md", "md"),
        ("mc", "mc"),
        ("mn", "mn"),
        ("me", "me"),
        ("ms", "ms"),
        ("ma", "ma"),
        ("mz", "mz"),
        ("mm", "mm"),
        ("na", "na"),
        ("nr", "nr"),
        ("np", "np"),
        ("nl", "nl"),
        ("nc", "nc"),
        ("nz", "nz"),
        ("ni", "ni"),
        ("ne", "ne"),
        ("ng", "ng"),
        ("nu", "nu"),
        ("nf", "nf"),
        ("kp", "kp"),
        ("mk", "mk"),
        ("mp", "mp"),
        ("no", "no"),
        ("om", "om"),
        ("pk", "pk"),
        ("pw", "pw"),
        ("pa", "pa"),
        ("pg", "pg"),
        ("py", "py"),
        ("pe", "pe"),
        ("ph", "ph"),
        ("pn", "pn"),
        ("pl", "pl"),
        ("pt", "pt"),
        ("pr", "pr"),
        ("qa", "qa"),
        ("cg", "cg"),
        ("re", "re"),
        ("ro", "ro"),
        ("ru", "ru"),
        ("rw", "rw"),
        ("bl", "bl"),
        ("sh", "sh"),
        ("kn", "kn"),
        ("lc", "lc"),
        ("mf", "mf"),
        ("pm", "pm"),
        ("vc", "vc"),
        ("ws", "ws"),
        ("sm", "sm"),
        ("st", "st"),
        ("sa", "sa"),
        ("sn", "sn"),
        ("rs", "rs"),
        ("sc", "sc"),
        ("sl", "sl"),
        ("sg", "sg"),
        ("sx", "sx"),
        ("sk", "sk"),
        ("si", "si"),
        ("sb", "sb"),
        ("so", "so"),
        ("za", "za"),
        ("gs", "gs"),
        ("kr", "kr"),
        ("ss", "ss"),
        ("es", "es"),
        ("lk", "lk"),
        ("ps", "ps"),
        ("sd", "sd"),
        ("sr", "sr"),
        ("sj", "sj"),
        ("sz", "sz"),
        ("se", "se"),
        ("ch", "ch"),
        ("sy", "sy"),
        ("tw", "tw"),
        ("tj", "tj"),
        ("tz", "tz"),
        ("th", "th"),
        ("bs", "bs"),
        ("tl", "tl"),
        ("tg", "tg"),
        ("tk", "tk"),
        ("to", "to"),
        ("tt", "tt"),
        ("tn", "tn"),
        ("tr", "tr"),
        ("tm", "tm"),
        ("tc", "tc"),
        ("tv", "tv"),
        ("ug", "ug"),
        ("ua", "ua"),
        ("ae", "ae"),
        ("uk", "uk"),
        ("us", "us"),
        ("um", "um"),
        ("uy", "uy"),
        ("uz", "uz"),
        ("vu", "vu"),
        ("va", "va"),
        ("ve", "ve"),
        ("vn", "vn"),
        ("vi", "vi"),
        ("wf", "wf"),
        ("eh", "eh"),
        ("ye", "ye"),
        ("yu", "yu"),
        ("zm", "zm"),
        ("zw", "zw"),
        ("world", "world"),
    ],
)


class APIConfig(BaseModel):
    country: Country = Country.world
    environment: Environment = Environment.org
    flavor: Flavor = Flavor.off
    version: APIVersion = APIVersion.v2
    username: Optional[str] = None
    password: Optional[str] = None
    timeout: float = 10.0


class DatasetType(str, enum.Enum):
    csv = "csv"
    jsonl = "jsonl"


class TaxonomyType(str, enum.Enum):
    category = "category"
    ingredient = "ingredient"
    label = "label"
    brand = "brand"
    packaging_shape = "packaging_shape"
    packaging_material = "packaging_material"
    packaging_recycling = "packaging_recycling"
    country = "country"
    nova_group = "nova_group"
    packaging = "packaging"
    additive = "additive"
    vitamin = "vitamin"
    mineral = "mineral"
    amino_acid = "amino_acid"
    nucleotide = "nucleotide"
    allergen = "allergen"
    state = "state"
    origin = "origin"
    language = "language"
    other_nutritional_substance = "other_nutritional_substance"
