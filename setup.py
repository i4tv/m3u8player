
from setuptools import setup, find_packages

setup(
    name='M3U8Player',
    version='0.1.0',
    author='Zhang Ping',
    author_email='dqzhangp@163.com',
    description='A MediaCore plugin m3u8 player.',

    packages=find_packages(),
    namespace_packages = ['m3u8player'],
    include_package_data=True,
    zip_safe = False,

    entry_points = {
        'mediacore.plugin': [
            'm3u8player = m3u8player.mediacore_plugin',
        ],
    },

    message_extractors = {'m3u8player/': [
        ('**.py', 'python', None),
        ('templates/**.html', 'genshi', {'template_class': 'genshi.template.markup:MarkupTemplate'}),
        ('public/**', 'ignore', None),
    ]},
)

