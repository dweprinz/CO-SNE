from setuptools import setup

setup(
    name="cosne",
    version="0.0.1",
    packages=["hyptorch", "pvae"],
    install_requires=[
        "numpy", "pillow", "scikit-learn", "scipy",
        "seaborn", "torch", "torchvision",
        "geoopt @ git+https://github.com/geoopt/geoopt.git",
    ],
    python_requires=">=3.11",
)
