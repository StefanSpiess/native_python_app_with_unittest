# Unit Testing Project

This project is a Python-based repository designed to demonstrate and test various functionalities using unit testing. It includes multiple modules, each focusing on specific tasks, and is containerized using Docker for ease of deployment and testing.

## Project Structure

### Modules

1. **`unittesting_efficiency.py`**
   - Contains the `FibonacciSequence` class with two methods to compute Fibonacci numbers:
     - `recursive_method`: Uses recursion to calculate Fibonacci numbers.
     - `math_method`: Uses a mathematical formula for computation.

2. **`unittesting_counter.py`**
   - Provides a `count_letters` function to count the number of letters in a string, excluding spaces and non-alphabetical characters.

3. **`unittesting_console_output.py`**
   - Defines a `Profile` class with attributes (`age`, `job`, `name`) and methods to print these attributes.

4. **`unittesting_classes.py`**
   - Contains a `Counter` class to increment, decrement, reset, and retrieve a numerical value.

5. **`unittesting_car_class.py`**
   - Implements a `Car` class with attributes like `speed`, `passengers`, and methods to manage car operations such as turning on/off, adding/subtracting passengers, and adjusting speed.

6. **`unittesting_base.py`**
   - Provides a utility function `str_to_uppercase` to convert a string to uppercase.

7. **`unittesting_average.py`**
   - Contains a `calculate_average` function to compute the average of a list of integers or floats.

### Configuration Files

- **`requirements.txt`**: Lists Python dependencies required for the project.
- **`Dockerfile`**: Defines the containerization setup for the project.
- **`docker-compose.yml`**: Configures the Docker Compose setup for building and running the project.
- **`docker-compose.debug.yml`**: Adds debugging capabilities to the Docker Compose setup.
- **`.vscode/tasks.json`**: Contains VS Code tasks for building and running the Docker container.
- **`.vscode/settings.json`**: Configures Python testing settings for the project.

### Ignore Files

- **`.gitignore`**: Specifies files and directories to exclude from version control.
- **`.dockerignore`**: Specifies files and directories to exclude from the Docker build context.

## Getting Started

### Prerequisites

- Python 3.x
- Docker and Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd unittesting_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. **Using Docker**:
   - Build and run the container:
     ```bash
     docker-compose up --build
     ```

2. **Debugging with Docker**:
   - Use the debug configuration:
     ```bash
     docker-compose -f docker-compose.debug.yml up --build
     ```

3. **Running Locally**:
   - Execute individual Python scripts or run tests using:
     ```bash
     python <script_name>.py
     ```

### Testing

- The project uses `unittest` for testing. To run the tests:
  ```bash
  python -m unittest discover -s ./tests -p "*_test.py"
  ```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Special thanks to the developers and maintainers of the libraries used in this project.
- Inspired by the need for efficient and modular unit testing practices.

