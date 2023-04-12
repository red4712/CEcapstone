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
    <button @click="showModal = true" class="btn btn-primary">Login</button>
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

<style>
.login-btn {
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background-color: #f8f8f8;
  border-bottom: 1px solid #ccc;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  margin-right: 1rem;
}

nav a {
  color: #333;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
}

.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #f8f8f8;
  margin: 10% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 30%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>