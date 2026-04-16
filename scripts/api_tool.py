#!/usr/bin/env python3

import requests
import json
import logging
import os
import sys
from datetime import datetime

# -----------------------------
# CONFIG LOADER
# -----------------------------
def load_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "config.json")

    if not os.path.exists(config_path):
        print("Config file not found")
        sys.exit(1)

    with open(config_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Invalid JSON in config file")
            sys.exit(1)

# -----------------------------
# LOGGER SETUP
# -----------------------------
def setup_logger(log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# -----------------------------
# API CALL
# -----------------------------
def make_request(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        return response
    except requests.exceptions.Timeout:
        logging.error("Request timed out")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection error occurred")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Unexpected request error: {e}")
        return None

# -----------------------------
# RESPONSE PROCESSING
# -----------------------------
def process_response(response):
    if response is None:
        return None

    if response.status_code != 200:
        logging.error(f"Bad status code: {response.status_code}")
        return None

    try:
        data = response.json()
    except json.JSONDecodeError:
        logging.error("Failed to parse JSON response")
        return None

    # Extract useful fields
    title = data.get("title")
    body = data.get("body")

    if not title or not body:
        logging.error("Missing expected fields in response")
        return None

    return {
        "title": title,
        "body": body
    }

# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    config = load_config()

    api_url = config.get("api_url")
    timeout = config.get("timeout", 5)
    log_file = config.get("log_file")

    if not api_url or not log_file:
        print("Missing required config values")
        sys.exit(1)

    # Resolve absolute log path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(base_dir, log_file)

    setup_logger(log_path)

    logging.info("Starting API automation tool")

    response = make_request(api_url, timeout)
    result = process_response(response)

    if result:
        logging.info(f"Title: {result['title']}")
        logging.info(f"Body: {result['body']}")
        print("✅ API call successful. Check logs for details.")
    else:
        logging.error("Processing failed")
        print("❌ API call failed. Check logs.")

    logging.info("Execution finished")

# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
