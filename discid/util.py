# Copyright (C) 2013  Johannes Dewender
# Copyright (C) 2026  Philipp Wolfer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Please submit bug reports to GitHub:
# https://github.com/metabrainz/python-discid/issues
"""utility functions"""

import math

SECTORS_PER_SECOND = 75


def _encode(string: str | bytes) -> bytes:
    """Encode (unicode) string to byte string"""
    if isinstance(string, str):
        return string.encode()
    elif isinstance(string, bytes):
        return string
    raise TypeError("Unexpected type, expected string or bytes")


def _decode(byte_string: bytes | str) -> str:
    """Decode byte string to (unicode) string"""
    if isinstance(byte_string, bytes):
        return byte_string.decode()
    elif isinstance(byte_string, str):
        return byte_string
    raise TypeError("Unexpected type, expected string or bytes")


def _sectors_to_seconds(sectors: float) -> int:
    """Round sectors to seconds like done on MusicBrainz Server

    The result is forced to :obj:int to make formatted output easier.
    """
    return math.floor((sectors / float(SECTORS_PER_SECOND)) + 0.5)


# vim:set shiftwidth=4 smarttab expandtab:
