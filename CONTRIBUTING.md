# Contributing to openfoodfacts-python

Any help is welcome, as long as you don't break the continuous integration.
Fork the repository and open a Pull Request directly on the `develop` branch.
A maintainer will review and integrate your changes.

Maintainers:

- [Anubhav Bhargava](https://github.com/Anubhav-Bhargava)
- [Frank Rousseau](https://github.com/frankrousseau)
- [Pierre Slamich](https://github.com/teolemon)
- [Raphaël](https://github.com/raphael0202)

Contributors:

- Agamit Sudo
- [Daniel Stolpe](https://github.com/numberpi)
- [Enioluwa Segun](https://github.com/enioluwas)
- [Nicolas Leger](https://github.com/nicolasleger)
- [Pablo Hinojosa](https://github.com/Pablohn26)
- [Andrea Stagi](https://github.com/astagi)
- [Benoît Prieur](https://github.com/benprieur)
- [Aadarsh A](https://github.com/aadarsh-ram)

## How to install on your local machine

Make sure you have [uv](https://docs.astral.sh/uv/) installed, then run:

```
uv sync --all-extras
```

## Install pre-commit hooks

This repo uses [pre-commit](https://pre-commit.com/) to enforce code styling, etc. To install it, run the following:

```
uv run pre-commit install
```

Now `pre-commit` will run automatically on `git commit` :)

## Write and run tests

You should create basic tests for each new feature or API change.

To run tests locally, just launch:

```
uv run pytest tests
```
