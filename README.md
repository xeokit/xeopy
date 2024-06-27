# xeopy = xeokit + Python (Work in progress project)

## Description

xeopy is a library which allows to create xeokit scenes using Python.

xeopy is fully written in Python.

It is currently a proof-of-concept prototype. Use on your own risk.

The scope, namings and structure of it is changing rapidly, that's why it's not published as a PIP package right now.

xeokit itself is a web programming toolkit for AEC graphics. Find more here: https://xeokit.io/

## Features

Right now you can control some things regarding:
- Box
- Mesh
- Sphere
- VectorText
- CameraSettings
- WebIFCLoaderPlugin
- XKTLoaderPlugin
- Viewer
- SectionPlanes

I'm open to hear suggestion regarding what should be added. Please open an issue here and let me know! :)

## Example files

![Examples](imgs/examples_image.png)

You will find example files here: https://github.com/xeokit/xeopy/tree/master/xeopy/tests/examples

## How to run it

1. Clone this repository and configure Python interpreter
2. Run one of the example .py files -> it should generate html file
3. Run generated html file on localhost. Some IDEs (such as PyCharm) will let you do it with one click of a button (for PyCharm just open generated html file and click web-browser logo).

There is no yet PyPi package published, as it is a prototype.

## How it works

xeopy concept is really simple: underneath it creates an html file filled with JS code which uses Xeokit. Later you can open such html file and see the results.

## License

Find the license here: https://github.com/xeokit/xeopy/blob/master/LICENSE.md

## Development

### Setup

After clone it's good to create a venv (virtual environment).

In Pycharm you can do it like this:

![Venv_pycharm](imgs/venv_pycharm.png)

### Architecture

Idea is that each small Python object should represent in **str** a tiny slice of JS code.

All these objects can be later put into **content** property of Xeokit object, so they can generate full code definition, if put in proper order.

### Unit tests

You can find and run unit tests inside the project here: https://github.com/xeokit/xeopy/tree/master/xeopy/tests/unit_tests

To run these tests you will also need to install pytest library.

In Pycharm you can run all the tests by right-clicking the unit_tests folder and clicking to run all tests.

![Unittest_pycharm](imgs/unittest_pycharm.png)

You can also install coverage package to see code coverage.

In Pycharm it's Run -> Run 'Python tests in unit_tests' with Coverage

## E2E tests for Xeokit examples itself

There is an endtoend_xeokit_tests folder where you can optionally build E2E test for Xeokit itself.

It uses Selenium to build test these things. To run it you need to place a geckodriver (0.34.0, https://github.com/mozilla/geckodriver/releases)
exactly where the .py file is located.

It will also require a proper version of browser installed.
