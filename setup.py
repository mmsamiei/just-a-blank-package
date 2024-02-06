from setuptools import setup, find_packages
import os
import re
from urllib.parse import urlparse



def get_install_requires():
    base_path = os.path.dirname(os.path.abspath(__file__))
    requirements_file_path = os.path.join(base_path, 'requirements.txt')
    with open(requirements_file_path, 'r') as requirements_file:
        requirements = requirements_file.readlines()
        requirements = [req.strip() for req in requirements if req]

        install_requires = []
        for req in requirements:
            if req.startswith("--"):
                continue
            
            parsed_req = urlparse(req)
            if parsed_req.scheme == '':
                install_requires.append(req)
            else:
                req_name = re.findall(r'egg=(\w+)$', parsed_req.fragment)[0]
                install_requires.append('{0} @ {1}'.format(req_name, req))

    return install_requires



setup(
    name='justablank',
    version='0.0.0',
    packages=find_packages(),
    author="Mahdi Samiei",
    license="MIT",
    install_requires=get_install_requires(),
)
