from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "ML PROJECT"
VERSION = "0.0.1"
DESCRIPITION = "This is Machine Learning project with Modular Coding"
AUTHOR = "Shailesh Gaddam"
AUTHOR_EMAIL = "shaileshgaddam10@gmail.com"

requirements = "requirements.txt"

HYPEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(requirements) as file_obj:
        requirements_list = file_obj.readlines()
        requirements_list = [req.replace("\n", "") for req in requirements_list]

        if HYPEN_E_DOT in requirements_list:
            requirements_list.remove(HYPEN_E_DOT)

        return requirements_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPITION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements()
     )