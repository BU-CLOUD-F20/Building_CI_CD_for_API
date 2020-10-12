from .link import LinkAPI, BaseAPI


def initialize_routes(api):
    api.add_resource(BaseAPI, '/')
    api.add_resource(LinkAPI, '/', '/<string:link_id>')
