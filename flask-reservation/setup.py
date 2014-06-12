"""
Flask-Reservation
----------------------------------------------------------------------

"""
from setuptools import setup


setup(
    name='Flask-Reservation',
    version='1.0',
    url='https://github.com/cloudmesh/reservation',
    license='Apache2',
    author='Gregor von Laszewski',
    author_email='laszewski@gmail.com',
    description='Managing Reservations in flask',
    long_description=__doc__,
    py_modules=['flask_reservation'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_reservation'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
