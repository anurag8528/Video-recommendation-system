import pickle
import streamlit as st
import requests
from PIL import Image


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)   
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title("Upload Image / clip ")
# Create a file uploader for image files with drag-and-drop functionality
uploaded_image = st.file_uploader("You Want to Find Related Clip", type=["jpg", "jpeg", "png"])

# Check if an image file is uploaded
if uploaded_image is not None:
    # Open the image file using PIL
    image = Image.open(uploaded_image)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Show image details
    st.write("Filename:", uploaded_image.name)
    st.write("Image format:", image.format)
    st.write("Image size:", image.size)
    
st.markdown(
    """
<style>
    /* Set the background color or image */
    .stApp {
        background-image: url('https://as2.ftcdn.net/v2/jpg/08/48/33/53/1000_F_848335388_jD5aySbYZE78I6NNEmjPSk7QKqIkAMT5.jpg');
        #background-image: url('https://i.pinimg.com/originals/2c/c0/6d/2cc06dbf173752aed1d56103f0df9f3b.gif');
        #background-image: url('https://as2.ftcdn.net/v2/jpg/08/37/50/63/1000_F_837506303_E0RKihlZdn25b2hVtI2xySAaJ6BEj4fr.jpg');
        background-size: cover;
        background-position: center;
    }
    }
</style>

    """,
    unsafe_allow_html=True
)
# Streamlit content here
st.title("Video - Recommendation - System")
#st.write("You can Search ")

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:9]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


#st.header('Video - Recommendation - System')
movies = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a Videos from the dropdown",
    movie_list
)

if st.button('Show suggetion'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5,col6,col7,col8, = st.columns(8)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6]) 
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])




