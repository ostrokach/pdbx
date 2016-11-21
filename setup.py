from setuptools import setup

setup(
    name='pdbx-mmcif',
    packages=['pdbx', 'pdbx.writer', 'pdbx.reader'],
    version='0.0.1',
    description="Parser for structures in the protein data bank (PDB) in the mmCIF format",
    author="various",
    url="https://github.com/ostrokach/pdbx",
    keywords=['protein', 'pdb'],
    classifiers=[
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3',
    ]
)
