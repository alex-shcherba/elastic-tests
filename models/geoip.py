from typing import Optional

from pydantic import BaseModel

from models.location import Location


class Geoip(BaseModel):
    country_iso_code: str
    location: Location
    region_name: Optional[str]
    continent_name: str
    city_name: Optional[str]
