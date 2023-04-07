<template>
  <footer class="footer">
    <div class="footer__logo">
      <img src="../assets/logo.png" alt="company logo" />
      <div class="footer__logo-text">Game Company</div>
    </div>
    <div class="footer__links">
      <div class="footer__link-group">
        <div class="footer__link-group-title">ABOUT US</div>
        <a href="#">Company</a>
        <a href="#">News</a>
        <a href="#">Careers</a>
      </div>
      <div class="footer__link-group">
        <div class="footer__link-group-title">SERVICES</div>
        <a href="#">Games</a>
        <a href="#">Platform</a>
        <a href="#">Store</a>
      </div>
      <div class="footer__link-group">
        <div class="footer__link-group-title">CONTACT US</div>
        <a href="#">Email</a>
        <a href="#">Phone</a>
        <a href="#">Address</a>
      </div>
    </div>
    <div class="footer__copy">
      © 2023 Game Company. All Rights Reserved.
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