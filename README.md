RadioLabs
=========

A Django version of https://github.com/alexayub-luizalabs/labsRadio

Usage
-----

* Download and install the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
* Copy the `radiolabs/example_local_settings.py` to `radiolabs/local_settings.py`
* Set the `YT_KEY`, and the DATABASES settings `HOST`, `NAME`, `USER`, `PASSWORD` to match your configurations in GAE (Google App Engine)

**NOTE:** Don't forget to update the unix socket connection in the `prod` condition. (You can find this setting in your Google Cloud Platform > Storage (SQL) > Instances > (your instance) > Properties. Use the Instance connection name.

In order to serve locally:

    ./manage.py runserver

In order to serve locally but using the configurations in `app.yaml`:

    dev_appserver.py ./ --admin_port=9000 --port=8000

In order to Deploy the app:

    appcfg.py update ./
