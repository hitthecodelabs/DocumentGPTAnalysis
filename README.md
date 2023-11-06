# DocumentGPTAnalysis

## Project Overview

Welcome to the DocumentGPTAnalysis! This web application is designed to provide an intuitive interface for users to upload text files from their local system. Our backend, built on Flask (a Python web framework), reads the uploaded files and extracts the contents. These contents are then processed by a powerful language model API, including GPT-3.5 Turbo and GPT-4, to analyze the text and answer specific questions posed by the user.

The app is an amalgamation of modern web technologies and cutting-edge AI to offer a seamless experience for text analysis. With VueJS crafting the responsive frontend and Flask serving as the robust backend, we aim to deliver an efficient and user-friendly platform that leverages the capabilities of ChatGPT's API to perform deep language understanding and generate insightful responses.

## Features

- **File Upload System**: Users can easily upload text files from their local machine for analysis.
- **Text Analysis**: Uploaded content is processed by the backend which interacts with OpenAI's language models.
- **Question & Answering**: The application responds to user questions by analyzing the text content using ChatGPT's API, capable of insightful and context-aware answers.
- **GPT-3.5 Turbo and GPT-4 Integration**: Utilizes the latest GPT models for superior language processing.

## Technical Details

- **Backend**: The server-side is powered by Flask, which handles file uploads and communicates with the ChatGPT API for processing natural language.
- **Frontend**: VueJS provides a dynamic and interactive user experience, facilitating file uploads and displaying the analysis results.
- **Language Model API**: Our application makes use of the ChatGPT API, tapping into the potential of models like GPT-3.5 Turbo and GPT-4 for analyzing and responding to text.
- **Security**: Measures are in place to ensure that user data is handled securely and responsibly.

## Getting Started

To get the app up and running on your local environment, follow these steps:

### Prerequisites

- Python 3.x
- Node.js and npm
- An OpenAI API key with access to GPT-3.5 Turbo and GPT-4

### Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/hitthecodelabs/DocumentGPTAnalysis.git

    cd DocumentGPTAnalysis
    ```
2. Navigate to the cloned directory and install the Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Install VueJS dependencies:
    ```sh
    cd frontend
    npm install
    ```
4. Enter your OpenAI API key in the `.env` file in the root directory:
    ```env
    OPENAI_API_KEY='your-api-key-here'
    ```

### Running the Application

1. Start the Flask server:
    ```sh
    python app.py
    ```
2. Run the VueJS development server:
    ```sh
    npm run serve
    ```
3. Open your web browser and navigate to `http://localhost:8080` to view the app.

## Usage

1. Use the web interface to upload a text file.
2. Enter the questions you want the app to answer based on the text.
3. Submit your questions and receive answers powered by GPT-3.5 Turbo or GPT-4.

## Contributions

Contributions to this project are welcome! Please follow the standard GitHub pull request process to propose changes.

## License

This project is open-source and available under the [MIT License](LICENSE.md).

## Acknowledgements

- Flask for the simple yet powerful web server framework.
- VueJS for the progressive frontend framework that makes web development enjoyable.
- OpenAI for providing the advanced language model APIs.

Thank you for considering the DocumentGPTAnalysis for your text analysis needs. We are eager to see how you utilize this tool to unlock new insights and understandings from your text data!
