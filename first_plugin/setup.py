from setuptools import setup, find_packages

setup(
    name="me-example",
    version='1.0',
    description='Demo',
    author='Me',
    author_email='me@me.com',
    platforms=['Any'],
    scripts=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'me.example.formatter': [
            'simple = me.example.simple.Simple',
            'plain = me.example.simple:Simple'
        ]
    },
    zip_safe=False
)
