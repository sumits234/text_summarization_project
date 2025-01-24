# Text Summarization Project

This project implements a **Text Summarization System** using state-of-the-art transformer models. The goal is to automatically generate concise, coherent summaries from large input texts, preserving semantic meaning while reducing length.

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Project Description

This project uses **Hugging Face Transformers** and **PyTorch** to implement an abstractive text summarization model, specifically leveraging transformer architectures .The model is trained on a large corpus and fine-tuned to summarize input texts effectively.

- **Input**: Long documents or articles.
- **Output**: Concise summaries with high semantic accuracy.

The model performance is evaluated using **ROUGE-L** and **BLEU** scores to assess the quality of the generated summaries.

## Technologies Used

- **Programming Languages**: Python  
- **Libraries/Frameworks**: Hugging Face Transformers, NLTK, spaCy, PyTorch  
- **Package Management**: Conda  
- **CI/CD**: GitHub Actions  
- **Deployment**: AWS  
- **Evaluation Metrics**: ROUGE, BLEU  
- **Development Tools**: Jupyter Notebook, Google Colab, GitHub

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sumits234/text_summarization_project.git
   cd text_summarization_project
