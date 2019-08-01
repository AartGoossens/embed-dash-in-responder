# Source: http://python-responder.org/en/latest/
import responder

import dash_app


api = responder.API()


api.mount('/dash', dash_app.app.server)


if __name__ == '__main__':
    api.run()
