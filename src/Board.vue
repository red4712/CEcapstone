<template>
    <Header></Header>
    <div class="board">
        <h1>게시판</h1>
        <ul>
            <li v-for="post in displayedPosts" :key="post.id">
                <h2>{{ post.id }}</h2>
                <p>{{ post.title }}</p> 
                <p>작성자: {{ post.content }}</p>
            </li>
        </ul>
        <div class="pagination">
            <button @click="currentPage--" :disabled="currentPage === 1">이전</button>
            <button v-for="number in pageNumbers" :key="number" @click="currentPage = number">{{ number }}</button>
            <button @click="currentPage++" :disabled="displayedPosts.length < postsPerPage || currentPage === pageCount">다음</button>
        </div>
    </div>
    <Footer></Footer>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'
import axios from 'axios';

export default {
    components: {
        Header,
        Footer,
    },
    data() {
        return {
            posts: [],
            currentPage: 1,
            postsPerPage: 10
        };
    },
    computed: {
        displayedPosts() {
            const startIndex = (this.currentPage - 1) * this.postsPerPage;
            return this.posts.slice(startIndex, startIndex + this.postsPerPage);
        },
        pageCount() {
            return Math.ceil(this.posts.length / this.postsPerPage);
        },
        pageNumbers() {
            const numbers = [];
            for (let i = 1; i <= this.pageCount; i++) {
                numbers.push(i);
            }
            return numbers;
        }
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