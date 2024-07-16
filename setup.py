from setuptools import find_packages, setup
from typing import List
hyphen='-e .'
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hyphen in requirements:
            requirements.remove(hyphen)

setup(
    name='LSTM_RNN',
    version='1.0.0',
    author='Samarth Garg',
    author_email='samarthgarg8099@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)