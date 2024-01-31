
import streamlit as st
import numpy as np
import pandas as pd
import pickle

#import sckit-learn
#import plotly as px
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
    pages = ["Introduction", "Contributors", "Charts", "Predictions", "Feedback"]
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
        25 million Nigerians are at high risk of food insecurity in 2023. High food insecurity is caused by factors such as high rates of food inflation, climate changes, high rates of poverty, and unemployment.
        Rising food prices affect the livelihood of Nigerian citizens, directly impacting economic stability and well-being. This project aims to utilize Data Science and Machine Learning (ML) techniques to analyze historical food price data in Nigeria, predict future price trends, and provide valuable insights for the benefit of consumers, policymakers, and relevant stakeholders.
        """)
    
    st.subheader('PROJECT BREAKDOWN', divider='rainbow')
    st.markdown("""
The project is broken down into 5 stages which include:
- Data Collection and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Development & Evaluation
- Interactive Web Application
      """)
  
    st.header("Problem Statement", divider='rainbow')
    st.markdown("""Agriculture serves as the primary economic pillar for a considerable number of households in Nigeria, engaging over 60% of the country's entire workforce. The daily sustenance of every household in Nigeria depends on agricultural food products like rice, beans, tomatoes, yams, and so on. Over the years, the price of these products has continuously increased and this is affected by several factors among which climatic factors such as rainfall and economic factors such as inflation. All through the farming cycle from the cultivation to the supply chain, the farmers have to endure several challenges such as insecurity, finance, postharvest loss, lack of storage facility, etc. 

For a sustainable agriculture practice, farmers and stakeholders need to make informed decisions regarding the sale of agricultural products. There is a need to have real-time information on the trending prices of food products across the country and how this information can be used to properly fix prices on their current product. The stakeholders such as wholesalers and retailers can also leverage such information while preparing their business budgets and plans.  The goal of this project is to provide farmers and stakeholders with a toolkit that enables them to make data-driven decisions on when, where, and how to sell their produce to maximize profit.
""")

    st.header("Objectives", divider='rainbow')
    st.markdown("""
- **Develop a Predictive Model**: Build a robust machine learning model that forecasts food prices in Nigeria based on historical data.
- **Improve Decision-Making**: Empower consumers, policymakers, and stakeholders with timely and accurate information to enhance decision-making related to food security and economic planning.
- **Mitigate Food Insecurity**: Contribute to efforts in mitigating food insecurity by providing insights that can assist in the development of effective policies and interventions.
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
       {"name": "Rabiat Ibrahim", "image": "Home_Page/Rabiat_ibrahim.jpg", "bio": "Rabiat Ibrahim is a dedicated machine learning/data scientist with a strong background in mathematics and statistics and a knack for uncovering insights from complex datasets. Skilled in Python, Pytorch and machine learning/neural network, with several projects available on platforms like GitHub and Kaggle", "link": "https://www.linkedin.com/in/rabiat-ibrahim-488716ab/"},
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
            st.image(Contributors_data[i]["image"], width=250, caption=Contributors_data[i]["name"])
            st.write(Contributors_data[i]["bio"])
            st.markdown(f"[{Contributors_data[i]['name']}'s LinkedIn]({Contributors_data[i]['link']})")

        
        # Column 2
        with col2:
        # Check if there is a second author in the row
            if i + 1 < len(Contributors_data):
                st.image(Contributors_data[i + 1]["image"], width=250, caption=Contributors_data[i + 1]["name"])
                st.write(Contributors_data[i + 1]["bio"])
                st.markdown(f"[{Contributors_data[i + 1]['name']}'s LinkedIn]({Contributors_data[i + 1]['link']})")

    st.subheader("Mentor", divider='rainbow')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('    ')

    with col2:
        st.image("Home_Page/Shungu_dhlamini.jpg", width=250, caption='Shungu Dhlamini')
        st.markdown('''[Shungu Dhlamini's Linkedin](https://www.linkedin.com/in/shungu-dhlamini)''')
        
    with col3:
        st.write('    ')

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

    #Line plot of Annual Rainfall across each states
    st.subheader("Annual Rainfall across each states", divider='rainbow')
    st.line_chart(df.pivot_table(index='states', columns='Year', values='Annual Rainfall mm').fillna(0), height=400)
    #st.plotly_chart(px.line(data=df, x='states', y=["Annual Rainfall mm", "Year"]), use_container_width=True)
#st.line_chart(data=df, x='states', y=['Annual Rainfall mm', "Year"], height = 400)


    #Plot of Crops accross each states
    st.subheader("Crops across each State", divider='rainbow')
    #food_crop = st.selectbox('Select Crop Type:', df['crops'].unique())

    # Filter DataFrame based on selected state
    filtered_df = df[df['crops'] == selected_crop]

    #st.title(f'Crop Concentration in {selected_state}')

    # Scatter plot
    st.map(filtered_df, latitude='Latitude', longitude='Longitude')


elif state.page == "Predictions":
    st.header("Predictions", divider='rainbow')

    # Load the pre-trained model
    with open('Home_Page/food-price-prediction-model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Add user input elements (e.g., sliders, dropdowns) for model input features
    Date = st.text_input("Enter a date:", "default_value")
    Crops = st.select_box("Choose crop:", df['crops'].unique())
    State = st.select_box("Choose state:", df['states'].unique())

    # When the user clicks a button or interacts with an input element, make a prediction
    if st.button("Predict"):
        #predictions based on user input
        prediction = model.predict([[Date, Crops, State]])

        # Display the prediction
        st.write(f"Predicted Price: {prediction[0]}")

# Feedback Page
elif state.page == "Feedback":
    st.title("Food Prediction Model")
    
    # Page content
    # Check if the CSV file exists, if not, create one
    csv_file_path = 'src/data/feedback.csv'
    if not os.path.isfile(csv_file_path):
        df = pd.DataFrame(columns=['Name', 'Email', 'Feedback'])
        df.to_csv(csv_file_path, index=False)
        
    st.header("Feedback Form :envelope_with_arrow:", help="Feel free to share your thoughts, suggestions, or report issues.", divider='rainbow')

    # Feedback form
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    feedback = st.text_area("Feedback:")
    #submit_button = st.button("Submit Feedback")

    # Handle feedback submission
    if st.button("Submit"):
        if name and email and subject and feedback:
            # Load existing data from CSV
            df = pd.read_csv(csv_file_path)
        
            # Append new entry
            new_entry = {'Name': name, 'Email': email, 'Subject': subject, 'Feedback': feedback}
            # df = df.append(new_entry, ignore_index=True)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        
            # Save updated data to CSV
            df.to_csv(csv_file_path, index=False)
        
            st.success("Feedback submitted successfully!")
        else:
            st.warning("Please fill out all fields.")
            

    st.header("Repository Link")
    st.markdown("[Github Repository](https://github.com/OhuneneIbrahim/Agricultural-food-price-prediction.git)")
