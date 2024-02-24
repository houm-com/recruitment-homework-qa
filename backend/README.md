# visists-app-backend

Visits Backup App

# Before running the project (optional)

## Environment variables
Create a copy of the `.env.template` file and name it `.env`.

## Run project locally

Run the following instructions to create the app container and database and run the service to start playing with the API.

```bash
make clean-install
make run-service
```

## Useful commands
```bash
make clean-install
```
To run the service locally, you need to build the necessary docker containers for the database
and the api, the created database is populated with testing data. This can be done with the following commands using the Makefile:

Use the same command if you want to rebuild everything from scratch.
After building the containers, you can run the service with the following command:

```bash
make run-service
```
This will run the container and start the API server in your terminal

```bash
make run-terminal
```
This will leave your terminal inside the container where you can run the `dev` custom command.
You can use this command to run the server manually, format code, trying new packages, etc.

```bash
make run-tests
```
Runs tests in the tests/ directory using pytest

```bash
make build-clean-database
```
Use this command if you only want to restart the database to its initial state with test data. This doesn't rebuild the docker image.


## API definition
Run the service and visit http://localhost:8000/docs