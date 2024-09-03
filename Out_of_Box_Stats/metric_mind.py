import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.image("Out_of_Box_Stats/metric_mind.jpeg", width=300)
st.write("")
st.write("""
        Metric Mind is an out-of-the-box statistics generator that provides instant statistical insights into your 
        data with minimal effort. Simply drag, drop, or upload your CSV file, and let Metric Mind do the rest. 
        The tool automatically generates the following:
        - Summary Statistics
        - Box and Whisker plot with dimension selection and outlier integration
        - Correlation Matrix
        - Missing Data Counts
        - Various Histograms 
""")
st.write("")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Convert date columns to datetime format
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col])
            except ValueError:
                continue

    st.write("File successfully uploaded!")
    st.write(df.head()) 
    st.write("")

    analysis_type = st.radio("Choose Analysis Type", ("Numerical Analysis", "Categorical Analysis"))

    if analysis_type == "Numerical Analysis":

        st.write("### Basic Statistics")
    
        st.write("#### Summary Statistics")
        st.write(df.describe())
        st.write("")

        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        st.write("### Box and Whisker Plot")
        selected_column = st.selectbox("Select a column for Box and Whisker Plot:", numerical_columns)


        if selected_column:
            st.write(f"Box and Whisker Plot for {selected_column}")

        # Generate the horizontal boxplot
        plt.figure()
        data = df[selected_column].dropna()

        # Create the boxplot
        boxplot = plt.boxplot(data, patch_artist=True, vert=False)

        plt.ylabel(selected_column)
        plt.title(f'Box and Whisker Plot of {selected_column}')

        # Extract the statistics manually
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        median = np.median(data)
        min_whisker = np.min(data[data >= Q1 - 1.5 * (Q3 - Q1)])
        max_whisker = np.max(data[data <= Q3 + 1.5 * (Q3 - Q1)])

        # Annotate the plot with statistics below the boxplot
        y_positiona = .65 
        y_positionb = .75
        plt.text(median, y_positionb, f'Median: {median:.2f}', horizontalalignment='center')
        plt.text(Q1, y_positiona, f'Q1: {Q1:.2f}', horizontalalignment='center')
        plt.text(Q3, y_positiona, f'Q3: {Q3:.2f}', horizontalalignment='center')
        plt.text(min_whisker, y_positionb, f'Min: {min_whisker:.2f}', horizontalalignment='center')
        plt.text(max_whisker, y_positionb, f'Max: {max_whisker:.2f}', horizontalalignment='center')

        st.pyplot(plt)
        st.write("")
            
        st.write("#### Correlation Matrix")
        # Exclude non-numerical columns for correlation matrix
        numerical_df = df.select_dtypes(include=['float64', 'int64'])
        st.write(numerical_df.corr())
        
        st.write("#### Missing Data")
        st.write(df.isnull().sum())
        
        st.write("#### Histograms")
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in numerical_columns:
            st.write(f"Histogram for {col}")
            plt.figure()
            plt.hist(df[col].dropna(), bins=20, edgecolor='k')
            plt.xlabel(col)
            plt.ylabel('Counts')  # Change the y-axis label to "Counts"
            plt.title(f'Histogram of {col}')
            st.pyplot(plt)  # Display the histogram in Streamlit

    elif analysis_type == "Categorical Analysis":
        st.write("### Categorical Variable Analysis")
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns
        
        for col in categorical_columns:
            st.write(f"**Analysis for {col}**")
            
            # Value counts
            st.write("**Value Counts:**")
            st.write(df[col].value_counts())
            
            # Mode
            st.write(f"**Most Frequent Category (Mode):** {df[col].mode()[0]}")
            
            # Bar Plot
            st.write(f"**Bar Plot for {col}:**")
            plt.figure(figsize=(10, 5))
            sns.countplot(y=df[col], order=df[col].value_counts().index, palette="viridis")
            plt.title(f'Bar Plot of {col}')
            plt.xlabel('Counts')
            plt.ylabel(col)
            st.pyplot(plt)
