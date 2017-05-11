"""
utils/

Utility methods for VulnBid backend.

:author: Sean Pianka
:e-mail: pianka@eml.cc

"""
import hashlib
from datetime import date

from vulnbid import app
from config import PASSWORD_SALT


@app.context_processor
def inject_fake_user():
    return {
        'user': {'nickname': 'Me'},
        'current_year': date.today().year
    }


def hash_password(plaintext_password, salt=PASSWORD_SALT):
    return str(hashlib.sha512(''.join([plaintext_password, salt]).encode('utf-8')).hexdigest())