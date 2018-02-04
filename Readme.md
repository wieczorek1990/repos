# Repositories

## Envs

Create `/envs/` directory using `/envs.example/` as template.

```bash
# django
DJANGO_DEBUG # 0 or 1 for disabled/enabled
DJANGO_SECRET_KEY # 50 characters
GITHUB_ACCESS_TOKEN # 40 characters

# postgres
POSTGRES_USERNAME # username
POSTGRES_PASSWORD # password
```

## Running

After creating envs run:

```bash
docker-compose up
```

This starts with failure when database is yet not created.

## Database

Setting up database, e.g. for local instance:

```bash
docker-compose up
docker-compose exec postgres bash
psql -h postgres -U postgres
CREATE DATABASE repositories WITH OWNER postgres ENCODING 'utf-8';
```

Now run `docker-compose up` again for backend to start without failure.

## Tests

Running tests:

```bash
docker-compose up
docker-compose exec django bash
./manage.py test
python ../e2e.py
```

I ran performance test with [wrk](https://github.com/wg/wrk). Tweaking server options and wrk arguments allowed me
to accomplish more that 20 requests per second.

```bash
$ wrk -t8 -c40 -d1s http://localhost:8000/repositories/wieczorek1990/wieczorek1990.github.io/
Running 1s test @ http://localhost:8000/repositories/wieczorek1990/wieczorek1990.github.io/
  8 threads and 40 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   691.04ms  102.14ms   1.09s    89.66%
    Req/Sec     7.00      5.99    20.00     76.47%
  29 requests in 1.10s, 9.40KB read
  Socket errors: connect 0, read 29, write 0, timeout 0
Requests/sec:     26.39
Transfer/sec:      8.56KB
```

## Deployment

Deploy to production:

* create AWS Docker configuration (look into /docker-compose.yml and /Dockerfile) [#devops]
    * generate envs (look into /envs/)
    * generate Github token https://github.com/settings/tokens
    * generate Djago secret with `pwgen -sy 50 1`

## Notes

* Time spent: around 6h
* I had used my own Django boilerplate
* Line max width 120 characters
