# GymnosFirestoreAPI

## Installation
To get a dev version: 
```
pip install gymnosfirestoreapi===0.1.0 --trusted-host thefirstjedi.asuscomm.com --index-url http://thefirstjedi.asuscomm.com:3141/gymnos/staging/+simple gymnosfirestoreapi===0.1.0
```
To get the latest version:
```
pip install GymnosFirestoreAPI --upgrade --trusted-host thefirstjedi.asuscomm.com --index-url http://thefirstjedi.asuscomm.com:3141/gymnos/staging/+simple
```
To uninstall this library, simply run `pip uninstall gymnosfirestoreapi`

## Building

To build this library, ensure you are in a virtualenv, and install the requirements from the main
directory.

Run the following command from this directory:

```bash
python3 setup.py sdist
```

## Publishing

To publish this library, ensure you are in a virtualenv, and install 'devpi-client'

```bash
pip install devpi-client
```

Choose which repository to upload to:

1) Stable (cannot overwrite uploaded versions!)
    ```bash
    devpi use http://thefirstjedi.asuscomm.com:3141/gymnos/stable
    ```
2) Staging (can overwrite uploaded versions)
    ```bash
    devpi use http://thefirstjedi.asuscomm.com:3141/gymnos/staging
    ```
Log into the server as user 'gymnos' (see google drive 'Shared Credentials' for password)

```bash
> devpi login gymnos
password for user gymnos:
logged in 'gymnos', credentials valid for 10.00 hours
```

Ensure you are in the root directory of this repository and upload using devpi:

```bash
devpi upload
```
