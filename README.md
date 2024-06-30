# Water Quality Prediction and Aquatic Life Sustainability

## Project Overview

This project aims to predict the quality of water samples and determine whether they are fit to sustain aquatic life. The solution utilizes machine learning techniques and is built using Python, Flask, HTML, and integrates a chatbot for enhanced user interaction.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [API Endpoints](#api-endpoints)
- [Chatbot Integration](#chatbot-integration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DevaduttM/Aqua_AI.git
    cd Aqua_AI
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to access the web application.

3. **Interact with the Chatbot** to predict water quality and determine its suitability for sustaining aquatic life.

## Model Training

The model training is done using the `AquaAI.py` script. This script reads the dataset, preprocesses it, and trains a Logistic Regression model to predict water quality.

**Steps to train the model**:

1. Ensure you have the dataset in the `data/` directory.
2. Run the `AquaAI.py` script:
    ```bash
    python AquaAI.py
    ```
3. The trained model will be saved as a `.pkl` file in the root directory.

## API Endpoints

The Flask application provides the following API endpoints:

- **GET /**: Render the home page.
- **POST /predict**: Predict the water quality based on user input.

## Chatbot Integration

The chatbot is integrated to provide an interactive user experience. It can answer questions related to water quality and predict the sustainability of aquatic life based on user inputs.

To interact with the chatbot:

1. **Open the web application** in your browser.
2. **Type your queries** in the chatbot interface.
3. **Receive real-time responses** from the chatbot.

## Contributing

We welcome contributions to this project. To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Open a pull request**.

---

For any questions or issues, please open an issue on GitHub or contact the project maintainers. Happy coding!
