from setuptools import setup, find_namespace_packages


def _read(filename: str) -> str:
    """
    Reads in the content of the file.

    :param filename:    The file to read.
    :return:            The file content.
    """
    with open(filename, "r") as file:
        return file.read()


setup(
    name="wai.annotations.generic",
    description="Module with generic plugins for wai.annotations that use user specified classes.",
    long_description=f"{_read('DESCRIPTION.rst')}\n"
                     f"{_read('CHANGES.rst')}",
    url="https://github.com/waikato-datamining/wai-annotations-generic",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
    ],
    license='Apache License Version 2.0',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    namespace_packages=[
        "wai",
        "wai.annotations"
    ],
    version="1.0.0",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    install_requires=[
        "wai.annotations.core>=0.1.7"
    ],
    entry_points={
        "wai.annotations.plugins": [
            # ISPs
            "generic-isp-ac=wai.annotations.generic.isp.audio_classification.specifier:AudioClassificationISPSpecifier",
            "generic-isp-ic=wai.annotations.generic.isp.image_classification.specifier:ImageClassificationISPSpecifier",
            "generic-isp-is=wai.annotations.generic.isp.image_segmentation.specifier:ImageSegmentationISPSpecifier",
            "generic-isp-od=wai.annotations.generic.isp.object_detection.specifier:ObjectDetectionISPSpecifier",
            "generic-isp-sp=wai.annotations.generic.isp.speech.specifier:SpeechISPSpecifier",
        ]
    }
)
