from MyWebsite.www.models import User
from MyWebsite.www.coroweb import get


@get('/')
def index(request):
    users=yield from User.findAll()
    return {
        '__template__':'test.html',
        'users':users
    }