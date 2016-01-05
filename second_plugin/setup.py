from setuptools import setup, find_packages

setup(
    name="me-example-plugin2",
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
            'field = me.example2.fields.FieldList',
        ]
    },
    zip_safe=False
)
