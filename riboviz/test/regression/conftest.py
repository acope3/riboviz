"""
pytest plugin file for regression tests. See
https://docs.pytest.org/en/latest/writing_plugins.html

This allows pytest to take in additional command-line parameters to
pass onto regression test modules:

* ``--expected=<DIRECTORY>``: Directory with expected data files,
  against which files specified in the configuration file (see below)
  will be checked.
* ``--skip-workflow``: Workflow will not be run prior to checking data
  files. This can be used to check existing files generated by a run
  of the workflow.
* ``--check-index-tmp``: Check index and temporary files (default is
  that only the output files are checked).
* ``--config-file``: Configuration file. If provided then the index,
  temporary and output directories specified in this file will be
  validated against those specified by ``--expected``. If not provided
  then the file :py:const:`riboviz.test.VIGNETTE_CONFIG` will be
  used. The configuration file must specify demultiplexed samples
  (i.e. it should use :py:const:`riboviz.params.FQ_FILES` and not
  :py:const:`riboviz.params.MULTIPLEX_FQ_FILES`).
"""
import os.path
import pytest
import yaml
from riboviz import params
from riboviz import test

EXPECTED = "--expected"
""" Directory with expected data files command-line flag."""
SKIP_WORKFLOW = "--skip-workflow"
""" Do not run workflow command-line flag. """
CHECK_INDEX_TMP = "--check-index-tmp"
""" Check index and temporary files command-line flag. """
CONFIG_FILE = "--config-file"
""" Configuration file command-line flag. """


def pytest_addoption(parser):
    """
    pytest configuration hook. See
    https://docs.pytest.org/en/latest/reference.html#_pytest.hookspec.pytest_addoption

    :param parser: command-line parser
    :type parser: _pytest.config.argparsing.Parser
    """
    parser.addoption(EXPECTED,
                     action="store",
                     required=True,
                     help="Directory with expected data files")
    parser.addoption(SKIP_WORKFLOW,
                     action="store_true",
                     required=False,
                     help="Do not run workflow")
    parser.addoption(CHECK_INDEX_TMP,
                     action="store_true",
                     required=False,
                     help="Check index and temporary files")
    parser.addoption(CONFIG_FILE,
                     action="store",
                     required=False,
                     help="Configuration file")


@pytest.fixture(scope="module")
def expected_fixture(request):
    """
    Gets value for ``--expected`` command-line option.

    :param request: request
    :type request: _pytest.fixtures.SubRequest
    :return: directory
    :rtype: str or unicode
    :raise AssertionError: if the option has a value that is \
    not a directory
    """
    expected_dir = request.config.getoption(EXPECTED)
    assert os.path.exists(expected_dir) and os.path.isdir(expected_dir),\
        "No such directory: %s" % expected_dir
    return expected_dir


@pytest.fixture(scope="module")
def skip_workflow_fixture(request):
    """
    Gets value for ``--skip-workflow`` command-line option.

    :param request: request
    :type request: _pytest.fixtures.SubRequest
    :return: flag
    :rtype: bool
    """
    return request.config.getoption(SKIP_WORKFLOW)


@pytest.fixture(scope="module")
def skip_index_tmp_fixture(request):
    """
    Gets value for `--check-index-tmp` command-line option. If
    ``False``, or undefined, invokes ``pytest.skip`` to skip
    test.

    :param request: request
    :type request: _pytest.fixtures.SubRequest
    :return: flag
    :rtype: bool
    """
    if not request.config.getoption(CHECK_INDEX_TMP):
        pytest.skip('Skipped index and temporary files tests')


@pytest.fixture(scope="module")
def config_fixture(request):
    """
    Gets value for ``--config-file`` command-line option.

    :param request: request
    :type request: _pytest.fixtures.SubRequest
    :return: configuration file
    :rtype: str or unicode
    """
    if request.config.getoption(CONFIG_FILE):
        config_file = request.config.getoption(CONFIG_FILE)
    else:
        config_file = test.VIGNETTE_CONFIG
    return config_file


def pytest_generate_tests(metafunc):
    """
    Parametrize tests using information within a configuration file.

    * If :py:const:`CONFIG_FILE` has been provided then use this as a
      configuration file, else use
      :py:const:`riboviz.test.VIGNETTE_CONFIG`.
    * Load configuration from file.
    * Inspect each test fixture used by the test functions and
      configure with values from the configuration:
        - ``sample``: keys from value of
          :py:const:`riboviz.params.FQ_FILES` (sample names).
          If :py:const:`riboviz.test.VIGNETTE_CONFIG` configuration
          file is being used then key
          :py:const:`riboviz.test.VIGNETTE_MISSING_SAMPLE` is
          removed.
        - ``index_prefix``: value of
          :py:const:`riboviz.params.ORF_INDEX_PREFIX` and
          :py:const:`riboviz.params.RRNA_INDEX_PREFIX`.
        - ``index_dir``: value of
          :py:const:`riboviz.params.INDEX_DIR`.
        - ``tmp_dir``: value of :py:const:`riboviz.params.TMP_DIR`.
        - ``output_dir``: value of
          :py:const:`riboviz.params.OUTPUT_DIR`.

    :param metafunc: pytest test function inspection object
    :type metafunc: _pytest.python.Metafunc
    :raise AssertionError: if the configuration file does not \
    exist or is not a file
    """
    if metafunc.config.getoption(CONFIG_FILE):
        config_file = metafunc.config.getoption(CONFIG_FILE)
    else:
        config_file = test.VIGNETTE_CONFIG
    assert os.path.exists(config_file) and os.path.isfile(config_file),\
        "No such file: %s" % config_file
    with open(config_file, 'r') as f:
        config = yaml.load(f, yaml.SafeLoader)
    if "sample" in metafunc.fixturenames:
        samples = list(config[params.FQ_FILES].keys())
        if config_file == test.VIGNETTE_CONFIG and \
           test.VIGNETTE_MISSING_SAMPLE in samples:
            samples.remove(test.VIGNETTE_MISSING_SAMPLE)
        metafunc.parametrize("sample", samples)
    if "index_prefix" in metafunc.fixturenames:
        metafunc.parametrize("index_prefix",
                             [config[params.ORF_INDEX_PREFIX],
                              config[params.RRNA_INDEX_PREFIX]])
    if "index_dir" in metafunc.fixturenames:
        metafunc.parametrize("index_dir", [config[params.INDEX_DIR]])
    if "tmp_dir" in metafunc.fixturenames:
        metafunc.parametrize("tmp_dir", [config[params.TMP_DIR]])
    if "output_dir" in metafunc.fixturenames:
        metafunc.parametrize("output_dir", [config[params.OUTPUT_DIR]])
