# Ayurvedic Dietician Bot

Ayurvedic Dietician Bot is a holistic Streamlit application that analyzes your mind-body constitution (Prakriti) and delivers a personalized Ayurvedic diet plan tailored to your unique dosha type. Powered by [Agno](https://github.com/agno-agi/agno) and OpenAI’s GPT-4o, this bot blends ancient Ayurvedic wisdom with modern AI to promote balance, vitality, and well-being through food.

## Folder Structure

```
Ayurvedic-Dietician-Bot/
├── ayurvedic-dietician-bot.py
├── README.md
└── requirements.txt
```

- **ayurvedic-dietician-bot.py**: The main Streamlit application.
- **requirements.txt**: Required Python packages.
- **README.md**: This documentation file.

## Features

- **Prakriti Assessment Input**  
  Answer a 13-question guided assessment covering body type, appetite, emotions, sleep, and more — all rooted in Ayurvedic profiling.

- **Dosha Analysis Agent**  
  The Prakriti Analyzer agent identifies your dominant dosha (Vata, Pitta, Kapha, or dual types) using a natural language explanation and Ayurvedic principles.

- **Comprehensive Diet Recommendation**  
  The Ayurvedic Dietician agent reads your prakriti analysis and generates a structured diet plan — including ideal foods, foods to avoid, and a full daily meal schedule from sunrise to bedtime.

- **Downloadable Wellness Plan**  
  You can download the full plan as a `.txt` file for reference, journaling, or sharing with a practitioner.

- **Streamlined UI with Streamlit**  
  A clean, responsive interface to help you explore your Ayurvedic constitution with ease and clarity.

## Prerequisites

- Python 3.11 or higher  
- An OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akash301191/Ayurvedic-Dietician-Bot.git
   cd Ayurvedic-Dietician-Bot
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the app**:
   ```bash
   streamlit run ayurvedic-dietician-bot.py
   ```

2. **In your browser**:
   - Enter your OpenAI API key in the sidebar.
   - Fill out the prakriti assessment form.
   - Click **🥗 Generate Ayurvedic Diet Plan**.
   - Review your personalized dosha analysis and full meal plan.

3. **Download Option**  
   Use the **📥 Download Ayurvedic Diet Plan** button to save your personalized report as a `.txt` file.

## Code Overview

- **`render_prakriti_inputs()`**: Captures the user's physical, emotional, and behavioral traits through a guided quiz.
- **`render_sidebar()`**: Manages OpenAI API key input via Streamlit session state.
- **`generate_diet_plan()`**:  
  - Uses the `Prakriti Analyzer` agent to classify the user's constitution based on profile inputs.  
  - Passes the result to the `Ayurvedic Dietician` agent to produce a detailed, dosha-aligned diet plan.
- **`main()`**: Controls app layout, user flow, analysis logic, and download generation.

## Contributions

Contributions are welcome! Fork the repo, suggest improvements, or open a pull request. Make sure your updates are aligned with the app’s purpose and thoroughly tested.