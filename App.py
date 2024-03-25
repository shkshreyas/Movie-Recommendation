import streamlit as st 
import pickle
import pandas as pd
import requests
def poster(mid):
   response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(mid))
   data=response.json()
   return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
  mi=movies[movies['title']==movie].index[0] #movie index
  dist=similarity[mi] #distances
  ml=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6] #movie list
  rm=[]
  posters=[]
  for i in ml:
    rm.append(movies.iloc[i[0]].title)
    posters.append(poster(movies.iloc[i[0]].movie_id))
  return rm,posters
   
movie_data=pickle.load(open('movie_data.pkl','rb'))
movies=pd.DataFrame(movie_data)
st.title("Recommend Movies")
similarity=pickle.load(open('similarity.pkl','rb'))
movie_selected=st.selectbox(
    'Enter Movie Name',movies['title'].values)
if st.button('Recommend'):
    r,p=recommend(movie_selected)
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
       st.text(r[0])
       st.image(p[0])
    with col2:
       st.text(r[1])
       st.image(p[1])
    with col3:
       st.text(r[2])
       st.image(p[2])
    with col4:
       st.text(r[3])
       st.image(p[3])
    with col5:
       st.text(r[4])
       st.image(p[4])
