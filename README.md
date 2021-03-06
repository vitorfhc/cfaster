[![codebeat badge](https://codebeat.co/badges/5f8a6b47-d5e3-42a9-aefc-bfb0d604bbbc)](https://codebeat.co/projects/github-com-vitorfhc-cfaster-master)
[![Maintainability](https://api.codeclimate.com/v1/badges/fa7bac7194b4d0c7e28b/maintainability)](https://codeclimate.com/github/vitorfhc/CFaster/maintainability)


# CFaster

CFaster is a tool to easily set all you need to start a contest problem as fast as possible.

## Get CFaster

If you want to install CFaster all you need is [pip](https://pypi.org/project/pip/) for Python 3 and running

```bash
pip install cfaster
```

## Usage

```bash
Usage: cfaster [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose  Output INFO level logs.
  -d, --debug    Output DEBUG level logs.
  --help         Show this message and exit.

Commands:
  scrape  Scrapes the problem and saves inputs and outputs.
```

## Example

This command will scrape the problem from the link and get all the inputs and outputs in `.txt` files.

```bash
cfaster scrape https://codeforces.com/contest/1174/problem/A
```

In the future we will have a `cfaster test` command for running your code, testing the inputs, comparing with the outputs and giving you the results.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For the default isolated development environment used by the maintainers you will need:

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)(optional)
- [Make](https://opensource.com/article/18/8/what-how-makefile)(optional)

If you prefer not using Docker feel free to use any other you prefer, but the CI integration will be running with Docker images so this is the best way to replicate the production environment.

### Installing

This project uses [Docker](https://docs.docker.com/install/) for creating the isolated development environment.

You can run the Dockerfile build and run the container manually with

```bash
docker build -t cfaster .
docker run -it --rm -v $(pwd):/cfaster cfaster bash
```

or you can use Make and docker-compose to easily get everything running

```bash
make dev 
```

Reading the Makefile shows what each target does.

### Using

You will have two options on how to execute from source code

```bash
python -m cfaster
```

or

```bash
python setup.py install
cfaster
```

## Running the tests

### Automated tests

The tests for the CFaster are yet to be implemented, the software still in early alpha version.

### Coding style tests

CFaster uses PEP8, for running a verification if your code is according to the rules use `pycodestyle .` which will recursively run through all files and find any mistakes.

For fixing them automatically we use `autopep8`

```bash
autopep8 -r --diff . # this will show the diff after the fixing
autopep8 -r --in-place . # and this will fix in place the files
```

We recommend always checking the diff first.

## Deployment

For now we don't have a deployment pipeline, but in the future it will be automated using [CI](https://en.wikipedia.org/wiki/Continuous_integration) and [CD](https://en.wikipedia.org/wiki/Continuous_deployment) deploying the package to [pypi](https://pypi.org/).

## Built With

* [Python 3](https://www.python.org/) - The coding language used
* [Click](https://click.palletsprojects.com/en/7.x/) - The command line interface package
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used to help scrapping the pages.

## Contributing

If you want to contribute to the project please read [CONTRIBUTING](CONTRIBUTING.md)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/vitorfhc/cfaster/tags). 

## Authors

* **Vitor Falcão** - *Starter and main maintainer* - [vitorfhc](https://github.com/vitorfhc)

As soon as we get out first contribution we will start the file with contributors.

## License

This project is licensed under the GPL-3.0 - see the [LICENSE.md](LICENSE.md) file for details
