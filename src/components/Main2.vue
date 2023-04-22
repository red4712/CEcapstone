<template>
  <div class="container">
    <div class="form-container">
      <form class="login-form" v-on:submit.prevent="submitForm">
        <div>
          <label for="subject">제목:</label>
          <input id="subject" type="text" v-model="subject" class="input-field" />
        </div>
        <div>
          <label for="content">내용:</label>
          <input id="content" type="text" v-model="content" class="input-field" />
        </div>
        <div>
          <label for="imgfile">Image</label>
          <input type="file" ref="fileInput" @change="uploadFile" />
          <img v-if="imageUrl" :src="imageUrl" />
        </div>
        <button type="submit" class="submit-button">글쓰기</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      subject: "",
      content: "",
      imgfile: null,
      imageUrl: null,
    };
  },
  methods: {
    uploadFile() {
      this.imgfile = this.$refs.fileInput.files[0];
      this.imageUrl = URL.createObjectURL(this.imgfile);
    },
    submitForm() {
      const formData = new FormData();
      formData.append("subject", this.subject);
      formData.append("content", this.content);
      formData.append("imgfile", this.imgfile);

      axios
        .post("http://127.0.0.1:8000/api/Question/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response.data);
          // 데이터 전송 성공 시 처리할 코드 작성
        })
        .catch((error) => {
          console.log(error);
          // 데이터 전송 실패 시 처리할 코드 작성
        });
    },
  },
};
</script>

<style>
.container {
  display: flex;
  width: 100%;
  height: 300px;
  padding: 20px;
  box-sizing: border-box;
  font-family: Arial, sans-serif;
  background-color: #fff;
  color: #fff;
}

.form-container {
  background-color: #374151;
  width: 800px;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

.input-field {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ccc;
  background-color: #374151;
  color: #fff;
}

.submit-button {
  background-color: #22c55e;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.submit-button:hover {
  background-color: #16a34a;
}

.title-container {
  margin-bottom: 20px;
}

.intro-container {
  float: left;
  width: 50%;
  margin-right: 20px;
  margin-left: 20px;
}
</style>
