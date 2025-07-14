"""
LogNowBot Python Client Library

A Python library for sending notifications via LogNowBot.
"""

from .client import LogNowBotClient, send_text

__version__ = "0.1.0"
__author__ = "LogNowBot"
__email__ = "supprot@lognowbot.com"

__all__ = ["LogNowBotClient", "send_text"]
