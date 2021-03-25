import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SearchPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'search')

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')
        is_positive_integer = toolkit.get_validator('is_positive_integer')

        schema.update({
            'ckan.datasets_per_page': [ignore_missing, is_positive_integer],
            'ckanext.search.test_config': [ignore_missing, is_positive_integer]
        })
        return schema
