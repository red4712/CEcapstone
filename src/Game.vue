<template>
  <Header></Header>
  <div class="gamecontainer">
    <h1 class="gametitle">미니게임 점수판</h1>
    <table class="treasure-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>보물 이름</th>
          <th>보물 설명</th>
          <th>보물 포인트</th>
          <th>보물 이미지</th>
          <th>보물 입력일</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="treasure in treasures" :key="treasure.id">
          <td>{{ treasure.id }}</td>
          <td>{{ treasure.subject }}</td>
          <td>{{ treasure.modify_date }}</td>
          <td>{{ treasure.content }}</td>
          <td>
            <img v-if="treasure.imgfile" :src="`${treasure.imgfile}`" alt="보물 이미지" />
          </td>
          <td>{{ treasure.create_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <Main2></Main2>
  <Footer></Footer>
</template>

<script>
import axios from "axios";
import Main2 from "./components/Main2";
import Header from "./components/Header";
import Footer from "./components/Footer";
export default {
  name: "App",
  data() {
    return {
      treasures: [],
    };
  },
  components: {
    Header,
    Main2,
    Footer,
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/Question")
      .then((response) => {
        this.treasures = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
<style>
.gamecontainer {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Noto Sans KR", sans-serif;
}

.gametitle {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 40px;
  text-align: center;
  color: #009688;
}

.treasure-table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #ddd;
  font-size: 16px;
}

.treasure-table th {
  padding: 12px;
  text-align: left;
  background-color: #009688;
  color: #fff;
  border: 1px solid #ddd;
}

.treasure-table td {
  padding: 12px;
  border: 1px solid #ddd;
}

.treasure-table tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
