"""A parser for the opening_hours fields from OpenStreetMap.

Provides an OHParser object with the most useful methods
(`is_open()`, `next_change()`, etc). Allows you to set
public and school holidays. Provides a `description()` method
to get a human-readable describing of the opening hours.

Automatically sanitizes the fields to prevent some common mistakes.

To get started, simply do:
>>> import osm_opening_hours_humanized as hoh
>>> oh = hoh.OHParser("Mo-Sa 10:00-19:00")
"""
# flake8: noqa

import os as _os
import gettext as _gettext
_gettext.install("HOH",
    _os.path.join(
        _os.path.dirname(_os.path.realpath(__file__)), "locales"
    )
)

from osm_opening_hours_humanized.version import __version__, __appname__, __author__, __licence__
from osm_opening_hours_humanized.main import OHParser, sanitize, days_of_week
from osm_opening_hours_humanized.temporal_objects import easter_date
from osm_opening_hours_humanized.rendering import AVAILABLE_LOCALES
from osm_opening_hours_humanized import exceptions
