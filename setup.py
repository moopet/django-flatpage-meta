from setuptools import setup, find_packages
setup(
    name='django-flatpage-meta',
    version='0.0.2',
    description='A simple app to add meta tag support to flatpages',
    author="Ben Sinclair",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1  - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
