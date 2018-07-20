import requests
# Handling Python 2/3 quote_plus import
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

class OpenGraphIO:
    def __init__(self, options={}):
        """
        Initialize OpenGraphIO instance with required app_id.
        """
        # Throw an error if app_id is not present in options dict
        if not 'app_id' in options:
            raise KeyError('app_id must be supplied when making requests to the API. Get a free app_id by signing up here: https://www.opengraph.io/')

        self.app_id = options['app_id']

        # Assign options if present, or defaults if not
        # These can be overridden when making requests through get_site_info
        self.cache_ok = options['cache_ok'] if 'cache_ok' in options else True
        self.full_render = options['full_render'] if 'full_render' in options else False
        self.version = options['version'] if 'version' in options else '1.1'

    def get_site_info_url(self, url, options={}):
        """
        Build the request URL.
        """
        version = options['version'] if 'version' in options else self.version
        return 'https://opengraph.io/api/' + version + '/site/' + quote_plus(url)

    def get_site_info_query_params(self, options={}):
        """
        Set params for a particular request called with get_site_info.
        """
        query_string_values = {}

        query_string_values['app_id'] = options['app_id'] if 'app_id' in options else self.app_id

        query_string_values['cache_ok'] = options['cache_ok'] if 'cache_ok' in options else self.cache_ok

        query_string_values['full_render'] = options['full_render'] if 'full_render' in options else self.full_render

        query_string_values['version'] = options['version'] if 'version' in options else self.version

        return query_string_values
    
    def get_site_info(self, passed_url, options={}):
        """
        Request OpenGraph tags and return JSON.
        """
        uri = self.get_site_info_url(passed_url)
        params = self.get_site_info_query_params(options)
        response = requests.get(uri, params)
        return response.json()
