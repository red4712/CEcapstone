<template>
    <Header></Header>
    <div class="board">
        <h1 class="board_title">게시판</h1>
        <ul class="board_ul">
            <li v-for="post in displayedPosts" :key="post.id">
                <h2 class="board_h2">{{ post.id }}</h2>
                <p class="board__p">{{ post.title }}</p> 
                <p>작성자: {{ post.content }}</p>
            </li>
        </ul>
        <div class="pagination">
            <button @click="currentPage--" :disabled="currentPage === 1">&lt;</button>
            <button v-for="number in pageNumbers" :key="number" @click="currentPage = number">{{ number }}</button>
            <button @click="currentPage++" :disabled="displayedPosts.length < postsPerPage || currentPage === pageCount"> &gt;</button>
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
                this.posts = response.data.sort((a, b) => b.id - a.id); // 역순 정렬
            })
            .catch(error => {
                console.log(error);
            });
    },
};
</script>
  
 <style>

    .board {
        width: 80%;
        margin: 50px auto;
    }
    
    ul {
        list-style-type: none;
        padding: 0;
    }
    
    li {
        border: 1px solid #1d1d1d;
        border-radius: 20px;
        margin-bottom: 20px;
        padding: 20px;
        background-color: #444444;
        color: white;
    }
    
    h1 {
        text-align: center;
        color: #1d1d1d;
    }
    
    h2 {
        font-size: 24px;
        margin-bottom: 10px;
    }
    
    .pagination {
        text-align: center;
        margin-top: 30px;
    }
    
    .pagination button {
        border-radius: 50%;
        width: 30px;
        height: 30px;
        background-color: #444444;
        border: 1px solid white;
        color: white;
        margin-right: 10px;
    }
    
    .pagination button:hover {
        background-color: #666666;
        cursor: pointer;
    }
    
    .pagination button:disabled {
        background-color: #888888;
        cursor: not-allowed;
    }
    
    .pagination button.active {
        background-color: #888888;
        cursor: default;
    }
    
    .pagination button:focus {
        outline: none;
    }
</style>