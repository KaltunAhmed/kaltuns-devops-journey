# Flask Redis Counter Application

A simple Flask web application that counts visits using Redis as the backend.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Build and Run the Application:** Use Docker Compose to build and run the application:
    ```
    docker-compose up --build
    ```

3. **Access the Application:** Open your web browser and go to `http://localhost:5002` to view the application.

## Endpoints

- **Homepage**: `GET /` - Displays "Hello, World!"
- **Visit Count**: `GET /count` - Displays the number of visits to the homepage.


4. **To stop the application:**
    ` docker-compose down`


## To run locally 
1. **Install Redis:**
   - If you haven't installed Redis yet, use Homebrew
    ```bash
    brew install redis
    ```

2. **Start the Redis Server:**
   ```bash
   redis-server
   ```
3. Navigate to the directory containing the `app.py` file and install the Python packages:
    ```
    pip install redis Flask
    ```
4. **Start the app** 
    ```
    python app.py
    ```


