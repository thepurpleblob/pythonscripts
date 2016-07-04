import pycurl
from urllib.parse import urlencode
from io import BytesIO
import json
import sys

class Mahara:
    "Access mahara web service"

    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.token = token 

    def _ws(self, data):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.endpoint)
        c.setopt(c.WRITEDATA, buffer)
        post_data = {
            'wstoken': self.token,
        }
        post_data.update(data)
        post_fields = json.dumps(post_data)
        #print(post_fields)
        #sys.exit(0)
        c.setopt(c.HTTPHEADER, ['Accept: application/json'])
        c.setopt(c.POST, 1)
        c.setopt(c.POSTFIELDS, post_fields)
        c.perform()
        c.close()
        buffer_str = buffer.getvalue()
        data = json.loads(buffer_str.decode('utf8'))
        return data

    def mahara_institution_get_members(self, institution):
        """
        Read list of users for institution
        institution - 'short name' of institution
        """
        data = {
            'wsfunction': 'mahara_institution_get_members',
            'institution': institution
        }
        return self._ws(data)

    def mahara_institution_add_members(self, institution, users):
        """
        Add list of users to institution
        institution - 'short name' of institution
        users - array of {'id': userid, 'username': username}
        """
        data = {
            'wsfunction': 'mahara_institution_add_members',
            'institution': institution,
            'users': users
        }
        return self._ws(data)

    def mahara_institution_remove_members(self, institution, users):
        """
        Remove list of users from institution
        institution - 'short name' of institution
        users - array of {'id': userid, 'username': username}
        """
        data = {
            'wsfunction': 'mahara_institution_remove_members',
            'institution': institution,
            'users': users
        }
        return self._ws(data)

    def mahara_user_get_users(self):
        """
        Get ALL users
        """
        data = {
            'wsfunction': 'mahara_user_get_users'
        }
        return self._ws(data)
