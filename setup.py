from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='tkwikipage',
    version='1.4',
    description='Send email with smtp setup',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='tuan.dv',
    author_email='tuan.dv@teko.vn',
    keywords=['wiki', 'Wiki', 'Md', 'md', 'page'],
    url='https://github.com/dotuan0601/tkwikipage',
    download_url='https://pypi.org/project/tkwikipage/'
)

install_requires = []

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)