# Repositories

1. Generate Github token on https://github.com/settings/tokens
2. Setup local database:
    ```bash
    docker-compose exec postgres bash
    psql -h postgres -U postgres
    CREATE DATABASE repositories WITH OWNER postgres ENCODING 'utf-8';
    ```
3. To deploy to production:
  * create AWS Docker configuration (look into /docker-compose.yml)
  * generate envs (look into /envs/)
