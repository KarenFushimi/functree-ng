#
# This is the FuncTree default configuration file.
# Before start up the application, do not forget to rewrite following variables
# or newly create "instance/config.py" with the same format.
#
DEBUG = False
SECRET_KEY = 'Replace me with long random characters!'
MONGODB_HOST = 'mongodb://127.0.0.1:27017/functree?tz_aware=true'
JSONIFY_PRETTYPRINT_REGULAR = False
FUNCTREE_TIME_ZONE = 'UTC'
FUNCTREE_ADMIN_USERNAME = 'admin'
FUNCTREE_ADMIN_PASSWORD = 'password'
FUNCTREE_PROFILE_TTL_DAYS = 7
