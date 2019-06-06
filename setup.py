import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as r:
    requirements = r.readlines()

with open('VERSION.txt', 'r') as v:
    version = v.read().strip()

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
]

entry_points = {
    'console_scripts': [
        'cfaster=cfaster.__main__:main_cmd',
    ]
}

setuptools.setup(
    name="cfaster",
    version=version,
    author="Vitor Falcão Costa",
    author_email="vitorfhcosta@gmail.com",
    description="A package to get all you need to start a\
            programming contest as fast as possible",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitorfhc/cfaster",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    entry_points=entry_points,
    keywords=["contest", "scraper", "tools", "codeforces", "uva"],
    install_requires=requirements,
)
