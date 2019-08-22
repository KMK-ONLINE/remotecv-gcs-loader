from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="remotecv_gcs_loader",
    version="0.0.1",
    description="Load assets from Google Cloud Storage for remotecv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KMK-ONLINE/remotecv-gcs-loader",
    author="Kreatif Media Karya",
    author_email="admin.it@kmklabs.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    packages=["remotecv_gcs_loader"],
    install_requires=["google-cloud-storage"]
)
