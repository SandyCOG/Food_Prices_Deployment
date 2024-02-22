df = pd.read_csv('Home_Page/food_price_dataset.csv')
#Line plot of Annual Rainfall across each states
    st.subheader("Inflation over the Years", divider='rainbow')
    st.line_chart(df.pivot_table(index='states', columns='Year', values='inflation_rate(food_item monthly avg.)').fillna(0), height=400)
