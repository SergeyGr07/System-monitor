from setuptools import find_packages, setup

setup(
    name="system-monitor",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "psutil",
        "pywebview",
    ],
)
