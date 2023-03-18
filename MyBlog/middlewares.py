import logging

from MyBlog.core.exception_handlers import server_error_view_500, page_not_found_view


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            # logging.error('ERROR - Something wrong')
            # logging.debug('Debug: errors')
            return server_error_view_500(request)

        return response

    return middleware
