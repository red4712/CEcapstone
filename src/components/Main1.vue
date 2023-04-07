<template>
  <form class="login-form" v-on:submit.prevent="submitForm"> 
    <div>
      <label for="id">ID:</label>
      <input id="id" type="text" v-model="id">
    </div>
    <div>
      <label for="title">Title:</label>
      <input id="title" type="text" v-model="title">
    </div>
    <div>
      <label for="content">Content:</label>
      <input id="content" type="text" v-model="content">
    </div>
    <button type="submit">Login</button>
  </form>
</template>

<script>
import axios from 'axios'
export default{

  data: function(){
    return {
      id: '',
      password: '',
      content: '',
    }
  },
  methods: {
    submitForm: function() {
      
      console.log(this.id, this.title, this.content);
      var url = 'http://127.0.0.1:8000/api/';
      var data = {
        id: this.id,
        title: this.title,
        content: this.content
      }
      axios.post(url, data)
        .then(function(response){
        console.log(response);
       })
        .catch(function(error){
          console.log(error);
        });
    }
  }    
}
</script>
<style scoped>

.login-form {
  align-items: flex-start; 
  display: flex;
  flex-direction: column;
  margin: 50px auto;
  padding: 30px;
  background-color: #24272E;
  color: white;
  font-size: 20px;
  border-radius: 10px;
}

.login-form div {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  margin-right: 10px;
}

input {
  display: block;
  padding: 5px 10px;
  font-size: 18px;
  border-radius: 5px;
  border: none;
  outline: none;

}

button {
  padding: 8px 15px;
  font-size: 18px;
  border-radius: 5px;
  border: none;
  outline: none;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
}

button:hover {
  background-color: #3e8e41;
}
</style>