# To install local package in virtual enviornment we create this file

from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.0.1",
    author="saksham shinde",
    author_email="sakshamshinde412@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)