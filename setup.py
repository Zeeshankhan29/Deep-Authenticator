from setuptools import find_packages,setup
from typing import List



def get_requirements()->List[str]:
    with open('requirements.txt') as f:
        requirements_list = f.readlines()
        requirements_list =  [data.replace('\n','') for data in requirements_list]
    if '-e .' in requirements_list:
        requirements_list.remove('-e .')
    return requirements_list


setup(name='Deep-Authenticator',
      version='0.0.1',
      description='Face authentication system',
      author='Zeeshan Khan',
      author_email='zeeshankhan29khan@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements()
     )

if __name__=="__main__":
    print(get_requirements())