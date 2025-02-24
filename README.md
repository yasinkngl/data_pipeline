# Data Pipeline Project

This project implements a robust data collection and processing pipeline using Python, Docker, and Apache Airflow. The pipeline fetches data from an external API, cleans and transforms it, and then inserts the processed data into external PostgreSQL and MongoDB databases. The entire workflow is orchestrated by an Apache Airflow DAG.

## Project Structure

root/ 
├── airflow/ │
    ├── dags/ │
        └──│ data_pipeline_dag.py │ 
    ├── logs/ │
    └──  plugins/ 
├── src/ │ 
    ├── data_ingestion.py │ 
    ├── data_cleaning.py │ 
    └── db_integration.py 
├── tests/ │ 
    └── test_data_cleaning.py 
├── Dockerfile 
├── docker-compose.yml # External databases: PostgreSQL & MongoDB 
├── airflow-compose.yml # Airflow services (scheduler, webserver, metadata DB) 
└── README.md

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (ensure it’s running)
- [Git](https://git-scm.com/downloads)
- Basic familiarity with Docker, Docker Compose, and Apache Airflow

## Getting Started

1. Clone the Repository

    bash:
    git clone <repository_url>
    cd data_pipeline

2. (Optional) Set Up a Python Virtual Environment
 If you prefer to run tests or scripts locally:

 bash:
 python -m venv venv

 On Linux/macOS:
 source venv/bin/activate
 On Windows:
 venv\Scripts\activate

 pip install -r requirements.txt

3. Build and Test the Docker Image

 The provided Dockerfile builds an image that runs unit tests by default:

 bash:
 docker build -t data_pipeline .
 docker run --rm data_pipeline

4. Start the Environment

 You have two Docker Compose files:

 airflow-compose.yml: Starts the Airflow services (scheduler, webserver, and its metadata PostgreSQL).
 docker-compose.yml: Starts external PostgreSQL and MongoDB containers for your pipeline data.
 You can run these separately or merge them for a unified setup.

 Option A: Run Separately

 Start External Databases:

 bash:
 docker-compose up -d

 Start Airflow Services:
 bash:
 docker-compose -f airflow-compose.yml up -d

 Option B: Merged Compose File (recommended)

 If you merged the two files into one, simply run:

 bash:
 docker-compose up -d

5. Access and Use Airflow
 Open your browser and go to http://localhost:8080.
 In the Airflow UI, you’ll see the DAG named data_pipeline_dag which:
 Fetches raw data from an external API.
 Cleans and transforms the data.
 Inserts the cleaned data into external PostgreSQL and MongoDB databases.
 Trigger the DAG:
 Manually trigger the DAG to run immediately (useful during development).
 Monitor the DAG:
 Check task logs and XComs (via Admin > XComs) to verify data flow and debug issues.
6. Verify Data in External Databases

 PostgreSQL

 Using a Client:

 Connect with pgAdmin, DBeaver, or the psql CLI.
 Example Query:
 SELECT * FROM books;

 MongoDB

 Using MongoDB Compass or Shell:

 Example Shell Commands:

 bash:
 mongo --port 27017
 use mydb
 db.books.find().pretty()

 Data Pipeline Overview

 Data Ingestion:
 The DAG’s fetch_data_task calls fetch_data() from src/data_ingestion.py to retrieve data from the external API.
 Data Cleaning:
 The clean_data_task calls clean_data() from src/data_cleaning.py to process the raw data.
 Data Insertion:
 The cleaned data is then inserted into:
 PostgreSQL via insert_into_postgres() from src/db_integration.py.
 MongoDB via insert_into_mongodb() from src/db_integration.py.

 Customization
 
 Connection Strings:
 Adjust connection strings in src/db_integration.py if necessary. When running in Docker, use service names (e.g., postgres) or host.docker.internal to connect to host-based databases.
 Debugging:
 Use task logs and, if needed, add a debug task to print sample data from XComs to verify data integrity.

 Contributing

 Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.

License
This project is licensed under the MIT License.