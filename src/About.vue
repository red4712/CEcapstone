<template>
  <Header></Header>
  <div class="about-page">
    <h1 class="title">About</h1>
    <div class="about-container">
      <div class="profile-container">
        <img class="profile-image" src="./assets/author.jpg" alt="profile" />
        <h3 class="profile-name">서욱현</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">소개</h2>
        <p class="description-text">
          안녕하세요, 저는 목포대학교 컴퓨터공학과 학생입니다. 저는 소프트웨어 개발에
          열정적이며 새로운 기술을 탐구하는 것을 좋아합니다. 제 관심 분야는 웹 개발,
          모바일 개발, 기계 학습입니다.
        </p>
      </div>
    </div>
  </div>
  <div class="about-page">
    <div class="about-container">
      <div class="profile-container">
        <img class="profile-image" src="./assets/author.jpg" alt="profile" />
        <h3 class="profile-name">전학수</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">소개</h2>
        <p class="description-text">
          안녕하세요 박종우 유튜브 트위치를 항상 챙겨보는 전학수입니다 삶이란 시련과 같은
          말이야~ 고개좀 들고좀 어깨 펴 짜샤~ 형도 그랬단다 죽고싶었지만~ 견뎌~....
          보니...! 갠찬더라~
        </p>
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
export default {
  name: "About",
  components: {
    Header,
    Footer,
  },
};
</script>

<style scoped>
.about-page {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f7f7f7;
}

.title {
  font-size: 4rem;
  margin-bottom: 2rem;
}

.about-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  width: 80%;
}

.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

.profile-image {
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  object-fit: cover;
}

.profile-name {
  font-size: 2rem;
  font-weight: bold;
  margin-top: 1rem;
  transition: opacity 0.5s, transform 0.5s;
}

@media (max-width: 768px) {
  .profile-container {
    flex-direction: row;
  }

  .profile-image {
    width: 5rem;
    height: 5rem;
    margin-right: 1rem;
  }

  .profile-name {
    font-size: 1.5rem;
  }

  .about-container {
    width: 100%;
    padding: 1rem;
  }

  .description-title {
    font-size: 1.8rem;
  }

  .description-text {
    font-size: 1.2rem;
  }
}

.description-title {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.description-text {
  font-size: 1.5rem;
  line-height: 1.5;
}

.fade-out {
  opacity: 0;
  animation: fade-out 1s forwards;
}

@keyframes fade-out {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(-50%);
  }
}
</style>
