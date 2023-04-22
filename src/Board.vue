<template>
  <Header></Header>
  <div class="board">
    <h1 class="board_title">게시판</h1>
    <ul class="board_ul">
      <li v-for="post in displayedPosts" :key="post.id">
        <h2 class="board_h2">{{ post.id }}</h2>
        <p class="board__p">{{ post.title }}</p>
        <p>작성자: {{ post.content }}</p>
        <v-btn @click="deletePost(post.id)" class="delete-btn">Delete</v-btn>
      </li>
    </ul>
    <div class="pagination">
      <button @click="currentPage--" :disabled="currentPage === 1">&lt;</button>
      <button v-for="number in pageNumbers" :key="number" @click="currentPage = number">
        {{ number }}
      </button>
      <button
        @click="currentPage++"
        :disabled="displayedPosts.length < postsPerPage || currentPage === pageCount"
      >
        &gt;
      </button>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import axios from "axios";

export default {
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      posts: [],
      currentPage: 1,
      postsPerPage: 10,
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
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then((response) => {
        this.posts = response.data.sort((a, b) => b.id - a.id); // 역순 정렬
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods: {
    deletePost(id) {
      axios
        .delete(`http://127.0.0.1:8000/api/${id}/`)
        .then(() => {
          // 삭제 요청이 성공하면 게시판에서 해당 게시물을 제거합니다.
          this.posts = this.posts.filter((post) => post.id !== id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

:root {
  --primary-color: #005aa0;
  --secondary-color: #3e6b49;
  --accent-color: #f3ca3e;
}

#Board .board {
  width: 80%;
  margin: 50px auto;
  /* background-image: url("./assets/cablecar.jpg"); */
  background-repeat: no-repeat;
  background-size: cover;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 20px;
}

#List ul {
  list-style-type: none;
  padding: 0;
}

li {
  border: 1px solid var(--primary-color);
  border-radius: 20px;
  margin-bottom: 20px;
  padding: 20px;
  background-color: var(--secondary-color);
  color: #f5f5f5;
}

li:hover {
  transform: translateY(-5px);
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

h1 {
  text-align: center;
  color: var(--primary-color);
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
  background-color: var(--secondary-color);
  border: 1px solid white;
  color: white;
  margin-right: 10px;
}

.pagination button:hover {
  background-color: var(--accent-color);
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
.delete-btn {
  border-radius: 50px;
  background-color: #2196f3;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.2s ease-in-out;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  border: none;
  cursor: pointer;
}

.delete-btn:hover {
  background-color: #0d8bf5;
  transform: translateY(-2px);
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.3);
}

.delete-btn:focus {
  outline: none;
}

.delete-btn:active {
  transform: translateY(0px);
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}
</style>
