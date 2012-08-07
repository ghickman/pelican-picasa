Installation
------------
Using your favourite package manager::

    pip install pelican-picasa

Add the following to your pelican settings::

    PLUGINS = ['picasa']

    PICASA_EMAIL = ''
    PICASA_PASSWORD = ''
    PICASA_USER_ID = ''

Email and Password must be a valid Google Account.

User ID is the Picasa user you want to display.


Usage
-----
Template
~~~~~~~~
Loop photos in a like so::

    {% for photo in picasa %}
        <img src="{{ photo.url }}">
    {% endfor %}

Post
~~~~
Add your picasa album id to a post's metadata::

    Picasa_album: 1234

You can optionally filter this album by tag too::

    Picasa_tag: foo

