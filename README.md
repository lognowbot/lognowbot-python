# LogNowBot Python Client

A Python library for sending notifications via LogNowBot. This library provides a simple interface to send notifications with different severity levels to your LogNowBot chat.

## Installation

Install the library using pip:

```bash
pip install lognowbot
```

## Configuration

Before using the library, you need to set up your LogNowBot chat ID as an environment variable:

```bash
export LOGNOWBOT_CHAT_ID="your_chat_id_here"
```

You can obtain your chat ID from the LogNowBot service.

## Usage

### Basic Usage

```python
import lognowbot

# Send a simple notification
lognowbot.send_info("Application started successfully!")

# Send notifications with different levels
lognowbot.send_warning("Database connection is slow")
lognowbot.send_error("Failed to process user request")
lognowbot.send_success("Backup completed successfully")
```

### Using the Client Class

```python
from lognowbot import LogNowBotClient

# Initialize client (uses LOGNOWBOT_CHAT_ID environment variable)
client = LogNowBotClient()

# Send notifications
client.send_info("Application started")
client.send_warning("Memory usage is high")
client.send_error("Database connection failed")
client.send_success("Task completed successfully")

# Close the client when done
client.close()
```

### Context Manager

```python
from lognowbot import LogNowBotClient

# Use as context manager for automatic cleanup
with LogNowBotClient() as client:
    client.send_info("Processing started")
    # ... do some work ...
    client.send_success("Processing completed")
```

### Custom Chat ID

You can specify a chat ID directly instead of using the environment variable:

```python
import lognowbot

# Using convenience functions
lognowbot.send_info("Hello World!", chat_id="your_chat_id")

# Using client class
client = LogNowBotClient(chat_id="your_chat_id")
client.send_info("Hello World!")
```

### Advanced Usage

```python
from lognowbot import LogNowBotClient

with LogNowBotClient() as client:
    # Send notification with additional parameters
    client.send_notification(
        message="Custom notification",
        level="info",
        source="my_app",
        timestamp="2023-01-01T00:00:00Z"
    )
```

## API Reference

### LogNowBotClient

#### Constructor
- `LogNowBotClient(chat_id=None)`: Initialize the client with optional chat ID

#### Methods
- `send_notification(message, level="info", **kwargs)`: Send a notification with custom level
- `send_info(message, **kwargs)`: Send an info-level notification
- `send_warning(message, **kwargs)`: Send a warning-level notification
- `send_error(message, **kwargs)`: Send an error-level notification
- `send_success(message, **kwargs)`: Send a success-level notification
- `close()`: Close the HTTP session

### Convenience Functions

- `send_notification(message, level="info", chat_id=None, **kwargs)`
- `send_info(message, chat_id=None, **kwargs)`
- `send_warning(message, chat_id=None, **kwargs)`
- `send_error(message, chat_id=None, **kwargs)`
- `send_success(message, chat_id=None, **kwargs)`

## Error Handling

The library raises appropriate exceptions for various error conditions:

```python
from lognowbot import LogNowBotClient
import requests

try:
    with LogNowBotClient() as client:
        client.send_info("Test notification")
except ValueError as e:
    print(f"Configuration error: {e}")
except requests.RequestException as e:
    print(f"Network error: {e}")
```

## Requirements

- Python 3.7+
- requests >= 2.25.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.