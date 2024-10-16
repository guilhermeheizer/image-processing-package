from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Guilherme Heizer Nogueira da Gama",
    author_email="guilhermeheizer@gmail.com",
    description="Pacote de imagens",
    long_description="Pacote de imagens",
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermeheizer/image-processing-package",
    install_requires=requirements,
    python_requires='>=3.8',
)