from setuptools import setup


def _read_requires_text_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="embook",
    version="0.0.1",
    python_requires=">=3.9.0",
    install_requires=_read_requires_text_from_file('requirements.txt'),
)