from setuptools import setup

setup(
    name='gymnosfirestoreapi',
    version='0.4.0',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    packages=['gymnos_firestore'],
    install_requires=['firebase-admin==2.17.0', 'matchbox-orm==0.2.4'],
)