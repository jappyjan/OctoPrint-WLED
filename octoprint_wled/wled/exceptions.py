# -*- coding: utf-8 -*-
"""Exceptions for WLED."""


class WLEDError(Exception):
    """Generic WLED exception."""


class WLEDEmptyResponseError(Exception):
    """WLED empty API response exception."""


class WLEDConnectionError(WLEDError):
    """WLED connection exception."""


class WLEDConnectionTimeoutError(WLEDConnectionError):
    """WLED connection Timeout exception."""
