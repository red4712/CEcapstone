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
        <h3 class="profile-name">주원빈</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">소개</h2>
        <p class="description-text">
          주원빈은 컴퓨터공학과 학생으로, 컴퓨터공학 분야에서의 지식과 기술을 습득하고 자신의 역량을 향상시키고자 노력하고 있습니다. 프로그래밍 언어에 대한 지식과 활용능력을 보유하며, 알고리즘과 데이터 구조를 이해하고 다양한 문제를 해결해나갈 수 있는 능력을 지니고 있습니다.
        </p>
      </div>
    </div>
  </div>
<div class="about-page">
    <div class="about-container">
      <div class="profile-container">
        <img class="profile-image" src="./assets/author.jpg" alt="profile" />
        <h3 class="profile-name">박지원</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">소개</h2>
        <p class="description-text">
박지원은 컴퓨터공학과 학생으로, 컴퓨터 시스템에 대한 이해와 응용 능력을 가지고 있습니다. 프로그래밍 언어와 웹 개발 분야에서 지식과 기술을 습득하고, 다양한 프로젝트 경험을 통해 협업과 문제해결 능력을 향상시켜 나가고 있습니다. 창의적인 생각과 문제 해결 능력을 바탕으로 좋은 결과를 도출해내는 능력을 가지고 있습니다.


        </p>
      </div>
    </div>
  </div>
<div class="about-page">
    <div class="about-container">
      <div class="profile-container">
        <img class="profile-image" src="./assets/author.jpg" alt="profile" />
        <h3 class="profile-name">최태민</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">소개</h2>
        <p class="description-text">
          최태민은 컴퓨터공학과 학생으로, 컴퓨터 시스템과 웹 개발에 대한 지식과 역량을 보유하고 있습니다. 프로그래밍 언어와 데이터베이스 등 다양한 분야에서 경험과 지식을 쌓아가며, 새로운 기술 동향과 트렌드에 관심을 가지고 자신의 능력을 끊임없이 발전시키고 있습니다. 창의적인 문제 해결 능력과 성실한 태도를 가지고 다양한 프로젝트를 성공적으로 수행한 경험이 있습니다.
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
          전학수 교수님은 현재 서울대학교 컴퓨터공학부에서 교수로 활동하고 있는 컴퓨터 공학자입니다. 그는 미국 캘리포니아 대학교 버클리 캠퍼스에서 박사학위를 받았으며, 이전에는 애플(Apple)에서 시스템 소프트웨어 엔지니어로 일했습니다.

전학수 교수님은 운영체제, 가상화 기술, 분산 시스템 등의 분야에서 연구하고 있으며, 이를 바탕으로 다양한 국제 학회에서 논문을 발표하고 있습니다. 그는 또한 국내외 다수의 대학과 연구소에서 연구원으로 활동하고 있으며, 국내외 대학에서 초청 강연을 하기도 합니다.
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
