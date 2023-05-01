<template>
  <div class="place-list">
    <h2>관광지 목록</h2>
    <ul>
      <li v-for="place in places" :key="place.id" class="place-item">
        <div class="place-content">
          <h3 class="place-name">{{ place.name }}</h3>
          <div class="place-image-container">
            <img :src="place.image" alt="place.name" class="place-image" />
          </div>
        </div>
        <p class="place-description">{{ place.description }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      places: [
        {
          id: 1,
          name: "마리나",
          description:
            "야외 캐주얼 카페와 유니크한 디자인의 야외편의시설을 갖춘 신개념 마리나",
          image: require("@/assets/마리나.jpg"),
        },
        {
          id: 2,
          name: "오동도",
          description:
            "오동도에는 다양한 해산물과 전통음식을 맛볼 수 있는 맛집들이 즐비하다.",
          image: require("@/assets/오동도.jpg"),
        },
        {
          id: 3,
          name: "유리의 성",
          description: "오리지널 유리 소품으로 가득 찬 독특한 분위기의 카페",
          image: require("@/assets/유리의성.jpg"),
        },
      ],
    };
  },
};
</script>

<style scoped>
.place-list {
  background-color: #fff;
  color: #fff;
  padding: 20px;
  border-radius: 10px;
}

.place-item {
  margin-bottom: 20px;
  padding: 20px;
  background-color: #2f2f2f;
  border-radius: 10px;
  display: flex;
  flex-direction: row;
}

.place-name {
  margin: 0;
  font-size: 24px;
  margin-bottom: 10px;
}

.place-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-right: 20px;
}

.place-image-container {
  width: 200px;
  height: 150px;
  border-radius: 10px;
  overflow: hidden;
}

.place-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.place-description {
  margin: 0;
  font-size: 16px;
  line-height: 1.5;
  color: #ddd;
}
</style>