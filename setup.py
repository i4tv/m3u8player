
from setuptools import setup, find_packages

setup(
    name='M3U8Player',
    version='1.0',

    author='Zhang Ping',
    author_email='dqzhangp@163.com',
    license='GPL v3 or later',

    packages=find_packages(),

    package_data = {
        'm3u8player': ['public/scripts/third-party/*', 'templates/*'],
    },

    entry_points = {
        'mediacore.plugin': [
            'm3u8player = m3u8player.mediacore_plugin',
        ],
    }
)

