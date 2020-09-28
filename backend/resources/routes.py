from .link import LinkApi


def initialize_routes(api):
    api.add_resource(LinkApi, '/', '/<string:link_id>')
