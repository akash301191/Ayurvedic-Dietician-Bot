import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat

def render_sidebar():
    st.sidebar.title("🔐 API Configuration")
    st.sidebar.markdown("---")

    # OpenAI API Key input
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        st.sidebar.success("✅ OpenAI API key updated!")

    st.sidebar.markdown("---")

def render_prakriti_inputs():
    st.markdown("---")

    # First row: 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🧬 Body & Basics")
        body_frame = st.selectbox("1. What best describes your body frame?", [
            "Thin, light, or underweight",
            "Medium, athletic, muscular",
            "Broad, heavy-set, gains weight easily"
        ])
        appetite = st.selectbox("2. How is your appetite?", [
            "Irregular, varies a lot",
            "Strong and sharp; gets irritable when hungry",
            "Slow, consistent, may skip meals"
        ])
        climate_preference = st.selectbox("3. How do you feel about the weather?", [
            "Dislike cold and wind",
            "Dislike heat and sun",
            "Dislike damp, humid weather"
        ])

    with col2:
        st.subheader("🔥 Skin, Hair & Eyes")
        skin_type = st.selectbox("4. Your skin is usually…", [
            "Dry, rough, flaky",
            "Warm, oily, prone to acne or rashes",
            "Cool, smooth, moist, thick"
        ])
        hair_type = st.selectbox("5. Your hair is…", [
            "Dry, brittle, frizzy",
            "Fine, silky, early graying or thinning",
            "Thick, oily, lustrous"
        ])
        eye_description = st.selectbox("6. How would you describe your eyes?", [
            "Small, dry, quick-moving",
            "Sharp, intense, reddish",
            "Large, calm, moist"
        ])

    with col3:
        st.subheader("💭 Mind & Emotions")
        memory = st.selectbox("7. How is your memory?", [
            "Quick to learn, quick to forget",
            "Sharp, focused, intense",
            "Slow to learn but good long-term memory"
        ])
        mood = st.selectbox("8. How would you describe your mood?", [
            "Anxious, restless, mood fluctuates easily",
            "Irritable, intense, quick to anger",
            "Calm, patient, rarely upset"
        ])
        stress_response = st.selectbox("9. How do you respond to stress?", [
            "Panic, worry, become overwhelmed",
            "Get angry, frustrated, try to control it",
            "Withdraw, procrastinate, emotionally shut down"
        ])

    # Second row: 2 columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛌 Sleep & Energy")
        sleep_pattern = st.selectbox("10. Your sleep is…", [
            "Light, interrupted, often with dreams",
            "Moderate, can wake with sharp dreams",
            "Deep, heavy, love to sleep in"
        ])
        energy_level = st.selectbox("11. How’s your daily energy level?", [
            "Bursts of energy but tires quickly",
            "Steady, intense energy",
            "Slow to get started, but lasts all day"
        ])

    with col2:
        st.subheader("🗣️ Lifestyle Tendencies")
        speech_style = st.selectbox("12. How would you describe your speech?", [
            "Fast, scattered, talks a lot",
            "Direct, sharp, sometimes critical",
            "Slow, deliberate, soothing"
        ])
        routine_approach = st.selectbox("13. How do you handle routine?", [
            "Hate routines, love variety",
            "Prefer efficiency and goal-driven routines",
            "Prefer familiar comfort and routine"
        ])

    # Assemble formatted profile string
    prakriti_profile = f"""
        **🧬 Body & Basics**
        - Body Frame: {body_frame}
        - Appetite: {appetite}
        - Climate Preference: {climate_preference}

        **🔥 Skin, Hair & Eyes**
        - Skin Type: {skin_type}
        - Hair Type: {hair_type}
        - Eye Description: {eye_description}

        **💭 Mind & Emotions**
        - Memory: {memory}
        - Mood: {mood}
        - Stress Response: {stress_response}

        **🛌 Sleep & Energy**
        - Sleep Pattern: {sleep_pattern}
        - Energy Level: {energy_level}

        **🗣️ Lifestyle Tendencies**
        - Speech Style: {speech_style}
        - Routine Approach: {routine_approach}
        """

    return prakriti_profile

