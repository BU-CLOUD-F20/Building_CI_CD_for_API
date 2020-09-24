from .link import ShortLink, LongLink


def initialize_routes(api):
    api.add_resource(ShortLink, '/link/short/<string:link>')
    api.add_resource(LongLink, '/link/long')
