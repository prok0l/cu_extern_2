from dataclasses import dataclass

from entities.coords import Coords, LocationName, Points


@dataclass
class LocationForm:
    start_city: str
    latitude_start: str
    longitude_start: str
    finish_city: str
    latitude_finish: str
    longitude_finish: str
    location_type: str = 'off'

    @property
    def type(self) -> bool:
        return self.location_type == 'on'

    @property
    def start(self) -> LocationName | Coords:
        if not self.type:
            return LocationName(name=self.start_city)
        else:
            return Coords(latitude=float(self.latitude_start),
                          longitude=float(self.longitude_start))

    @property
    def finish(self) -> LocationName | Coords:
        if not self.type:
            return LocationName(name=self.finish_city)
        else:
            return Coords(latitude=float(self.latitude_finish),
                          longitude=float(self.longitude_finish))

    @property
    def points(self) -> Points:
        return Points(start=self.start,
                      end=self.finish)
