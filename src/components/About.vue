<template>
  <div class="about-page">
    <h1 class="title">About</h1>
    <div class="about-container">
      <div class="profile-container">
        <img class="profile-image" src="../assets/author.jpg" alt="profile">
        <h3 class="profile-name">{{ name }}</h3>
      </div>
      <div class="description-container">
        <h2 class="description-title">Introduction</h2>
        <p class="description-text">
          Hello, I am a computer engineering student at XYZ University. I am passionate about software development and I love to explore new technologies. My areas of interest include web development, mobile development, and machine learning.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      name: "서욱현",
      lastScrollY: 0
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  unmounted() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.lastScrollY = window.scrollY;
    }
  },
  computed: {
    profileNameStyle() {
      return {
        opacity: this.lastScrollY > 200 ? 1 : this.lastScrollY / 200,
        transform: `translateY(${this.lastScrollY / 2}px)`
      };
    }
  }
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