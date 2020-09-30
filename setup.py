from setuptools import dist
dist.Distribution().fetch_build_eggs(['numpy>=1.17'])

long_description = """
A numpy binding for the Poisson E-Test, described in this paper:

http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf

I basically just minimally edited the original fortran code so that numpy f2py
could pick it up. The original code can be found in an early commit to this repo
or via this link:

http://www.ucs.louisiana.edu/~kxk4695/statcalc/pois2pval.for
"""

if __name__ == "__main__":
    from numpy.distutils.core import setup, Extension
    fortran_ext = Extension(
        "poisson_etest.poisson_etest_fortran", sources=["lib/poisson_etest.f"]
    )

    setup(
        name="poisson_etest",
        version="0.1",
        url="https://github.com/NickHilton/poisson-etest",
        packages=["poisson_etest"],
        description="A poisson e-test.",
        long_description=long_description,
        ext_modules=[fortran_ext],
        package_dir={"poisson_etest": "lib"},
        setup_requires=["numpy>=1.17.0,<2"],
        install_requires=["numpy>=1.17.0,<2"]
    )
