from sqlalchemy.orm import sessionmaker

from recipe import SETTINGS
from recipe.oven.base import OvenBase
from recipe_caching import query_callable


class CachingOven(OvenBase):
    """Concrete Implementation of OvenBase
    """
    def init_engine(self, connection_string=None, **kwargs):
        return super(CachingOven, self).init_engine(connection_string,
                                                    **kwargs)

    def init_session(self):
        """Establishes a Session constructor for async database communications
        with caching queries.
        """
        if not self.engine:
            return

        SETTINGS.REGIONS = {}

        return sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False,
            query_cls=query_callable(SETTINGS.CACHE_REGIONS)
        )
