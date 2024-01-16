import streamlit as st
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

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
    .st-emotion-cache-1r4qj8v {
        color: #00A8E8; 
    }
    h1, h2, h3, a, .st-emotion-cache-nahz7x a {
        color: #00A8E8;  
    }
    .st-emotion-cache-nahz7x {
        color: #00A8E8; 
    }
    .st-emotion-cache-6qob1r {
        background-color: #003459
        
    }
    
    .stApp > header {
        background-color: #003459
    }
    .st-emotion-cache-1cypcdb {
        background-color: #003459
        color: #00A8E8
    }
    st-emotion-cache-1r4qj8v {
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
    st.header("Introduction", divider='rainbow')
    image = st.image("Home_Page/foodstuffs.jpg", use_column_width=True)
    st.markdown("""[Action Against Hunger](https://www.actionagainsthunger.org.uk/our-impact/stories/the-hungriest-countries-in-the-world), ranks Nigeria as one of the world's hungriest countries. Additionally, [UNICEF](https://www.unicef.org/press-releases/25-million-nigerians-high-risk-food-insecurity-2023),\n",
        25 million Nigerians are at high risk of food insecurity in 2023. High food insecurity is caused by factors such as high rate of food inflation, climate changes, high rates of poverty and unemployment.
        Rising food prices affects the livelihood of Nigerian citizens, directly impacting economic stability and well-being. This project aims to utilize Data science and Machine Learning (ML) techniques to analyze historical food price data in Nigeria, predict future price trends, and provide valuable insights for the benefit of consumers, policymakers, and relevant stakeholders.
        """)
    
    st.subheader('PROJECT BREAKDOWN', divider='rainbow')
    st.markdown("""
The project is broken down into 5 stages which include:
- Data Collection and Preprocessin
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Development & Evaluation
- Interactive Web Application
      """)
  
    st.header("Problem Statement", divider='rainbow')
    st.markdown("""
- The recent upsurge in food inflation has significantly impacted the livelihoods of Nigerians, with a particularly pronounced effect on those residing in crisis-affected regions. This added economic shock has disproportionately affected households that were already grappling with precarious living conditions.
- Government agencies, humanitarian groups, and development organizations consistently track inflation rates to detect concerning patterns and inform their strategies for assistance. Elevated inflation can result in a substantial uptick in essential household expenditures, necessitating a policy intervention. In severe instances, a spike in food costs can serve as an early warning sign of local food scarcity, indicating the onset or exacerbation of a food and nutrition crisis.
- However, during various crisis situations, especially in conflict-affected regions where food markets become inaccessible, the collection of detailed price data is often hindered. These disruptions tend to align with periods and locations characterized by significant price instability. The absence of such data creates challenges in accurately assessing price fluctuations, which is essential for gauging the gravity of conditions in these areas and formulating effective responses.
""")

    st.header("Objectives", divider='rainbow')
    st.markdown("""
The core aim of this project is to harness the potential of data and machine learning to forecast food prices in Nigeria. This predictive analysis serves as a valuable resource for consumers, policymakers, and stakeholders, empowering them to make informed, data-driven decisions. The specific objectives are:
- To Analyse historical food price data to identify trends, seasonality, and correlations.
- To Develop machine learning models to predict food prices for essential commodities.
- To Create an interactive web application to visualize the data for better insights.
- To create reports and give recommendations based on the findings.
""")



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
       {"name": "Rabiat Ibrahim", "image": "Home_Page/Rabiat_ibrahim.jpg", "bio": "Rabiat Ibrahim is a dedicated machine learning/data scientist with a strong background in mathematics and statistics and a knack for uncovering insights from complex datasets. Skilled in Python, Pytorch and machine learning/neural network, with several projects available on platforms like GitHub and Kaggle", "link": "https://www.linkedin.com/in/https://www.linkedin.com/in/rabiat-ibrahim-488716ab"},
       {"name": "Sandy Om'Iniabohs", "image": "Home_Page/sandy.jpg", "bio": "Sandy Om'Iniabohs is a data and research analyst with broad-based experience across agro-allied and IT industries. She is skilled in the use of Python, SQL, Power BI, Tableau and Spreadsheets as well as in data modelling, data visualisation and machine learning to perform data analysis and make predictions.", "link": "https://linkedin.com/sandyominiabohs"},
       {"name": "Juliet Sackey", "image": "Home_Page/Juliet_sackey.jpg", "bio": "Juliet Sackey is a data analyst with scientific training, good at analysing and interpreting complex data, deriving meaningful conclusions, and communicating findings to stakeholders", "link": "https://www.linkedin.com/in/juliet-sackey-phd-23676257"}, 
        {"name": "Temitayo Badewole", "image": "Home_Page/Temi.jpg", "bio": "Temitayo Badewole is a Data scientist and advocate for gender equity for underrepresented women, particularly Teen moms. She has vast experience in data science, modelling and software development.", "link": "https://www.linkedin.com/in/temitayo-badewole-1046a768"},
        
        # Add more authors as needed
    ]

    #Display authors in a 3 by 2 grid
    for i in range(0, len(Contributors_data), 2):
        col1, col2 = st.columns(2)
        
        # Column 1
        with col1:
            st.image(Contributors_data[i]["image"], width=200, caption=Contributors_data[i]["name"])
            st.write(Contributors_data[i]["bio"])
            st.markdown(f"[{Contributors_data[i]['name']}'s LinkedIn]({Contributors_data[i]['link']})")

        # Column 2
        with col2:
        # Check if there is a second author in the row
            if i + 1 < len(Contributors_data):
                st.image(Contributors_data[i + 1]["image"], width=200, caption=Contributors_data[i + 1]["name"])
                st.write(Contributors_data[i + 1]["bio"])
                st.markdown(f"[{Contributors_data[i + 1]['name']}'s LinkedIn]({Contributors_data[i + 1]['link']})")

    st.subheader("Mentor", divider='rainbow')
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.write('')

    with col2:
        st.image("Home_Page/Shungu_dhlamini.jpg", width=250, height = 250, caption='Shungu Dhlamini')

    with col3:
        st.write('')

