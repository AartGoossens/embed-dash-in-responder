# Source: http://python-responder.org/en/latest/
import responder

import dash_app


api = responder.API()


@api.route('/hello/{world}')
async def hello(_, response, world):
    response.text = f'Hello, {world}!'


api.mount('/dash', dash_app.app.server)


if __name__ == '__main__':
    api.run()
