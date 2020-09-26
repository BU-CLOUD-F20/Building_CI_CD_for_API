from .link import LinkAPI


def initialize_routes(api):
    api.add_resource(LinkAPI, '/', '/<string:link_id>')
