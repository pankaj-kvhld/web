"""Holds the configurations for this project."""

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "DC_STUDD"
