# Repositories

## Style

1. Line max width 120 characters.

## Setup

1. Setup database, e.g. for local instance:
    ```bash
    docker-compose up
    docker-compose exec postgres bash
    psql -h postgres -U postgres
    CREATE DATABASE repositories WITH OWNER postgres ENCODING 'utf-8';
    ```
2. Run tests:
    ```bash
    docker-compose up
    docker-compose exec django bash
    ./repositories/manage.py test
    python ./e2e.py
    ```
3. Deploy to production:
  * create AWS Docker configuration (look into /docker-compose.yml) [#devops]
  * generate envs (look into /envs/) [#devops]
    * generate Github token https://github.com/settings/tokens
    * generate Djago secret with `pwgen -sy 50 1`
