#Line plot of Annual Rainfall across each states
    st.subheader("Inflation over the Years", divider='rainbow')
    st.line_chart(df.pivot_table(index='states', columns='Year', values='Inflation').fillna(0), height=400)
