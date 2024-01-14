import streamlit as st

# Set Page Configuration for a Wider Layout
st.set_page_config(layout="wide")

# Custom CSS
st.markdown("""
<style>
    .css-z5fcl4 {
    padding: 2rem 3rem 1rem 3rem;
    }
    .css-otxysd{
        display: none;
    }
    .css-1oe5cao {
        max-height: 100vh;
    }
    .css-74h3l2{
        display: block;
    }
    .stApp {
        background-color: #003459;
        color: #00A8E8;
    }
    h1, h2, a, .st-emotion-cache-nahz7x a {
        color: #FFFFFF; 
    }

    .st-emotion-cache-nahz7x {
        color: #00A8E8; 
    }
    .stApp > header {
        background-color: #003459
    }

    .st-emotion-cache-1cypcdb {
        background-color: #003459
    }
    
</style>
""", unsafe_allow_html=True)


# Create a session state to manage page navigation
class SessionState:
    def __init__(self):
        self.page = "Introduction"  # Initial page

# Initialize session state
state = SessionState()


# Sidebar for page Navigation -labels the sidebar menu
with st.sidebar:
    st.title("Menus")
    pages = ["Introduction", "Contributors", "Charts", "Prediction", "Feedback"]
    selected_page = st.sidebar.radio("Go to:", pages)

# Update page in the session state
state.page = selected_page

# Introduction Page
if state.page == "Introduction":
    st.title("Food Prediction Model")
    st.markdown("---")# Horizontal Line below the title

 # Page content
    st.header("Introduction")
    image = st.image("Home_Page/foodstuffs.jpg", use_column_width=True)
    st.markdown("""[Action Against Hunger](https://www.actionagainsthunger.org.uk/our-impact/stories/the-hungriest-countries-in-the-world), ranks Nigeria as one of the world's hungriest countries. Additionally, [UNICEF](https://www.unicef.org/press-releases/25-million-nigerians-high-risk-food-insecurity-2023),\n",
        25 million Nigerians are at high risk of food insecurity in 2023. High food insecurity is caused by factors such as high rate of food inflation, climate changes, high rates of poverty and unemployment.
        Rising food prices affects the livelihood of Nigerian citizens, directly impacting economic stability and well-being. This project aims to utilize Data science and Machine Learning (ML) techniques to analyze historical food price data in Nigeria, predict future price trends, and provide valuable insights for the benefit of consumers, policymakers, and relevant stakeholders.\n",
        
        "**PROJECT BREAKDOWN**\n",
        "The project is broken down into 5 stages which include:\n",
        "- Data Collection and Preprocessing\n",
        "- Exploratory Data Analysis (EDA)\n",
        "- Feature Engineering,
        "- Model Development & Evaluation,
        "- Interactive Web Application"
      """)
  
    st.header("Problem Statement")
    st.markdown("""
- The recent upsurge in food inflation has significantly impacted the livelihoods of Nigerians, with a particularly pronounced effect on those residing in crisis-affected regions. This added economic shock has disproportionately affected households that were already grappling with precarious living conditions.
- Government agencies, humanitarian groups, and development organizations consistently track inflation rates to detect concerning patterns and inform their strategies for assistance. Elevated inflation can result in a substantial uptick in essential household expenditures, necessitating a policy intervention. In severe instances, a spike in food costs can serve as an early warning sign of local food scarcity, indicating the onset or exacerbation of a food and nutrition crisis.
- However, during various crisis situations, especially in conflict-affected regions where food markets become inaccessible, the collection of detailed price data is often hindered. These disruptions tend to align with periods and locations characterized by significant price instability. The absence of such data creates challenges in accurately assessing price fluctuations, which is essential for gauging the gravity of conditions in these areas and formulating effective responses.
""")

    st.header("Objectives")
    st.markdown("""
The core aim of this project is to harness the potential of data and machine learning to forecast food prices in Nigeria. This predictive analysis serves as a valuable resource for consumers, policymakers, and stakeholders, empowering them to make informed, data-driven decisions. The specific objectives are:
- To Analyse historical food price data to identify trends, seasonality, and correlations.
- To Develop machine learning models to predict food prices for essential commodities.
- To Create an interactive web application to visualize the data for better insights.
- To create reports and give recommendations based on the findings.
""")


    #Project Overview
