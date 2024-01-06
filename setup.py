import os
import re
from codecs import open

from setuptools import find_packages, setup

# Based on https://github.com/pypa/sampleproject/blob/main/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
long_description_content_type = "text/markdown"

with open(os.path.join(here, "mitmproxy/version.py")) as f:
    match = re.search(r'VERSION = "(.+?)"', f.read())
    assert match
    VERSION = match.group(1)

setup(
    name="mitmproxy",
    version=VERSION,
    description="An interactive, SSL/TLS-capable intercepting proxy for HTTP/1, HTTP/2, and WebSockets.",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url="http://mitmproxy.org",
    author="Aldo Cortesi",
    author_email="aldo@corte.si",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],
    project_urls={
        "Documentation": "https://docs.mitmproxy.org/stable/",
        "Source": "https://github.com/mitmproxy/mitmproxy/",
        "Tracker": "https://github.com/mitmproxy/mitmproxy/issues",
    },
    packages=find_packages(
        include=[
            "mitmproxy",
            "mitmproxy.*",
        ]
    ),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mitmproxy = mitmproxy.tools.main:mitmproxy",
            "mitmdump = mitmproxy.tools.main:mitmdump",
            "mitmweb = mitmproxy.tools.main:mitmweb",
        ],
        "pyinstaller40": [
            "hook-dirs = mitmproxy.utils.pyinstaller:hook_dirs",
        ]
    },
    python_requires=">=3.9",
    # https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires
    # It is not considered best practice to use install_requires to pin dependencies to specific versions.
    install_requires=[
        "asgiref>=3.2.10",
        "Brotli>=1.0",
        "certifi>=2019.9.11",  # no semver here - this should always be on the last release!
        "cryptography>=38.0",
        "flask>=1.1.1",
        "h11>=0.11",
        "h2>=4.1",
        "hyperframe>=6.0",
        "kaitaistruct>=0.10",
        "ldap3>=2.8",
        "mitmproxy_wireguard>=0.1.6",
        "msgpack>=1.0.0",
        "passlib>=1.6.5",
        "protobuf>=3.14",
        "pyOpenSSL>=22.1",
        "pyparsing>=2.4.2",
        "pyperclip>=1.6.0",
        "ruamel.yaml>=0.16",
        "sortedcontainers>=2.3",
        "tornado>=6.1",
        "urwid>=2.1.1",
        "wsproto>=1.0",
        "publicsuffix2>=2.20190812",
        "zstandard>=0.11",
        "typing-extensions>=4.3; python_version<'3.10'",
    ],
    extras_require={
        ':sys_platform == "win32"': [
            "pydivert>=2.0.3,<2.2",
        ],
        "dev": [
            "click>=7.0,<8.2",
            "hypothesis>=5.8,<7",
            "parver>=0.1,<2.0",
            "pdoc>=4.0.0",
            "pyinstaller==5.6.2",
            "pytest-asyncio>=0.17,<0.21",
            "pytest-cov>=2.7.1,<4.1",
            "pytest-timeout>=1.3.3,<2.2",
            "pytest-xdist>=2.1.0,<3.1",
            "pytest>=6.1.0,<8",
            "requests>=2.9.1,<3",
            "tox>=3.5,<4",
            "wheel>=0.36.2,<0.39",
        ],
    },
)
