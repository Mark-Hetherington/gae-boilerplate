from webapp2_extras.routes import RedirectRoute
from webapp2_extras.routes import PathPrefixRoute
import users


_routes = [
    PathPrefixRoute('/admin', [
        RedirectRoute('/logout/', users.AdminLogoutHandler, name='admin-logout', strict_slash=True),
        RedirectRoute('/', users.AdminGeoChartHandler, name='geochart', strict_slash=True),
        RedirectRoute('/users/', users.AdminUserListHandler, name='user-list', strict_slash=True),
        RedirectRoute('/users/<user_id>/', users.AdminUserEditHandler, name='user-edit', strict_slash=True, handler_method='edit')
    ])
]

def get_routes():
    return _routes

def add_routes(app):
    for r in _routes:
        app.router.add(r)
