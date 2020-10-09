from .link import LinkAPI, BaseAPI


def initialize_routes(api):
    api.add_resource(LinkAPI, "/api/", "/<string:link_id>")
