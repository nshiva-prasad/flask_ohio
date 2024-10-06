# Ohio Well Data API

## Overview

This project is a Flask application that loads the excel data to SqliteDB and provides an API for accessing annual oil, gas, and brine production data for wells in Ohio.

## Python packages used:

1. Flask
2. Flask-SQLAlchemy
3. Pandas
4. SqLite

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using - pip install -r requirements.txt

Example Curl request:
curl --location 'http://localhost:8080/data?well=34059242540000'

Response:
{
"brine": 939,
"gas": 108074,
"oil": 381
}