# Charts Page
elif state.page == "Charts":
    df = pd.read_csv('Home_Page/food_price_dataset.csv')
    st.title("Food Prediction Model")

    # Page content 
    col1, col2, col3 =  st.columns(3)
    with col1:
        selected_year = st.selectbox('Select Year:', df['Year'].unique(), placeholder="Select a Year...")
    with col2:
        selected_state = st.selectbox('Select State:', df['states'].unique(), placeholder="Select a State...")
    with col3:
        selected_category = st.selectbox('Select Crop Type:', df['crops'].unique(), placeholder="Select a Crop...")
    # Filter the data based on user selection
    filtered_df = df[(df['Year'] == selected_year) & (df['crops'] == selected_category) & (df['states'] == selected_state)]

    # Dataset
    st.subheader("Filtered Data", divider='rainbow')
    col1, col2, col3 =  st.columns(3)
    with col1:
        st.write(f"Selected Year: {selected_year}")
    with col2:
        st.write(f"Selected State: {selected_state}")
    with col3:
        st.write(f"Selected Category: {selected_category}")  
    st.write(filtered_df)

    #selected_crop = st.selectbox('Select Crop Type:', df['crops'].unique())
    st.subheader("Cost of Crop per Kg accross the states (2017 to 2020)", divider='rainbow')
    selected_crop = st.selectbox('Select Crop Type:', df['crops'].unique())

    # Using Seaborn to create a bar plot
    #plt.figure(figsize=(10, 5))
    #gx = sns.barplot(data=df[df["crops"]==selected_crop], x='states', y='Price/Kg (Naira)')
    #gx.set_xticklabels(gx.get_xticklabels(), rotation=90)

    #USING st.bar_chart
    st.bar_chart(data=df[df["crops"]==selected_crop], x='states', y='Price/Kg (Naira)', color="#177245", width= 150, height=500, use_container_width=True)
    
    # Display the plot using st.pyplot()
    #st.pyplot(plt)

# Feedback Page
elif state.page == "Feedback":
    st.title("Food Prediction Model")

    # Page content
    st.header("Feedback Form", divider='rainbow')

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
