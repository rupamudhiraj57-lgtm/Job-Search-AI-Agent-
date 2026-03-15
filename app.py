import streamlit as st
from job_api import search_jobs

# Page configuration
st.set_page_config(
    page_title="AI Job Search Assistant",
    page_icon="💼",
    layout="wide"
)

# Custom CSS for job cards
st.markdown("""
<style>
.job-card {
    background-color: #f5f7ff;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}
.title {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>AI Job Search Assistant</h1>", unsafe_allow_html=True)
st.write("Find the latest job opportunities quickly and easily.")

# Sidebar filters
st.sidebar.header("Job Search Filters")

keyword = st.sidebar.text_input("Job Role", "Python Developer")

location = st.sidebar.selectbox(
    "Location",
    ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]
)

search_button = st.sidebar.button("Search Jobs")

# Main search functionality
if search_button:

    with st.spinner("Searching for jobs..."):
        jobs = search_jobs(keyword, location)

    if not jobs:
        st.warning("No jobs found. Try another keyword.")
    else:
        st.success(f"{len(jobs)} jobs found")

        for i, job in enumerate(jobs):

            st.markdown(f"""
            <div class="job-card">
                <h3>{job['title']}</h3>
                <p><b>Company:</b> {job['company']}</p>
                <p><b>Location:</b> {job['location']}</p>
                <p><b>Salary:</b> {job['salary']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.button("Apply Now", key=i)