def generate_diet_plan(user_prakriti_profile):
    prakriti_analyzer = Agent(
        model=OpenAIChat(id="gpt-4o", api_key=st.session_state.openai_api_key),
        name="Prakriti Analyzer",
        role="Analyzes the user's Ayurvedic prakriti profile and generates a multi-paragraph narrative report identifying their dominant dosha(s).",
        description=(
            "You are an experienced Ayurvedic consultant. Your job is to analyze a user's prakriti profile and identify their dominant dosha or dosha combination."
        ),
        instructions=[
            "Carefully analyze the user's prakriti profile grouped into physical, emotional, and behavioral traits.",
            "Determine the user's dominant prakriti — one of the six valid types: Vata, Pitta, Kapha, Vata-Pitta, Vata-Kapha, or Pitta-Kapha.",
            "Write a multi-paragraph analysis starting with the header '## Prakriti Analysis' and a bold line indicating the constitution type, like:\n\n"
            "**Dominant Prakriti**: Vata-Pitta",
            "Follow this with 3–4 well-written narrative paragraphs:",
            "- The first should describe key physical characteristics and what they indicate.",
            "- The second should focus on mental and emotional tendencies.",
            "- The third should describe lifestyle, sleep, speech, and energy patterns.",
            "Use smooth natural language. Do not list traits. Do not include bullet points, headers, or per-trait dosha tags.",
            "Do not guess beyond the input. All insights must be based on the profile."
        ],
        markdown=True
    )

    prakriti_response = prakriti_analyzer.run(user_prakriti_profile)
    prakriti_analysis = prakriti_response.content 

    diet_recommender = Agent(
        model=OpenAIChat(id="gpt-4o", api_key=st.session_state.openai_api_key),
        name="Ayurvedic Dietician",
        role="Creates a detailed daily Ayurvedic diet plan based on the user's Prakriti analysis.",
        description=(
            "You are a certified Ayurvedic dietician. When given a Prakriti analysis, your job is to generate a "
            "comprehensive food and lifestyle plan that matches the user's constitution. The diet plan should help balance their unique "
            "dosha characteristics using Ayurvedic dietary principles."
        ),
        instructions=[
            "Read the user's full Prakriti analysis carefully to identify their dominant constitution type (e.g., Vata, Pitta, Kapha, Vata-Pitta, etc.).",
            "Then return a comprehensive Ayurvedic diet plan formatted exactly as follows:\n\n"
            "## Personalized Ayurvedic Diet Plan\n\n"
            "**For Constitution Type**: <Prakriti Type>\n\n"
            "### 🥗 Ideal Foods\n"
            "<A bulleted list of recommended food types suited to their dosha. Include grains, vegetables, fruits, oils, dairy, and spices.>\n\n"
            "### ❌ Foods to Avoid\n"
            "<A bulleted list of foods or categories that may aggravate the dosha or imbalance digestion.>\n\n"
            "### 🕒 Daily Meal Schedule\n"
            "**🌅 Early Morning (6:30–7:30 AM)**\n"
            "- Bullet point 1: What to drink or eat\n"
            "- Bullet point 2: Optional variation\n"
            "- Bullet point 3: (if needed)\n\n"
            "**🍵 Breakfast (7:30–8:30 AM)**\n"
            "- Bullet point 1: Main breakfast option\n"
            "- Bullet point 2: Add-on or variation\n"
            "- Bullet point 3: Optional beverage\n\n"
            "**🍲 Mid-Morning Snack (10:30–11:00 AM)**\n"
            "- Bullet point 1: Light snack\n"
            "- Bullet point 2: Herbal drink or fruit\n\n"
            "**🍛 Lunch (12:30–1:30 PM)**\n"
            "- Bullet point 1: Grain + dal combo\n"
            "- Bullet point 2: Cooked vegetables or chutney\n"
            "- Bullet point 3: Dessert or digestive add-on\n\n"
            "**🍵 Afternoon Drink (3:30–4:00 PM)**\n"
            "- Bullet point 1: Herbal tea or infusion\n"
            "- Bullet point 2: Optional spice mix or hydration\n\n"
            "**🥣 Dinner (6:30–7:30 PM)**\n"
            "- Bullet point 1: Light main dish\n"
            "- Bullet point 2: Steamed or soupy vegetable side\n"
            "- Bullet point 3: Gentle spice recommendation\n\n"
            "**🌙 Before Bed (9:00 PM)**\n"
            "- Bullet point 1: Warm milk or nutmeg drink\n"
            "- Bullet point 2: Optional calming herb blend\n\n"
            "### 🌱 Lifestyle & Eating Habits\n"
            "<Write 3–4 tips in paragraph form that align with the user's prakriti. Address things like meal timing, emotional state while eating, and seasonal tuning.>\n\n",
            "Ensure each meal section has 2–3 thoughtful bullet points. Avoid generic placeholders. Stay aligned with the user’s dosha."
        ],
        markdown=True
    )

    diet_response = diet_recommender.run(prakriti_analysis)
    diet_plan = diet_response.content

    final_report = f"""
{prakriti_analysis}

{diet_plan}
"""
    
    return final_report          

def main() -> None:
    # Page config
    st.set_page_config(page_title="Ayurvedic Dietician Bot", page_icon="🌿", layout="wide")

    # Custom styling
    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header and intro
    st.markdown("<h1 style='font-size: 2.5rem;'>🌿 Ayurvedic Dietician Bot</h1>", unsafe_allow_html=True)
    st.markdown(
        "Welcome to Ayurvedic Dietician Bot — a holistic Streamlit app that helps you identify your Prakriti and suggests a personalized diet plan rooted in ancient Ayurvedic wisdom.",
        unsafe_allow_html=True
    )

    render_sidebar()
    user_prakriti_profile = render_prakriti_inputs()

    st.markdown("---")

    # Button to trigger diet plan generation
    if st.button("🥗 Generate Ayurvedic Diet Plan"):
        if not hasattr(st.session_state, "openai_api_key"):
            st.error("Please provide your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Analyzing your prakriti and preparing your personalized diet plan..."):
                diet_plan = generate_diet_plan(user_prakriti_profile)
                st.session_state.diet_plan = diet_plan

    # Display and download option for generated diet plan
    if "diet_plan" in st.session_state:
        st.markdown(st.session_state.diet_plan, unsafe_allow_html=True)
        st.markdown("---")

        st.download_button(
            label="📥 Download Ayurvedic Diet Plan",
            data=st.session_state.diet_plan,
            file_name="ayurvedic_diet_plan.txt",
            mime="text/plain"
        )



if __name__ == "__main__":
    main()