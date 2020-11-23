"""
sdist - copy all dropbear files (defined in MANIFEST.in) and compile on setup
bdist_wheel - distributed with precompiled dropbear
"""
import os
from distutils.command.build import build
from distutils.command.install import install
from subprocess import check_call

from setuptools import setup

BASEPATH = os.path.dirname(os.path.abspath(__file__))
DROPBEAR_PATH = os.path.join(BASEPATH, "dropbear")


class DropbearBuild(build):
    def run(self):
        build.run(self)

        def compile():
            check_call("autoconf", cwd=DROPBEAR_PATH)
            check_call("autoheader", cwd=DROPBEAR_PATH)
            check_call("./configure", cwd=DROPBEAR_PATH)
            check_call(
                'make PROGRAMS="dropbear dbclient dropbearkey" MULTI=1',
                cwd=DROPBEAR_PATH,
                shell=True,
            )

        self.execute(compile, [], "Building Dropbear")
        self.mkpath(self.build_lib)

        if not self.dry_run:
            bin_path = os.path.join(DROPBEAR_PATH, "dropbearmulti")
            self.copy_file(bin_path, self.build_lib + "/pysshserver")


class DropbearInstall(install):
    def run(self):
        self.copy_tree(self.build_lib, self.install_lib)
        install.run(self)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pysshserver",
    version="0.0.1",
    author="u1234x1234",
    author_email="u1234x1234@gmail.com",
    description=("pysshserver"),
    license="MIT",
    keywords="",
    url="https://github.com/u1234x1234/pysshserver",
    packages=["pysshserver"],
    zip_safe=False,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    cmdclass={
        "build": DropbearBuild,
        "install": DropbearInstall,
    },
)
