# Cold Email Generator

An AI-powered application that automatically generates personalized cold emails for job postings by analyzing job descriptions and matching them with relevant portfolio projects.

## Overview

This tool helps business development professionals quickly create tailored cold emails by:
- Scraping job posting URLs to extract job requirements
- Analyzing required skills and experience
- Matching job requirements with relevant portfolio projects
- Generating personalized cold emails with appropriate portfolio links

## Features

- **Web Scraping**: Extracts job details from any job posting URL
- **AI-Powered Analysis**: Uses LLaMA 3.1 to parse job requirements and generate emails
- **Portfolio Matching**: Automatically finds relevant portfolio projects using vector similarity search
- **Clean UI**: Simple Streamlit interface for easy interaction

## Tech Stack

- **Frontend**: Streamlit
- **LLM**: LLaMA 3.1 (via Groq API)
- **Framework**: LangChain
- **Vector Database**: ChromaDB
- **Web Scraping**: LangChain WebBaseLoader

## Prerequisites

- Python 3.8+
- Groq API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

2. Install required packages:
```bash
pip install streamlit langchain-community langchain-groq langchain-core chromadb python-dotenv
```

3. Create a `.env` file in the root directory and add your Groq API key:
```
Groq_API_Key=your_groq_api_key_here
```

4. Create a `sample_portfolio.csv` file with your portfolio data:
```csv
Skill1,Skill2,Skill3,Portfolio_URL
Python,Machine Learning,TensorFlow,https://example.com/project1
React,JavaScript,Node.js,https://example.com/project2
```

## Project Structure

```
cold-email-generator/
├── main.py              # Streamlit app entry point
├── chain.py             # LLM chain logic for job extraction and email generation
├── portfolio.py         # Portfolio management and vector search
├── utils.py             # Text cleaning utilities
├── sample_portfolio.csv # Portfolio data
├── .env                 # Environment variables (not tracked in git)
└── vectorstore2/        # ChromaDB persistence directory
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. Enter a job posting URL in the text input field

3. Click "Submit" to generate cold emails

4. The app will:
   - Scrape and clean the job posting
   - Extract job requirements
   - Find matching portfolio projects
   - Generate personalized cold emails

## How It Works

1. **Web Scraping**: The app uses `WebBaseLoader` to fetch content from the provided URL
2. **Text Cleaning**: Removes HTML tags, URLs, and special characters
3. **Job Extraction**: LLM parses the cleaned text to extract role, experience, skills, and description
4. **Portfolio Matching**: ChromaDB finds the most relevant portfolio projects based on required skills
5. **Email Generation**: LLM creates a personalized cold email incorporating the matched portfolio links

## Configuration

You can customize the email generation by modifying the prompt templates in `chain.py`:

- **Company Name**: Change "Mentee Consulting" to your company name
- **Company Focus**: Update the company description in the email prompt
- **Email Tone**: Adjust the prompt to change the writing style

## Example Output

The generated emails follow this structure:
- Professional greeting
- Hook mentioning the specific job role
- Brief company introduction
- Relevant portfolio examples
- Call to action

## Limitations

- Requires valid Groq API key
- Limited to 1000 tokens per LLM response
- Depends on job posting structure for accurate extraction
- Portfolio matching quality depends on skill descriptions

## Future Enhancements

- [ ] Support for multiple job postings at once
- [ ] Email template customization via UI
- [ ] Export emails to various formats
- [ ] Integration with email clients
- [ ] Support for additional LLM providers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- LangChain for the LLM framework
- Groq for providing fast LLM inference
- Streamlit for the web interface

## Contact

Hassan - [Your Contact Information]

Project Link: [https://github.com/yourusername/cold-email-generator](https://github.com/yourusername/cold-email-generator)
