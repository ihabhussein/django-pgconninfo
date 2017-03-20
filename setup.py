from setuptools import setup

setup(
    name='django-pgconninfo',
    version='0.1',
    description='PostgreSQL connection info from invironment variables',
    url='http://github.com/ihabhussein/django-pgconninfo',
    author='Ihab Hussein',
    author_email='ihab@ihabhussein.com',
    license='BSD',
    packages=['django-pgconninfo'],
    install_requires=[
        "pgpasslib >= 1.1.0",
    ],
    zip_safe=True
)
