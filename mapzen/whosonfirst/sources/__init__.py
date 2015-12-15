# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

# https://github.com/whosonfirst/whosonfirst-sources/blob/master/data/sources-spec-latest.json
# (20151215)

__SPEC__ = {"404734177": {"name": "geoplanet", "license": "http://developer.yahoo.com/geo/geoplanet/data/", "url": "http://developer.yahoo.com/geo/geoplanet/", "prefix": "gp", "fullname": "Yahoo! GeoPlanet", "id": 404734177}, "404734179": {"name": "naturalearth", "license": "http://www.naturalearthdata.com/about/terms-of-use/", "url": "http://www.naturalearthdata.com/", "prefix": "ne", "fullname": "Natural Earth", "id": 404734179}, "404734187": {"name": "whereonearth", "license": "http://developer.yahoo.com/geo/geoplanet/data/", "url": "http://developer.yahoo.com/geo/geoplanet/", "prefix": "woe", "fullname": "Yahoo! GeoPlanet (formerly Where On Earth)", "id": 404734187}, "404734181": {"name": "ourairports", "license": "http://ourairports.com/", "url": "http://ourairports.com/data/", "prefix": "oa", "fullname": "OurAirports", "id": 404734181}, "404734209": {"name": "minitenders", "license": "", "url": "http://www.thebolditalic.com/articles/1101-mini-tenders", "prefix": "mt", "fullname": "Mini Tenders", "id": 404734209, "description": ""}, "404734183": {"name": "quattroshapes", "license": "https://github.com/foursquare/quattroshapes/blob/master/LICENSE.md", "url": "http://www.quattroshapes.com/", "prefix": "qs", "fullname": "Quattroshapes", "id": 404734183}, "404734189": {"name": "wikipedia", "license": "https://en.wikipedia.org/wiki/Wikipedia:Copyrights", "url": "http://www.wikipedia.org/", "prefix": "wk", "fullname": "Wikipedia", "id": 404734189}, "404734173": {"name": "edtf", "license": "", "url": "http://loc.gov/standards/datetime/", "prefix": "edtf", "fullname": "Extended Date/Time Format", "id": 404734173}, "404734193": {"name": "factual", "license": "", "url": "https://github.com/Factual/places", "prefix": "fct", "fullname": "Factual", "id": 404734193}, "404734195": {"name": "mapshaper", "license": "CC0", "url": "", "prefix": "ms", "fullname": "Mapshaper", "id": 404734195, "description": ""}, "404734197": {"name": "mapzen", "license": "CC0", "url": "", "prefix": "mz", "fullname": "Mapzen", "id": 404734197, "description": ""}, "404734199": {"name": "simplegeo", "license": "https://creativecommons.org/publicdomain/zero/1.0/", "url": "", "prefix": "sg", "fullname": "SimpleGeo", "id": 404734199, "description": "SimpleGeo was a location aware services company that operated between 2009 and 2011. It is no longer an active company."}, "404734201": {"name": "yerbashapes", "license": "CC0", "url": "", "prefix": "ys", "fullname": "Yerbashapes", "id": 404734201, "description": "Weighted means from Quattroshapes"}, "404734207": {"name": "woedb", "license": "CC0", "url": "http://woe.spum.org/", "prefix": "woedb", "fullname": "WOE DB", "id": 404734207, "description": ""}, "404734191": {"name": "zetashapes", "license": "http://www.zetashapes.com/license", "url": "http://www.zetashapes.com", "prefix": "zs", "fullname": "Zetashapes", "id": 404734191}, "404734205": {"name": "burritojustice", "license": "CC0", "url": "http://burritojustice.com/la-lengua/", "prefix": "bj", "fullname": "Burrito Justice", "id": 404734205, "description": ""}, "404734175": {"name": "geonames", "license": "http://www.geonames.org/about.html", "url": "http://www.geonames.org/", "prefix": "gn", "fullname": "GeoNames", "id": 404734175}}

__NAMES__ = {}
__PREFIXES__ = {}

for id, details in __SPEC__.items():
    name = details['name']
    prefix = details['prefix']

    __NAMES__[name] = id
    __PREFIXES__[prefix] = id

def is_valid_source(k):

    if __SPEC__.get(k, False):
        return True

    if __NAMES__.get(k, False):
        return True

    if __PREFIXES__.get(k, False):
        return True

    return False


