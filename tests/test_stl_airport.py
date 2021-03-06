from datetime import datetime
from os.path import dirname, join

from city_scrapers_core.constants import COMMISSION
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.stl_airport import StlAirportSpider

test_response = file_response(
    join(dirname(__file__), "files", "stl_airport.html"),
    url="https://www.stlouis-mo.gov/events/eventdetails.cfm?Event_ID=23421",
)
spider = StlAirportSpider()

freezer = freeze_time("2020-07-26")
freezer.start()

parsed_items = [item for item in spider._parse_event(test_response)]

freezer.stop()


def test_title():
    assert parsed_items[0]["title"] == "Airport Commission"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2020, 6, 3, 2, 0)


def test_end():
    assert parsed_items[0]["end"] == datetime(2020, 6, 3, 3, 30)


def test_id():
    assert parsed_items[0]["id"] == "stl_airport/202006030200/x/airport_commission"


def test_status():
    assert parsed_items[0]["status"] == "passed"


def test_location():
    assert parsed_items[0]["location"] == {"name": "Teleconference", "address": ""}


def test_source():
    assert (
        parsed_items[0]["source"]
        == "https://www.stlouis-mo.gov/events/eventdetails.cfm?Event_ID=23421"
    )


def test_links():
    assert parsed_items[0]["links"] == []


def test_classification():
    assert parsed_items[0]["classification"] == COMMISSION


def test_all_day():
    assert parsed_items[0]["all_day"] is False
