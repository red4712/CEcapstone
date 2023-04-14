<template>
  <form>
    <div class="form-group">
      <label for="name">이름</label>
      <input type="text" class="form-control" id="name" v-model="name" required>
    </div>
    <div class="form-group">
      <label for="email">이메일</label>
      <input type="email" class="form-control" id="email" v-model="email" required>
    </div>
    <div class="form-group">
      <label for="phone">전화번호</label>
      <input type="tel" class="form-control" id="phone" v-model="phone" required>
    </div>
    <div class="form-group">
      <label for="message">문의 내용</label>
      <textarea class="form-control" id="message" v-model="message" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary" @click.prevent="submitForm">전송</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      phone: '',
      message: '',
    };
  },
  methods: {
    submitForm() {
      // 폼 전송 로직
      console.log('폼 전송');
    },
  },
};
</script>
<style>
  form {
    max-width: 600px;
    margin: 0 auto;
  }

  .form-group {
    margin-bottom: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
  }

  input[type="text"],
  input[type="email"],
  input[type="tel"],
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    resize: vertical;
  }

  button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
  }

  button[type="submit"]:hover {
    background-color: #45a049;
  }

  .form-control {
    font-size: 16px;
  }
</style>