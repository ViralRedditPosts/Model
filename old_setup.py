# #!/usr/bin/env python
# # good reference: https://github.com/boto/boto3/blob/develop/setup.py
# from setuptools import find_packages, setup
#
# # install_requires = [
# #     "boto3==1.26.117",
# #     "matplotlib==3.3.4",
# #     "numpy==1.21.6",  # required by pyspark
# #     "pandas==1.0.5",  # required by pyspark
# #     "pg8000==1.29.4",  # this was easier to pip install than psycopg2
# #     "pyarrow==2.0.0",
# #     "pyspark==3.3.0",  # using this version because py37 deprecated in pyspark 3.4.0
# #     "requests==2.31.0",
# #     "scikit-learn==1.0.2",
# #     "seaborn==0.11.2",
# #     "shap==0.41.0",
# #     "sqlalchemy==1.4.46",  # originally tried 2.0.10, but this was incompatible with old versions of pandas https://stackoverflow.com/a/75282604/5034651,
# #     "viral_reddit_posts_utils @ git+https://github.com/ViralRedditPosts/Utils.git@main",
# # ]
# #
# # test_requires = [
# #     "moto[dynamodb,s3]==4.1.8",
# #     "pytest==7.3.1",
# #     "pytest-cov==4.0.0",
# # ]+install_requires
# #
# # build_requires = ["flake8", "black"] + test_requires
# # dev_requires = ["pre-commit==2.21.0"] + build_requires
#
# setup(name='viral_reddit_posts_model',
#       version='0.0.1',
#       description='Model for Viral Reddit Posts project',
#       author='Kenneth Myers',
#       url='https://github.com/ViralRedditPosts',
#       packages=find_packages(exclude=['tests*']),
#       python_requires=">= 3.7",
#       # install_requires=install_requires,
#       # extras_require={
#       #     'test':test_requires,
#       #     'build':build_requires,
#       #     'dev':dev_requires
#       # }
#      )