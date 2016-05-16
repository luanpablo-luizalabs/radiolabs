import os

YT_KEY = 'your-youtube-key'

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '111.111.111.11',
        'NAME': 'radiolabs',
        'USER': 'root',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

if os.environ.get('SETTINGS_MODE') == 'prod':
    # check your instance connection name in your cloud SQL instance properties
    DATABASES['default']['HOST'] = '/cloudsql/<instance-connection-name>'
    DATABASES['default']['PORT'] = ''
