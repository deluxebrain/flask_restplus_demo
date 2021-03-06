import logging

from flask_restplus_demo.extensions import ma

log = logging.getLogger(__name__)

class UserSchema(ma.Schema):
    class Meta:
        additional = ('id',
            'first_name',
            'last_name'
        )
        ordered = True
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api_v1.UserItem', id='<id>'),
        'collection': ma.URLFor('api_v1.UsersCollection')
    })
