<template>
  <div class="slider-container">
    <div
      class="slider-wrapper"
      :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
    >
      <div class="slider-slide" v-for="(image, index) in images" :key="index">
        <img :src="image" />
      </div>
    </div>
    <button class="slider-button slider-button-prev" @click="prevSlide">&lt;</button>
    <button class="slider-button slider-button-next" @click="nextSlide">&gt;</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: [
        require("@/assets/목포1.jpg"),
        require("@/assets/목포2.jpg"),
        require("@/assets/목포3.jpg"),
        require("@/assets/목포4.jpg"),
      ],
      currentSlide: 0,
      timerId: null,
    };
  },
  mounted() {
    this.timerId = setInterval(this.nextSlide, 5000);
  },
  beforeUnmount() {
    clearInterval(this.timerId);
  },
  methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.images.length;
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.images.length) % this.images.length;
    },
  },
};
</script>

<style>
.slider-container {
  position: relative;
  width: 100%;
  height: 500px;
  overflow: hidden;
}

.slider-wrapper {
  position: relative;
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.5s ease-in-out;
}

.slider-slide {
  flex: 1 0 100%;
  height: 100%;
}

.slider-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slider-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  border: none;
  background-color: rgba(255, 255, 255, 0.5);
  font-size: 24px;
  color: #333;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.slider-button:hover {
  background-color: rgba(255, 255, 255, 0.7);
}

.slider-button-prev {
  left: 0;
  border-radius: 0 25px 25px 0;
}

.slider-button-next {
  right: 0;
  border-radius: 25px 0 0 25px;
}
</style>
