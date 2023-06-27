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


class Country(str, enum.Enum):
    af = "en:afghanistan"
    ax = "en:aland-islands"
    al = "en:albania"
    dz = "en:algeria"
    as_ = "en:american-samoa"
    ad = "en:andorra"
    ao = "en:angola"
    ai = "en:anguilla"
    aq = "en:antarctic"
    ag = "en:antigua-and-barbuda"
    ar = "en:argentina"
    am = "en:armenia"
    aw = "en:aruba"
    au = "en:australia"
    at = "en:austria"
    az = "en:azerbaijan"
    bh = "en:bahrain"
    bd = "en:bangladesh"
    bb = "en:barbados"
    by = "en:belarus"
    be = "en:belgium"
    bz = "en:belize"
    bj = "en:benin"
    bm = "en:bermuda"
    bt = "en:bhutan"
    bo = "en:bolivia"
    ba = "en:bosnia-and-herzegovina"
    bw = "en:botswana"
    bv = "en:bouvet-island"
    br = "en:brazil"
    io = "en:british-indian-ocean-territory"
    vg = "en:british-virgin-islands"
    bn = "en:brunei"
    bg = "en:bulgaria"
    bf = "en:burkina-faso"
    bi = "en:burundi"
    kh = "en:cambodia"
    cm = "en:cameroon"
    ca = "en:canada"
    cv = "en:cape-verde"
    bq = "en:caribbean-netherlands"
    ky = "en:cayman-islands"
    cf = "en:central-african-republic"
    td = "en:chad"
    cl = "en:chile"
    cn = "en:china"
    cx = "en:christmas-island"
    cc = "en:cocos-keeling-islands"
    co = "en:colombia"
    km = "en:comoros"
    ck = "en:cook-islands"
    cr = "en:costa-rica"
    ci = "en:cote-d-ivoire"
    hr = "en:croatia"
    cu = "en:cuba"
    cw = "en:curacao"
    cy = "en:cyprus"
    cz = "en:czech-republic"
    cd = "en:democratic-republic-of-the-congo"
    dk = "en:denmark"
    dj = "en:djibouti"
    dm = "en:dominica"
    do = "en:dominican-republic"
    ec = "en:ecuador"
    eg = "en:egypt"
    sv = "en:el-salvador"
    gq = "en:equatorial-guinea"
    er = "en:eritrea"
    ee = "en:estonia"
    et = "en:ethiopia"
    fk = "en:falkland-islands"
    fo = "en:faroe-islands"
    fm = "en:federated-states-of-micronesia"
    fj = "en:fiji"
    fi = "en:finland"
    fr = "en:france"
    gf = "en:french-guiana"
    pf = "en:french-polynesia"
    tf = "en:french-southern-and-antarctic-lands"
    ga = "en:gabon"
    gm = "en:gambia"
    ge = "en:georgia"
    de = "en:germany"
    gh = "en:ghana"
    gi = "en:gibraltar"
    gr = "en:greece"
    gl = "en:greenland"
    gd = "en:grenada"
    gp = "en:guadeloupe"
    gu = "en:guam"
    gt = "en:guatemala"
    gg = "en:guernsey"
    gn = "en:guinea"
    gw = "en:guinea-bissau"
    gy = "en:guyana"
    ht = "en:haiti"
    hm = "en:heard-island-and-mcdonald-islands"
    hn = "en:honduras"
    hk = "en:hong-kong"
    hu = "en:hungary"
    is_ = "en:iceland"
    in_ = "en:india"
    id = "en:indonesia"
    ir = "en:iran"
    iq = "en:iraq"
    ie = "en:ireland"
    im = "en:isle-of-man"
    il = "en:israel"
    it = "en:italy"
    jm = "en:jamaica"
    jp = "en:japan"
    je = "en:jersey"
    jo = "en:jordan"
    kz = "en:kazakhstan"
    ke = "en:kenya"
    ki = "en:kiribati"
    xk = "en:kosovo"
    kw = "en:kuwait"
    kg = "en:kyrgyzstan"
    la = "en:laos"
    lv = "en:latvia"
    lb = "en:lebanon"
    ls = "en:lesotho"
    lr = "en:liberia"
    ly = "en:libya"
    li = "en:liechtenstein"
    lt = "en:lithuania"
    lu = "en:luxembourg"
    mo = "en:macau"
    mg = "en:madagascar"
    mw = "en:malawi"
    my = "en:malaysia"
    mv = "en:maldives"
    ml = "en:mali"
    mt = "en:malta"
    mh = "en:marshall-islands"
    mq = "en:martinique"
    mr = "en:mauritania"
    mu = "en:mauritius"
    yt = "en:mayotte"
    mx = "en:mexico"
    md = "en:moldova"
    mc = "en:monaco"
    mn = "en:mongolia"
    me = "en:montenegro"
    ms = "en:montserrat"
    ma = "en:morocco"
    mz = "en:mozambique"
    mm = "en:myanmar"
    na = "en:namibia"
    nr = "en:nauru"
    np = "en:nepal"
    nl = "en:netherlands"
    nc = "en:new-caledonia"
    nz = "en:new-zealand"
    ni = "en:nicaragua"
    ne = "en:niger"
    ng = "en:nigeria"
    nu = "en:niue"
    nf = "en:norfolk-island"
    kp = "en:north-korea"
    mk = "en:north-macedonia"
    mp = "en:northern-mariana-islands"
    no = "en:norway"
    om = "en:oman"
    pk = "en:pakistan"
    pw = "en:palau"
    pa = "en:panama"
    pg = "en:papua-new-guinea"
    py = "en:paraguay"
    pe = "en:peru"
    ph = "en:philippines"
    pn = "en:pitcairn"
    pl = "en:poland"
    pt = "en:portugal"
    pr = "en:puerto-rico"
    qa = "en:qatar"
    cg = "en:republic-of-the-congo"
    re = "en:reunion"
    ro = "en:romania"
    ru = "en:russia"
    rw = "en:rwanda"
    bl = "en:saint-barthelemy"
    sh = "en:saint-helena"
    kn = "en:saint-kitts-and-nevis"
    lc = "en:saint-lucia"
    mf = "en:saint-martin"
    pm = "en:saint-pierre-and-miquelon"
    vc = "en:saint-vincent-and-the-grenadines"
    ws = "en:samoa"
    sm = "en:san-marino"
    st = "en:sao-tome-and-principe"
    sa = "en:saudi-arabia"
    sn = "en:senegal"
    rs = "en:serbia"
    sc = "en:seychelles"
    sl = "en:sierra-leone"
    sg = "en:singapore"
    sx = "en:sint-maarten"
    sk = "en:slovakia"
    si = "en:slovenia"
    sb = "en:solomon-islands"
    so = "en:somalia"
    za = "en:south-africa"
    gs = "en:south-georgia-and-the-south-sandwich-islands"
    kr = "en:south-korea"
    ss = "en:south-sudan"
    es = "en:spain"
    lk = "en:sri-lanka"
    ps = "en:state-of-palestine"
    sd = "en:sudan"
    sr = "en:suriname"
    sj = "en:svalbard-and-jan-mayen"
    sz = "en:swaziland"
    se = "en:sweden"
    ch = "en:switzerland"
    sy = "en:syria"
    tw = "en:taiwan"
    tj = "en:tajikistan"
    tz = "en:tanzania"
    th = "en:thailand"
    bs = "en:the-bahamas"
    tl = "en:timor-leste"
    tg = "en:togo"
    tk = "en:tokelau"
    to = "en:tonga"
    tt = "en:trinidad-and-tobago"
    tn = "en:tunisia"
    tr = "en:turkey"
    tm = "en:turkmenistan"
    tc = "en:turks-and-caicos-islands"
    tv = "en:tuvalu"
    ug = "en:uganda"
    ua = "en:ukraine"
    ae = "en:united-arab-emirates"
    uk = "en:united-kingdom"
    us = "en:united-states"
    um = "en:united-states-minor-outlying-islands"
    uy = "en:uruguay"
    uz = "en:uzbekistan"
    vu = "en:vanuatu"
    va = "en:vatican-city"
    ve = "en:venezuela"
    vn = "en:vietnam"
    vi = "en:virgin-islands-of-the-united-states"
    wf = "en:wallis-and-futuna"
    eh = "en:western-sahara"
    ye = "en:yemen"
    yu = "en:yugoslavia"
    zm = "en:zambia"
    zw = "en:zimbabwe"
    world = "en:world"

    @classmethod
    def get_from_2_letter_code(cls, value: str):
        """This function is used to support conversion from string:
        'as', 'in', and 'is' are encoded with a '_' suffix, as these are
        Python reserved words.

        :param value: the input string
        :return: the associated Country
        """
        if value in ("as", "in", "is"):
            value = f"{value}_"
        return cls[value]


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
