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
    pages = ["Introduction", "Authors", "Charts", "Prediction", "Feedback"]
    selected_page = st.sidebar.radio("Go to:", pages)

# Update page in the session state
state.page = selected_page

# Introduction Page
if state.page == "Introduction":
    st.title("Food Prediction Model")
    st.markdown("---")# Horizontal Line below the logo

 # Page content
    st.header("Introduction")
    image = st.image("Home_Page/foodstuffs.jpg", use_column_width=True)
    st.write("Introduction content goes here.")
  
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


    # Project Overview
#st.markdown("""
    #<style>
        #h3{
            #margin-left: 50px;
        #}
        #p{
         #   margin-left: 50px;
         #   text-align: justify;
       # }
    #</style>
   # <h3>Overview of the Project</h3>
   # <p>Food prices hold significant influence over the lives of people globally, impacting factors such as affordability, food security, and economic stability. This project leverages Machine Learning (ML) techniques and Python programming to analyze historical food prices data in Nigeria, predict future prices, and offer valuable insights for consumers, policymakers, and stakeholders.</p>
   # """, unsafe_allow_html=True)



# Footer
st.markdown("---")
