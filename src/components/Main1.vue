<template>
  <div class="container">
    <div>
    <MapKakao :latitude="37.39843974939604" :longitude="127.10972941510465" />
  </div>
    <div class="intro-container">
      <h3 style="color: black">목포관광 홈페이지에 오신 것을 환영합니다.</h3>
      <p style="color: black">
        아름다운 해안 도시 목포와 그 주변 지역을 탐험하세요. 아름다운 자연 경관에서 풍부한
        문화 유산에 이르기까지 목포는 모두를 위한 무언가를 가지고 있습니다.
      </p>
      <p style="color: black">
        지역 명소, 이벤트 및 활동을 발견하고 포괄적인 여행 가이드 및 리소스를 사용하여
        쉽게 여행 계획을 세우십시오.
      </p>
      <p style="color: black">자유게시판 글쓰기를 이용하여 소통해주세요.</p>
    </div>
  </div>
</template>

<script>

import MapKakao from './MapKakao.vue';

export default {
  components: {
    MapKakao
  }
}

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