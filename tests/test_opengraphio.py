import unittest
import os
from urllib.parse import quote_plus
from opengraphio import OpenGraphIO


class TestOpenGraphIO(unittest.TestCase):
    def constants_for_test_cases(self):
        return {
            'test_url': 'https://github.com',
            'test_title': 'Build software better, together',
            'test_description': 'GitHub is where people build software. More than 36 million people use GitHub' +
            ' to discover, fork, and contribute to over 100 million projects.'
        }

    def test_default_initialization(self):
        """
        It should initialize with an app_id and default values
        """
        options = {
            'app_id': os.environ['APP_ID']
        }
        og = OpenGraphIO
        og = OpenGraphIO(options)
        self.assertEqual(og.app_id, os.environ['APP_ID'])
        self.assertEqual(og.cache_ok, True)
        self.assertEqual(og.full_render, False)
        self.assertEqual(og.version, '1.1')

    def test_override_initialization(self):
        """
        It should initialize with overridden default values
        """
        options = {
            'app_id': os.environ['APP_ID'],
            'cache_ok': False,
            'full_render': True,
            'version': '1.0'
        }

        og = OpenGraphIO(options)
        self.assertEqual(og.app_id, os.environ['APP_ID'])
        self.assertEqual(og.cache_ok, False)
        self.assertEqual(og.full_render, True)
        self.assertEqual(og.version, '1.0')

    def test_override_with_defaults(self):
        """
        It should allow overriding of defaults but otherwise use defaults
        """
        options = {
            'app_id': os.environ['APP_ID'],
            'cache_ok': False
        }

        og = OpenGraphIO(options)
        self.assertEqual(og.cache_ok, False)
        self.assertEqual(og.full_render, False)

    def test_no_app_id_error(self):
        """
        It should throw an error if an app_id is not provided
        """
        with self.assertRaises(KeyError):
            og = OpenGraphIO({})

    def test_create_valid_url(self):
        """
        It should create a valid URL with no options except app_id
        """
        target = 'http://cnn.com'
        og = OpenGraphIO({'app_id': os.environ['APP_ID']})
        url = og.get_site_info_url(target)
        self.assertEqual(
            url,
            'https://opengraph.io/api/1.1/site/' + quote_plus(target)
        )

    def test_create_query_params(self):
        """
        It should create proper query parameters
        """
        options = {
            'app_id': os.environ['APP_ID'],
            'cache_ok': False
        }
        params_override_options = {
            'full_render': True
        }
        og = OpenGraphIO(options)
        params = og.get_site_info_query_params(params_override_options)

        self.assertEqual(params['app_id'], os.environ['APP_ID'])
        self.assertEqual(params['cache_ok'], False)
        self.assertEqual(params['full_render'], True)

    def test_get_results_with_app_id(self):
        og = OpenGraphIO({'app_id': os.environ['APP_ID']})
        response = og.get_site_info(self.constants_for_test_cases()['test_url'])
        hybrid_graph = response['hybridGraph']
        self.assertEqual(hybrid_graph['url'], self.constants_for_test_cases()['test_url'])
        self.assertEqual(hybrid_graph['title'], self.constants_for_test_cases()['test_title'])
        self.assertEqual(hybrid_graph['description'], self.constants_for_test_cases()['test_description'])

    def test_get_results_with_options(self):
        og = OpenGraphIO({
            'app_id': os.environ['APP_ID'],
            'cache_ok': False,
            'full_render': True
        })
        response = og.get_site_info(self.constants_for_test_cases()['test_url'])
        hybrid_graph = response['hybridGraph']
        self.assertEqual(hybrid_graph['url'], self.constants_for_test_cases()['test_url'])
        self.assertEqual(hybrid_graph['title'], self.constants_for_test_cases()['test_title'])
        self.assertEqual(hybrid_graph['description'], self.constants_for_test_cases()['test_description'])

