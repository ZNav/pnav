import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.txt").read_text()

setuptools.setup(
    name='pnav',
    version='0.2.4',
    author='Zander Navratil',
    description="Package with random functions, some are useful, some aren't so much. They are however used often, maintained, and good for learning.",
    packages=['pnav'],
    long_description=long_description,
    long_description_content_type='text/markdown')