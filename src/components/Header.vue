<template>
  <div class="header">
    <img src="../assets/로고.webp" alt="Logo" style="width: 70px; height: 70px" />
    <nav>
      <ul>
        <li v-for="item in menuItems" :key="item.id">
          <a :href="item.link">{{ item.label }}</a>
        </li>
      </ul>
    </nav>
    <button class="btn" @click="showModal = true">
      <div class="icon-container">
        <i class="fas fa-sign-in-alt"></i>
        <i class="fas fa-circle"></i>
      </div>
      <span v-if="userName">{{ userName }} 님</span>
      <span v-else>로그인</span>
    </button>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showModal = false">&times;</span>
        <h2>회원 로그인</h2>
        <form @submit.prevent="submitLogin">
          <div class="form-group">
            <label for="email">이메일</label>
            <input
              type="email"
              class="form-control"
              id="email"
              placeholder="이메일을 입력해주세요"
              required
              v-model="email"
            />
          </div>
          <div class="form-group">
            <label for="password">비밀번호</label>
            <input
              type="password"
              class="form-control"
              id="password"
              placeholder="비밀번호를 입력해주세요"
              required
              v-model="password"
            />
          </div>
          <button type="submit" class="btn btn-primary">로그인</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      menuItems: [
        { id: 1, label: "Home", link: "http://127.0.0.1:8000/" },
        { id: 2, label: "About", link: "http://127.0.0.1:8000/About/" },
        { id: 3, label: "QnA", link: "http://127.0.0.1:8000/QnA/" },
        { id: 4, label: "Board", link: "http://127.0.0.1:8000/Board/" },
        { id: 5, label: "AR", link: "http://127.0.0.1:8000/AR/" },
        { id: 6, label: "Game", link: "http://127.0.0.1:8000/Game/" },
      ],
      showModal: false,
      email: "",
      password: "",
      userName: "",
    };
  },
  created() {
    // 로그인한 사용자 정보가 localStorage에 저장되어 있는지 확인
    const user = localStorage.getItem("user");
    if (user) {
      // 사용자 이름 보여주기
      this.userName = JSON.parse(user).username;
    }
  },
  methods: {
    async submitLogin() {
      const response = await fetch("http://127.0.0.1:8000/api/User/");
      const users = await response.json();
      const user = users.find(
        (u) => u.email === this.email && u.password === this.password
      );
      if (user) {
        // 로그인 성공
        alert("로그인 성공!");
        this.showModal = false;
        // 사용자 정보 localStorage에 저장
        localStorage.setItem("user", JSON.stringify(user));
        // 사용자 이름 보여주기
        this.userName = user.username;
      } else {
        // 로그인 실패
        alert("아이디 또는 비밀번호가 올바르지 않습니다.");
      }
    },
  },
};
</script>

<style scoped>
/* Style for the header */
.header {
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #1d1d1d;
  color: #fff;
  font-family: Arial, sans-serif;
}

.header img {
  margin-right: 10px;
}

.header nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.header nav li {
  margin-right: 150px;
}

.header nav li:last-child {
  margin-right: 0;
}

.header nav a {
  text-decoration: none;
  color: #fff;
  font-size: 18px;
  transition: all 0.3s ease;
}

/* .header nav a:hover {
  color: #f1c40f;
} */

.header .btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  color: #fff;
  border: 2px solid #fff;
  border-radius: 20px;
  padding: 10px 15px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.header .btn:hover {
  background-color: #fff;
  color: #000;
}

.header .btn .icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.header .btn .icon-container .fa-sign-in-alt {
  font-size: 20px;
}

.header .btn .icon-container .fa-circle {
  font-size: 6px;
  position: absolute;
  top: 10px;
  right: 10px;
}

/* Style for the modal */
.modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: #1d1d1d;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  height: 300px;
  position: relative;
}

.modal-content h2 {
  margin-top: 0;
  font-family: Arial, sans-serif;
  text-align: center;
  margin-bottom: 20px;
  color: #fff;
}

.modal-content form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.modal-content .form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
  width: 100%;
}

.modal-content .form-group label {
  font-family: Arial, sans-serif;
  margin-bottom: 5px;
}

.modal-content .form-group input {
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
}

.modal-content button[type="submit"] {
  background-color: #f1c40f;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 18px;
  color: black;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
</style>