#st.markdown("""
    #<style>
       # h3{
       #     margin-left: 50px;
       # }
       # p{
        #    margin-left: 50px;
       #     text-align: justify;
      #  }
    #</style>
  # <h3>Overview of the Project</h3>
    #<p>Food prices hold significant influence over the lives of people globally, impacting factors such as affordability, food security, and economic stability. This project leverages Machine Learning (ML) techniques and Python programming to analyze historical food prices data in Nigeria, predict future prices, and offer valuable insights for consumers, policymakers, and stakeholders.</p>
     #""", unsafe_allow_html=True)



# Footer
#st.markdown("---")


#state.page = selected_page

# Contributors Page
elif state.page == "Contributors":
    st.title("Contributors Profiles")
    st.markdown("---")# Horizontal Line below the title

    #images = ['Rabiat_ibrahim.jpg', 'Rabiat_ibrahim.jpg']
    #st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
    #Contributors
    Contributors_data = [
       {"name": "Rabiat Ibrahim", "image": "Home_Page/Rabiat_ibrahim.jpg", "bio": "Bio of Author 1", "link": "https://www.linkedin.com/in/https://www.linkedin.com/in/rabiat-ibrahim-488716ab"},
       #{"name": "Sandy Om'Iniabohs", "image": "url_to_image_2", "bio": "Bio of Author 2", "link": "https://linkedin.com/sandyominiabohs"},
       {"name": "Juliet Sackey", "image": "Home_Page/Juliet_sackey.jpg", "bio": "Juliet Sackey is a data analyst with scientific training, good at analysing and interpreting complex data, deriving meaningful conclusions, and communicating findings to stakeholders", "link": "https://www.linkedin.com/in/juliet-sackey-phd-23676257"},
        
        # Add more authors as needed
    ]

    #Display authors in a 3 by 2 grid
    for i in range(0, len(Contributors_data), 2):
        col1, col2 = st.columns(2)
        
        # Column 1
        with col1:
            st.image(Contributors_data[i]["image"], width=150, caption=Contributors_data[i]["name"])
            st.write(Contributors_data[i]["bio"])
            st.markdown(f"[{Contributors_data[i]['name']}'s LinkedIn]({Contributors_data[i]['link']})")

        # Column 2
        with col2:
        # Check if there is a second author in the row
            if i + 1 < len(Contributors_data):
                st.image(Contributors_data[i + 1]["image"], width=150, caption=Contributors_data[i + 1]["name"])
                st.write(Contributors_data[i + 1]["bio"])
                st.markdown(f"[{Contributors_data[i + 1]['name']}'s LinkedIn]({Contributors_data[i + 1]['link']})")


# Charts Page
elif state.page == "Charts":
    df = pd.read_csv('Home_Page\preprocessed_data.csv')
    st.title("Food Prediction Model")

    # Page content 
    col1, col2, col3 =  st.columns(3)
    with col1:
        selected_year = st.selectbox('Select Year:', df['year'].unique())
    with col2:
        selected_category = st.selectbox('Select State:', df['State'].unique())
    with col3:
        selected_category = st.selectbox('Select Category Type:', df['category'].unique())
    # Filter the data based on user selection
    filtered_df = df[(df['year'] == selected_year) & (df['category'] == selected_category)]

    # Dataset
    st.subheader("Filtered Data")
    col1, col2, col3 =  st.columns(3)
    with col1:
        st.write(f"Selected Year: {selected_year}")
    with col2:
        st.write(f"Selected State: {selected_state}")
    with col3:
        st.write(f"Selected Category: {selected_category}")  
    st.write(filtered_df)



# Feedback Page
elif state.page == "Feedback":
    st.title("Food Prediction Model")

    # Page content
    st.header("Feedback Form")

    # Feedback form
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    feedback = st.text_area("Feedback:")
    submit_button = st.button("Submit Feedback")

    # Handle feedback submission
    if submit_button:
        # Save feedback to CSV file
        feedback_df = pd.DataFrame({'Name': [name], 'Email': [email], 'Feedback': [feedback]})
        feedback_df.to_csv('feedback.csv', mode='a', index=False, header=not pd.read_csv('feedback.csv').exists())

        st.success("Feedback submitted successfully!")

    st.header("Repository Link")
    st.write("Add your repository link here.")
