# Listing visit board

This template provides a simple web application to list visits. It is a simple web application that uses a backend API to list visits.

## Good to know
this project uses [Vite](https://vitejs.dev/) as a frontend build tool, it is a build tool that aims to provide a faster and leaner development experience for modern web projects. In a practical sense, you don't need to worry about vite, it is already configured for you, but if you want to know more about it, you can visit the [Vite documentation](https://vitejs.dev/guide/)

## Pre-requisites
This project requires the following software to be installed in your machine:
* Node.js (we use npm to manage the frontend dependencies) [Node.js installation](https://nodejs.org/en/download/)
* NPM (Node.js package manager) [NPM installation](https://www.npmjs.com/get-npm) or alternatively you can use Yarn or PNPM

## Run project locally

Before running the project, you need to install the dependencies. You can do this by running the following command in the terminal:

```bash
npm install
```

After installing the dependencies, you can run the project with the following command:

```bash
npm run dev
```
this will start the server and open the web application in your default browser at http://localhost:5173/

## Other Useful commands

| script | description |
| ------ | ----------- |
| `npm run test:unit ` | Runs the unit tests for the project using Jest in watch mode |
| `npm run test:e2e ` | Runs the end-to-end tests for the project using Cypress |
| `npm run test:lint ` | Check linter rules with eslint |
| `npm run test:types ` | Check typescript errors |
| `npm run build ` | Build the project for production |
| `npm run preview` | Runs the build version of the project |  