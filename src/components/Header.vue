<template>
  <div class="header">
    <img src="../assets/logo.png" alt="Logo" style="width: 70px; height: 70px;">
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
      <span>Login</span>
    </button>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showModal = false">&times;</span>
        <h2>Login</h2>
        <form>
          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" class="form-control" id="email" placeholder="Enter your email" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" placeholder="Enter your password" required>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      menuItems: [
        { id: 1, label: 'Home', link: 'http://127.0.0.1:8000/' },
        { id: 2, label: 'About', link: 'http://127.0.0.1:8000/About/' },
        { id: 3, label: 'Contact', link: 'http://127.0.0.1:8000/Contact/' },
        { id: 4, label: 'Board', link: 'http://127.0.0.1:8000/Board/'}
      ],
      showModal: false,
    }
  },
}
</script>


<style scoped>
/* Style for the header */
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #000;
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
  margin-right: 20px;
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

.header nav a:hover {
  color: #f1c40f;
}

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
  margin-right: 10px;
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
  background-color: rgba(0,0,0,0.4);
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

.modal-content button[type=submit] {
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