from setuptools import setup, find_packages

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
