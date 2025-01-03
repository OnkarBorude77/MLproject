from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(requiements:str)->List[str]:
    
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
            return requirements
    

setup(
    name='Mlproject',
    version='0.0.1',
    author='onkar',
    author_email='onkar.wugwg22@sinhgad.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    )