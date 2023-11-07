# DocumentGPTAnalysis-GCF

## Project Overview

Welcome to the DocumentGPTAnalysis-GCF Edition! This specialized web application offers an intuitive platform for users to upload documents and automatically extract answers to the Green Climate Fund's (GCF) key compliance questions. Our backend, powered by Flask, is fine-tuned to process the text within uploaded documents using advanced AI models, including GPT-3.5 Turbo and GPT-4.

Leveraging VueJS for a responsive frontend and Flask for a secure backend, the application aims to streamline the GCF's compliance and documentation process. It stands as a nexus of web technology and artificial intelligence, designed specifically to dissect and respond to the stringent requirements of the GCF.

## Features

- **GCF-Specific File Analysis**: Tailored to address the GCF's first three compliance questions by analyzing user-uploaded documents.
- **Intelligent Text Extraction**: Processes documents to extract answers relevant to the GCF's compliance inquiries.
- **Automated Q&A for GCF Compliance**: Automatically analyzes the text and extracts information to answer predefined GCF-related questions.
- **GPT-3.5 Turbo and GPT-4 Integration**: Employs the most advanced language processing models available for nuanced and precise analysis.

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
4. Enter your OpenAI API key in the `app.py` file in the root directory:
    ```sh
    import openai
    
    openai.api_key='your-api-key-here'
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
