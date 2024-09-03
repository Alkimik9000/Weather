☁️ Weather App Project 🌦️
Overview 🌍
Welcome to the Weather App project! This application is designed to provide current and future weather information for cities around the globe. Built with Python and Flask, this project showcases the use of APIs, Docker, Kubernetes, Helm charts, and Argo CD for continuous integration and continuous deployment (CI/CD).

Features ✨
Current Weather: Get real-time weather updates for any city 🏙️.
Future Weather: Check the weather forecast for any upcoming date 🌤️.
Dockerized Application: Easily deploy the app using Docker 🐳.
Kubernetes Deployment: Managed with Helm charts for scalable and reliable deployment 🚀.
CI/CD Pipeline: Automated with GitHub Actions and Argo CD for smooth deployment 🛠️.
Getting Started 🚀
Prerequisites 📋
Python 3.10: Ensure Python is installed on your machine.
Docker: Required for containerizing the application.
Kubernetes: A running Kubernetes cluster (Minikube is recommended for local development).
Helm: For managing Kubernetes applications.
Argo CD: For continuous deployment.
GitHub Actions: Set up for continuous integration.
Installation 🛠️
Clone the Repository:

bash
Copy code
git clone https://github.com/alkimik/weather-app.git
cd weather-app
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python weather_app.py
Access the Application: Open your browser and navigate to http://localhost:5001.

Deployment 🌐
Docker 🐳
To build and run the application in a Docker container:

bash
Copy code
docker build -t alkimik/weather-app:v2.0.1 .
docker run -p 5001:5001 alkimik/weather-app:v2.0.1
Kubernetes with Helm 🚀
Deploy with Helm:

bash
Copy code
helm install weather-app-release ./weather-app-chart --set image.repository=alkimik/weather-app --set image.tag=v2.0.1
Port Forwarding:

bash
Copy code
kubectl port-forward svc/weather-app-service -n default 8080:5001
Access the Application: Open your browser and navigate to http://localhost:8080.

CI/CD Pipeline ⚙️
The project uses GitHub Actions for CI and Argo CD for CD:

GitHub Actions: Automates the Docker image build and push to Docker Hub.
Argo CD: Syncs the changes and deploys the updated application version to your Kubernetes cluster.
Versioning 📌
Current Version: v2.0.1
We recommend using version tags for the Docker image and Helm chart to ensure consistency across deployments.
Contribution Guidelines 🤝
Feel free to fork this repository and contribute to improving the project. Submit a pull request with your changes, and ensure that all tests pass before merging.

License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments 🙌
Special thanks to the OpenWeatherMap API for providing the weather data.
Contact ✉️
For any inquiries, feel free to reach out to me at alkimik9000@example.com.

