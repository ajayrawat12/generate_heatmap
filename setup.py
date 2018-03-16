from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as f:
        return f.readlines()


setup(name='generate_heatmap',
      version='0.1',
      description='Generate heatmap from the video for usage analysis.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: Apache 2.0 License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Video Processing :: Images',
      ],
      keywords='Generate Heatmap from video',
      url='https://github.com/ajayrawat12/generate_heatmap',
      author='Ajay Rawat',
      author_email='ajayrawat12@outlook.com',
      package_data={'': ['LICENSE']},
      license='Apache 2.0',
      packages=['generate_heatmap'],
      install_requires=get_requirements(),
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['generate_heatmap=generate_heatmap.command:main'],
      },
      include_package_data=True,
      zip_safe=False)
