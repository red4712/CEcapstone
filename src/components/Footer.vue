<template>
  <footer class="footer">
    <div class="footer__logo">
      <img src="../assets/logo.png" alt="company logo" />
      <div class="footer__logo-text">해양도시목포</div>
    </div>
    <div class="footer__links">
      <div class="footer__link-group">
        <div class="footer__link-group-title">SNS</div>
        <a href="https://discord.com/">Discord</a>
        <a href="https://www.instagram.com/">Instargram</a>
        <a href="https://ko-kr.facebook.com/">Facebook</a>
      </div>
      <div class="footer__link-group">
        <div class="footer__link-group-title">서비스</div>
        <a href="https://play.google.com/store/games">게임</a>
        <a href="https://www.expedia.co.kr/Mokpo.dx2399">관광지</a>
        <a href="https://www.tripadvisor.co.kr/Attractions-g1074117-Activities-c26-t144-Mokpo_Jeollanam_do.html">상점</a>
      </div>
      <div class="footer__link-group">
        <div class="footer__link-group-title">문의하기</div>
        <a href="https://mail.naver.com/">이메일</a>
        <a href="https://www.mokpo.go.kr/tour/tourguide/information/desk">전화번호</a>
        <a href="https://m.place.naver.com/place/34807808/home?entry=ple">주소</a>
      </div>
    </div>
    <div class="footer__copy">
      © 2023 해양도시목포.
       <br>컴퓨터공학과 서욱현, 주원빈, 전학수, 박지원, 최태민.
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #1d1d1d;
  color: #fff;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 3rem;
}

.footer__logo img {
  width: 4rem;
}

.footer__logo-text {
  font-size: 2rem;
  font-weight: bold;
  margin-left: 1rem;
}

.footer__links {
  display: flex;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.footer__link-group {
  margin-right: 5rem;
  margin-bottom: 2rem;
}

.footer__link-group-title {
  font-weight: bold;
  margin-bottom: 1rem;
}

.footer__links a {
  color: #fff;
  margin-bottom: 1rem;
  display: block;
  text-decoration: none;
}

.footer__links a:hover {
  text-decoration: underline;
}

.footer__copy {
  font-size: 1.2rem;
  opacity: 0.7;
  margin-top: 2rem;
}

@media (max-width: 768px) {
  .footer {
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem;
  }

  .footer__links {
    margin-top: 1rem;
  }

  .footer__link-group {
    margin-right: 0;
    margin-bottom: 1rem;
  }

  .footer__logo-text {
    margin-left: 0;
    margin-bottom: 1rem;
  }
}
</style>