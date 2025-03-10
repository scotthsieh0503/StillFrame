# StillFrame

## Quick Start

1. Clone the repository:
    ```sh
    git clone https://github.com/scotthsieh0503/StillFrame.git
    ```
2. Navigate to the project directory:
    ```sh
    cd StillFrame
    ```
3. Run the installation script:
    ```sh
    ./install.sh
    ```
4. Start the application:
    ```sh
    ./start.sh
    ```

## Development Mode

To run the application in development mode, you can use Docker Compose to start both the Flask backend and the Next.js frontend.

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the project directory:
    ```sh
    cd StillFrame
    ```
3. Start the development environment:
    ```sh
    docker-compose up
    ```

This will start the Flask backend and the Next.js frontend, allowing you to develop and test the application locally.


## Building for RaspberryPI
To limit the need for RaspberryPI to build the JS dependencies, we re-compile the Next.js app and push it to the repository by running the following command:

```sh
npm run build
```

This will create an export of the Next.js app as static web pages.