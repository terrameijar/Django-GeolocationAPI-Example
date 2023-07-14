## Geolocation API Example

This project demonstrates how to build a Geolocation Site using Django.

## Setup

To run this project, do the following:

1. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

1. Generate Secret Key and save it to a `SECRET_KEY` environment variable:
    ```bash
    # Start the Django Shell
    python manage.py shell

    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()

    ```

1. Create an API key on tomtom.com to generate maps. Copy and save it to a `TOMTOM_API_KEY` environment variable.
1. Run migrations:
    ```python
    python manage.py migrate
    ```
1. Collect static files:
    ```shell
    python manage.py collectstatic
    ```