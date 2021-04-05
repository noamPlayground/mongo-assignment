# mongo-assignment

## Prior requirements
- Please make sure to have Docker Engine and Docker Compose installed in order to start the application.

This repository includes a simple Python 3 application that inserts data to a new MongoDB database and collection, manipulates the data, and displays it in a webpage using the Flask web framework.

### Instructions:

When in the project's root directory, simply run:

$ docker-compose up

docker-compose will provision a MongoDB server and the Python application.
When the application is running, a web page containing details from the newly created MongoDB collection is available at http://127.0.0.1:5000/.


### Notes:
- Application code is in the '/src' folder.
- MongoDB collection data is in the '/mongo' folder.
- Dockerfile builds the Python application
- requirements.txt includes dependencies for the Python application to run.
- docker-composel.yml defines the Python application container, and MongoDB container that will be applied using Docker Compose.
- After running the application via Docker Compose, DB collection data will be available in the host machine machine at '/exportData/users.json'.
- The Python application can also be downloaded from Docker Hub at noamozer/mongo-assignment-app, but it is recommended to use Docker Compose in order to create the MongoDB along with the Python application.
- The app uses the default MongoDB port of 27017.
