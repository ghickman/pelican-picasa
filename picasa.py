from gdata.photos import service

from pelican import signals


__version__ = '0.1'


class Photo(object):
    def __init__(self, data):
        self.url = data.GetHtmlLink().href
        self.caption = data.summary.text
        self.thumbs = [thumb.url for thumb in data.media.thumbnail]
        try:
            self.latitude = data.geo.latitude()
            self.longitude = data.geo.longitude()
        except ValueError:
            pass  # stupid gdata


class Picasa(object):
    def __init__(self, generator):
        self.client = service.PhotosService()
        self.client.email = generator.settings['PICASA_EMAIL']
        self.client.password = generator.settings['PICASA_PASSWORD']
        self.client.source = 'Super Awesome Pelican Plugin'
        self.client.ProgrammaticLogin()

    def fetch(self, gen, album_id, tag=None):
        user = gen.settings['PICASA_USER_ID']
        feed = '/data/feed/api/user/{0}/albumid/{1}?kind=photo'.format(user, album_id)
        if tag is not None:
            feed = '{0}&tag={1}'.format(feed, tag)
        photos = self.client.GetFeed(feed)
        return [Photo(item) for item in photos.entry]


def init_picasa(generator):
    generator.plugin_instance = Picasa(generator)


def fetch_photos(gen, metadata):
    settings = (
        'PICASA_EMAIL' in gen.settings.keys(),
        'PICASA_PASSWORD' in gen.settings.keys(),
        'PICASA_USER_ID' in gen.settings.keys()
    )
    if all(settings) and 'picasa_album' in metadata.keys():
        args = [gen, metadata['picasa_album']]
        if 'picasa_tag' in metadata.keys():
            args.append(metadata['picasa_tag'])
        gen.context['picasa'] = gen.plugin_instance.fetch(*args)


def register():
    signals.article_generator_init.connect(init_picasa)
    signals.article_generate_context.connect(fetch_photos)

