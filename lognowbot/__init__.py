"""
LogNowBot Python Client Library

A Python library for sending notifications via LogNowBot.
"""

from .client import (
    LogNowBotClient,
    send_notification,
    send_info,
    send_warning,
    send_error,
    send_success,
)

__version__ = "0.1.0"
__author__ = "LogNowBot"
__email__ = "contact@lognowbot.com"

__all__ = [
    "LogNowBotClient",
    "send_notification",
    "send_info",
    "send_warning",
    "send_error",
    "send_success",
]