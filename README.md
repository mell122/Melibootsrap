# Project Name

Brief description or tagline for your project.

## Tools and Technologies Used

### Programming Languages:
- Python
- YAML

### API:
- Implemented both GET and POST methods for endpoint communication.

### Continuous Integration (CI):
- Docker: Built a Docker image for continuous integration.

### Continuous Deployment (CD):
- Kubernetes: Utilized Kubectl for continuous deployment.

### Automated Pipeline:
- Integrated all tools and technologies to create an automated pipeline.

### Other Tools:
- **Kind:** Kubernetes in Docker for local testing and development.
- **Webhooks:**
  - Webhook Handler
  - FastAPI

### Diagrams:
- Utilized Draw.io to create visual representations of the system architecture.

### Ngrok:
- Exposed a local server to the public internet using Ngrok for running webhooks.

## Second Project: Migration to AWS Cloud

- **Cloud Provider:** Amazon Web Services (AWS)
- **Infrastructure as Code (IaC):**
  - Terraform: Automated the infrastructure provisioning process.

## Getting Started

Provide instructions on how to set up the project locally or deploy it in a production environment.

## Usage

Explain how to use the project, including any configuration settings and examples.

## Contributing

If you'd like to contribute to the project, follow these guidelines.

## License

This project is licensed under the [LICENSE NAME] - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

Mention and thank any contributors, libraries, or resources that inspired or helped with the project.

## Contact

Provide your contact information for inquiries or feedback.

## test and run

# FastAPI Divisibility Checker

A simple FastAPI application that checks whether a given number is even or odd.

## Running the Application

1. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

2. Run the FastAPI application:

    ```bash
    uvicorn __main__:app --host 0.0.0.0 --port 5000 --reload
    ```

3. Open your web browser or use a tool like `curl` or Postman to access the divisibility checker:

    - Example URL: [http://127.0.0.1:5000/42](http://127.0.0.1:5000/42)
  
    Replace `42` with the desired number to check its divisibility.

4. Remember to avoid accessing paths like `/` or `/favicon.ico`, as they are not defined in the application.

## Additional Information

- The application defines a single route: `/{number}`, where `number` is an integer to check for divisibility.
- If you encounter a "404 Not Found" error, make sure you are accessing a valid route with a valid number in the URL.

Feel free to modify the documentation to better fit your project's structure and details.
