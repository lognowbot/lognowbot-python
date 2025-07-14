import os
import requests
from typing import Optional, Dict, Any


class LogNowBotClient:
    """Client for sending notifications via LogNowBot."""
    
    def __init__(self, chat_id: Optional[str] = None):
        """
        Initialize the LogNowBot client.
        
        Args:
            chat_id: The chat ID for LogNowBot. If not provided, will use LOGNOWBOT_CHAT_ID environment variable.
        
        Raises:
            ValueError: If chat_id is not provided and LOGNOWBOT_CHAT_ID environment variable is not set.
        """
        self.chat_id = chat_id or os.getenv('LOGNOWBOT_CHAT_ID')
        
        if not self.chat_id:
            raise ValueError(
                "Chat ID is required. Either pass it as a parameter or set the LOGNOWBOT_CHAT_ID environment variable."
            )
        
        self.base_url = "https://api.lognowbot.com"
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'lognowbot-python/0.1.0'
        })
    
    def send_notification(self, message: str, level: str = "info", **kwargs) -> Dict[str, Any]:
        """
        Send a notification to LogNowBot.
        
        Args:
            message: The notification message to send.
            level: The notification level (info, warning, error, success). Defaults to "info".
            **kwargs: Additional parameters to include in the notification.
        
        Returns:
            dict: Response from the LogNowBot API.
        
        Raises:
            requests.RequestException: If the request fails.
            ValueError: If the response indicates an error.
        """
        if not message:
            raise ValueError("Message cannot be empty")
        
        payload = {
            "chat_id": self.chat_id,
            "message": message,
            "level": level,
            **kwargs
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/v1/notify",
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            result = response.json()
            
            if not result.get('success', False):
                raise ValueError(f"Notification failed: {result.get('error', 'Unknown error')}")
            
            return result
            
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to send notification: {str(e)}")
    
    def send_info(self, message: str, **kwargs) -> Dict[str, Any]:
        """Send an info-level notification."""
        return self.send_notification(message, level="info", **kwargs)
    
    def send_warning(self, message: str, **kwargs) -> Dict[str, Any]:
        """Send a warning-level notification."""
        return self.send_notification(message, level="warning", **kwargs)
    
    def send_error(self, message: str, **kwargs) -> Dict[str, Any]:
        """Send an error-level notification."""
        return self.send_notification(message, level="error", **kwargs)
    
    def send_success(self, message: str, **kwargs) -> Dict[str, Any]:
        """Send a success-level notification."""
        return self.send_notification(message, level="success", **kwargs)
    
    def close(self):
        """Close the HTTP session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Convenience functions for quick usage
def send_notification(message: str, level: str = "info", chat_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Send a notification using a one-time client.
    
    Args:
        message: The notification message to send.
        level: The notification level (info, warning, error, success). Defaults to "info".
        chat_id: The chat ID for LogNowBot. If not provided, will use LOGNOWBOT_CHAT_ID environment variable.
        **kwargs: Additional parameters to include in the notification.
    
    Returns:
        dict: Response from the LogNowBot API.
    """
    with LogNowBotClient(chat_id=chat_id) as client:
        return client.send_notification(message, level=level, **kwargs)


def send_info(message: str, chat_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """Send an info-level notification."""
    return send_notification(message, level="info", chat_id=chat_id, **kwargs)


def send_warning(message: str, chat_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """Send a warning-level notification."""
    return send_notification(message, level="warning", chat_id=chat_id, **kwargs)


def send_error(message: str, chat_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """Send an error-level notification."""
    return send_notification(message, level="error", chat_id=chat_id, **kwargs)


def send_success(message: str, chat_id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """Send a success-level notification."""
    return send_notification(message, level="success", chat_id=chat_id, **kwargs)