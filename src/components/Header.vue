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
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      menuItems: [
        { id: 1, label: 'Home', link: 'http://127.0.0.1:8000/' },
        { id: 2, label: 'About', link: 'http://127.0.0.1:8000/api/' },
        { id: 3, label: 'Contact', link: '#' },
      ],
    }
  },
}
</script>

<style>
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
</style>