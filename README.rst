Installation
------------
Using your favourite package manager::

    pip install pelican-picasa

Add the following to your pelican settings::

    PLUGINS = ['picasa']

    PICASA_EMAIL = ''
    PICASA_PASSWORD = ''
    PICASA_TAG = ''
    PICASA_USER_ID = ''

Email and Password must be a valid Google Account.

User ID is the Picasa user you want to display.


Usage
-----
Loop photos in a given tag like so::

    {% for photo in picasa %}
        <img src="{{ photo.url }}">
    {% endfor %}

