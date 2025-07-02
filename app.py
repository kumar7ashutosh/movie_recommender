import streamlit as st 
import pickle,pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    rec_movies=[]
    for i in movies_list:
        rec_movies.append(movies.iloc[i[0]].title)
    return rec_movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('movie recommender')
selected_movie_name = st.selectbox(
    'how would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    rec=recommend(selected_movie_name)
    for i in rec:
     st.write(i)
    
