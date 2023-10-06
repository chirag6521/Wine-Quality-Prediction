import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine-Quality-Prediction"
AUTHOR_USER_NAME = "Chirag6521"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "chiragsingh38988@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small Python app package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)
