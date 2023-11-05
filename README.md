<h1 align="center" >Py Sberbank Payments</h1>

<p align="center">
	<a href="https://pypi.org/project/py_sberbank_payments">
		<img src="https://img.shields.io/pypi/status/py_sberbank_payments.svg" alt="PyPI - Status" />
	</a>
	<a href="https://pypi.org/project/py_sberbank_payments">
		<img src="https://img.shields.io/pypi/v/py_sberbank_payments.svg" alt="PyPI - Version" />
	</a>
	<a href="https://pypi.org/project/py_sberbank_payments">
		<img src="https://img.shields.io/pypi/dm/py_sberbank_payments.svg" alt="PyPI - Downloads" />
	</a>
	<a href="https://pypi.org/project/py_sberbank_payments">
		<img src="https://img.shields.io/pypi/pyversions/py_sberbank_payments.svg" alt="PyPI - Python Version" />
	</a>
	<a href="https://pypi.org/project/py_sberbank_payments">
		<img src="https://img.shields.io/pypi/format/py_sberbank_payments.svg" alt="PyPI - Format" />
	</a>
</p>
<p align="center">
	<a href="https://github.com/gocream/py_sberbank_payments/actions/workflows/mkdocs-release.yml" >
		<img src="https://img.shields.io/github/actions/workflow/status/gocream/py_sberbank_payments/mkdocs-release.yml?logo=github&label=docs" alt="Documentation - Release" />
	</a>
	<!-- <a href="https://github.com/gocream/py_sberbank_payments/actions/workflows/test.yml" >
		<img src="https://img.shields.io/github/actions/workflow/status/gocream/py_sberbank_payments/test.yml?logo=github&label=tests" alt="Tests - Running" />
	</a> -->
	<!-- <a href="https://codecov.io/gh/gocream/py_sberbank_payments" >
		<img src="https://codecov.io/gh/gocream/py_sberbank_payments/branch/main/graph/badge.svg?token=HV1QGD74EK" alt="Tests - Coverage" />
	</a> -->
</p>
<p align="center">
	<a href="https://github.com/pypa/hatch" target="_blank">
		<img src="https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg" alt="Hatch project" />
	</a>
	<a href="https://squidfunk.github.io/mkdocs-material/" target="_blank">
		<img src="https://img.shields.io/badge/docs-mkdocs_material-blue?logo=mdbook&logoColor=white" alt="Material for MkDocs" />
	</a>
	<a href="https://github.com/charliermarsh/ruff" target="_blank">
		<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="linting - Ruff" />
	</a>
	<a href="https://github.com/psf/black" target="_blank">
		<img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code style - black" />
	</a>
	<a href="https://raw.githubusercontent.com/gocream/py_sberbank_payments/master/LICENSE" target="_blank">
		<img src="https://img.shields.io/pypi/l/py_sberbank_payments?color=008033" alt="License - GNU Lesser General Public License v3.0" />
	</a>
</p>

Python wrapper for [Sberbank Payments API](https://securepayments.sberbank.ru/wiki/doku.php/start).

Тестовые карты - [link][test_cards]


## Development

`pip install -e .[dev]`


## TO DO:

* all errors inheritance SberbankException and raise them
* add all params from api to class methods arguments
* unittests
* test flask app


[test_cards]: https://securepayments.sberbank.ru/wiki/doku.php/test_cards
