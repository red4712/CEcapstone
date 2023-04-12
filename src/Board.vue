<template>
    <div class="board">
      <h1>게시판</h1>
      <ul>
        <li v-for="post in posts" :key="post.id">
          <h2>{{ post.id }}</h2>
          <p>{{ post.title }}</p>
          <p>작성자: {{ post.content }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
        return {
            posts: []
        };
    },
    mounted() {
        axios
            .get("http://127.0.0.1:8000/api/")
            .then(response => {
            this.posts = response.data;
        })
            .catch(error => {
            console.log(error);
        });
     
    },
};
  </script>
  
  <style>
  .board {
    background-color: #f2f2f2;
    padding: 20px;
    margin: 20px;
  }
  
  .board h1 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .board ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .board li {
    background-color: white;
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .board li h2 {
    font-size: 18px;
    margin-bottom: 5px;
  }
  
  .board li p {
    font-size: 14px;
    margin-bottom: 5px;
  }
  </style>