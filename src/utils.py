import json
import logging
import os
from pathlib import Path
import requests


def setup_logger(name="api_test", level=logging.DEBUG):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger



def load_json(file_path):
    """Load test data from JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)



def pretty_print_response(response: requests.Response):
    """Print status code + response body in a nice format (for debugging)."""
    print(f"\nSTATUS: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print(response.text)



def assert_status_code(response, expected_code=200):
    """Check if response status matches expected."""
    assert response.status_code == expected_code, (
        f"Expected {expected_code}, got {response.status_code}, "
        f"Response: {response.text}"
    )