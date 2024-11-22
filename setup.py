#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

# from setuptools import setup
# from torch.utils.cpp_extension import CUDAExtension, BuildExtension
# import os
# os.path.dirname(os.path.abspath(__file__))

# setup(
#     name="project_rasterization",
#     packages=['project_rasterization'],
#     ext_modules=[
#         CUDAExtension(
#             name="project_rasterization._C",
#             sources=[
#             "cuda_rasterizer/rasterizer_impl.cu",
#             "cuda_rasterizer/forward.cu",
#             "cuda_rasterizer/backward.cu",
#             "rasterize_points.cu",
#             "ext.cpp"],
#             # extra_compile_args={"nvcc": ["-Xcompiler", "-fno-gnu-unique","-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")]})
#             extra_compile_args={"nvcc": ["-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")]})
#         ],
#     cmdclass={
#         'build_ext': BuildExtension
#     }
# )

import os

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension

# Package metadata
NAME = "project_rasterization"
VERSION = "1.0"
DESCRIPTION = "project_rasterization"
URL = "https://github.com/moonite1209/langsplat-rasterization"
AUTHOR = "moonite"
AUTHOR_EMAIL = "moonite1209@qq.com"
LICENSE = "Apache 2.0"

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# Required dependencies
REQUIRED_PACKAGES = [
    "torch>=2.3.1",
]

EXTRA_PACKAGES = {
}

# Catch and skip errors during extension building and print a warning message
# (note that this message only shows up under verbose build mode
# "pip install -v -e ." or "python setup.py build_ext -v")
CUDA_ERROR_MSG = (
    "{}\n\n"
    "Failed to build the SAM 2 CUDA extension due to the error above. "
    "You can still use SAM 2 and it's OK to ignore the error above, although some "
    "post-processing functionality may be limited (which doesn't affect the results in most cases; "
    "(see https://github.com/facebookresearch/segment-anything-2/blob/main/INSTALL.md).\n"
)

def get_extensions():
    from torch.utils.cpp_extension import CUDAExtension

    srcs = [
        "cuda_rasterizer/rasterizer_impl.cu",
        "cuda_rasterizer/forward.cu",
        "cuda_rasterizer/backward.cu",
        "rasterize_points.cu",
        "ext.cpp"]
    compile_args = {
        "cxx": [],
        "nvcc": [
            "-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/")
        ],
    }
    ext_modules = [CUDAExtension("project_rasterization._C", srcs, extra_compile_args=compile_args)]
    return ext_modules

cmdclass = {
        "build_ext": (
            BuildExtension.with_options(no_python_abi_suffix=True)
        )
    }

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(exclude="notebooks"),
    package_data={"": ["*.yaml"]},  # SAM 2 configuration files
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRA_PACKAGES,
    python_requires=">=3.10.0",
    ext_modules=get_extensions(),
    cmdclass=cmdclass,
)