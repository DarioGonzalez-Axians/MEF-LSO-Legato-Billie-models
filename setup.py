# @Author            : Dario Gonzalez
# @Date              : 2021-11-29
# @Last Modified by  : Dario Gonzalez
# @Last Modified time: 2021-12-01

import setuptools


DESCRIPTION = "Implements the MEF-LSO-Legato models for Pydantic/FastAPI"

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        LONG_DESCRIPTION = fh.read()
except IOError:
    LONG_DESCRIPTION = DESCRIPTION

setuptools.setup(
    name                          = "meflsolegato-models",
    version                       = "1.0",
    description                   = DESCRIPTION,
    long_description              = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    author                        = "Axians Spain Development Team",
    author_email                  = "desarrollosoftware@axians.es",
    python_requires               = ">=3.9",
    packages                      = ['models'],
    install_requires              = ["pydantic==1.8.2"],
    extras_require                = {},
    include_package_data          = True,
    entry_points                  = {}
)
