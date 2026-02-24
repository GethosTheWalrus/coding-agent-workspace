"""SQLAlchemy models for the Todo application.

TODO: Define the Todo model with fields:
- id (Integer, primary key)
- title (String, required)
- description (String, optional)
- completed (Boolean, default False)
"""

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: Define Todo model class here
