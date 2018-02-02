import datetime


class RepositoryFactory:
    __dict__ = {
        'full_name': 'wieczorek1990',
        'description': 'wieczorek1990.github.io',
        'clone_url': 'https://github.com/wieczorek1990/wieczorek1990.github.io.git',
        'stars': 1,
        'created_at': datetime.datetime.utcnow(),
    }

    def __getitem__(self, item):
        return self.__dict__[item]

    def keys(self):
        return self.__dict__.keys()
