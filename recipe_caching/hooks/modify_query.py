from recipe import SETTINGS
from recipe.dynamic_extensions import DynamicExtensionBase
from recipe_caching.mappers import FromCache


class CachingQuery(DynamicExtensionBase):
    def __init__(self, recipe_parts):
        super(CachingQuery, self).__init__(recipe_parts)

    def execute(self):
        cache_target = getattr(SETTINGS, 'CACHE_REGION', 'default')
        cache_prefix = getattr(SETTINGS, 'CACHE_PREFIX', None)
        self.recipe_parts['query'] = self.recipe_parts['query'].options(
            FromCache(cache_target, cache_prefix=cache_prefix))
        return self.recipe_parts
