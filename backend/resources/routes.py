from .link import Link


def initialize_routes(api):
    api.add_resource(Link, '/link/<string:link_id>')
