from urllib3.parse import urlencode

class OpenGraphIO:
    def __init__(self, app_id, cache_ok=True, full_render=False, version='1.1'):
        self.app_id = app_id
        self.cache_ok = cache_ok
        self.full_render = full_render
        self.version = version

    def get_site_info_url(self, url):
        return 'https://opengraph.io/api' + self.version + '/site/' + urllib3.urlencode(url)

    def get_site_info_query_params(self, options):
        query_string_values = {}

        query_string_values['app_id'] = options['app_id'] if 'app_id' in options else self.app_id

        query_string_values['cache_ok'] = options['cache_ok'] if 'cache_ok' in options else self.cache_ok

        query_string_values['full_render'] = options['full_render'] if 'full_render' in options else self.full_render

        query_string_values['version'] = options['version'] if 'version' in options else self.version

        return query_string_values
    