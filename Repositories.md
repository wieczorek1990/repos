# Repositories

## Style

1. Line max width 120 characters.

## Setup

1. Generate Github token on https://github.com/settings/tokens
2. Setup local database:
    ```bash
    docker-compose up
    docker-compose exec postgres bash
    psql -h postgres -U postgres
    CREATE DATABASE repositories WITH OWNER postgres ENCODING 'utf-8';
    ```
3. Tests:
    ```bash
    docker-compose up
    docker-compose exec django bash
    ./repositories/manage.py test
    python ./e2e.py
    ```
4. To deploy to production:
  * create AWS Docker configuration (look into /docker-compose.yml)
  * generate and load envs (look into /envs/)
