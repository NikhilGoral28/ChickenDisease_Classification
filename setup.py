import setuptools

with open("README.md",'r', encoding='utf-8') as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME = 'ChickenDisease_Classification'
AUTHOR_USER_NAME = "Nikhil"
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'nikhilgoral587@gmail.com'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CNN app",
    Long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/NikhilGoral28/ChickenDisease_Classification',
    project_urls={
        "Bug Tracker": f"https://github.com/NikhilGoral28/ChickenDisease_Classification/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')

)