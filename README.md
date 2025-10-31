# DRF Timezone Test

A simple project to test and demonstrate timezone handling with Postgres, JavaScript, Python, Django and django-rest-framework.

## Features

- Demonstrates timezone-aware datetime handling in DRF
- Example API endpoints for testing datetime serialization and parsing
- Configurable timezone settings

## Requirements

- PostgreSQL database (check connection settings in [`settings.py`](./drf_timezone_test/settings.py))
- uv to install Python (3.13+) (https://docs.astral.sh/uv/)
- Node (24+) and npm (to play with the frontend part if needed)

## Setup

```bash
make requirements   # install python with uv and synchronize dependencies
npm install         # install node dependencies
```

## Usage

1. Run migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Access the API endpoints at `http://localhost:8000/`

## Configuration

Timezone settings can be adjusted in [`settings.py`](./drf_timezone_test/settings.py):

```python
TIME_ZONE = 'UTC'
USE_TZ = True
```

## License

MIT License

## Author

Denny Biasiolli
