<template>
  <button class="navbutton" @click="toggleNavbar">
    네비게이션바 {{ isNavbarVisible ? "끄기" : "켜기" }}
  </button>
  <div class="navbar" v-if="isNavbarVisible">
    <div
      class="navbar__item"
      v-for="(item, index) in items"
      :key="index"
      :class="{ active: index === activeItem }"
      @click="setActiveItem(index)"
    >
      <div class="navbar__item__icon">
        <i :class="item.icon"></i>
      </div>
      <div class="navbar__item__text">{{ item.title }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          title: "축제",
          icon: "fas fa-flag",
        },
        {
          title: "항공AR",
          icon: "fas fa-plane",
        },
        {
          title: "로드뷰",
          icon: "fas fa-road",
        },
        {
          title: "스마트 관광앱",
          icon: "fas fa-mobile-alt",
        },
      ],
      activeItem: 0,
      isNavbarVisible: true, // 새로운 데이터 속성 추가
    };
  },
  methods: {
    setActiveItem(index) {
      this.activeItem = index;
    },
    toggleNavbar() {
      this.isNavbarVisible = !this.isNavbarVisible; // 속성값 토글
    },
  },
};
</script>

<style scoped>
.navbutton {
  z-index: 999;
  position: fixed;
  top: 45%;
  right: 0;
  transform: translateY(-0%);
  display: flex;
  flex-direction: column;
  align-items: center;
}
.navbar {
  z-index: 999;
  position: fixed;
  top: 50%;
  right: 30px;
  transform: translateY(-0%);
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f5f5f5;
  border-radius: 50px;
  padding: 15px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.navbar__item {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 15px;
  margin-bottom: 10px;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.navbar__item.active {
  background-color: #ff6b6b;
  color: #fff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

/* .navbar__item:hover {
  background-color: #d3d3d3;
} */

.navbar__item__icon {
  font-size: 1.5rem;
  /* margin-right: 10px; */
}

.navbar__item__text {
  font-size: 1rem;
  font-weight: bold;
}
@media only screen and (max-width: 767px) {
  .navbar {
    right: 15px;
    padding: 10px;
  }

  .navbar__item {
    padding: 8px 12px;
    margin-bottom: 8px;
  }

  .navbar__item__icon {
    font-size: 1.2rem;
    margin-right: 8px;
  }

  .navbar__item__text {
    font-size: 0.9rem;
  }
}
</style>
