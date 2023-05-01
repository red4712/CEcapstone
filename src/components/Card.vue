<template>
  <div class="card-container">
    <div class="card">
      <div class="card__image">
        <img src="../assets/유달산.jpg" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">유달산</h2>
        <p class="card__description">
          전라남도 목포시에 위치한 해안산으로, 해돋이와 해물먹는 명소로 유명합니다.
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/케이블카.jpg" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">케이블카</h2>
        <p class="card__description">
          유달산과 한산도를 연결하는 케이블카로, 목포에서 가장 높은 곳에서 한산도를 바라볼 수 있습니다.
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/해양레저.jpg" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">해양레저</h2>
        <p class="card__description">
          바다 위에서 즐기는 스포츠 및 레저 활동으로, 수상스키, 제트스키, 패들보드 등이 포함됩니다.
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/바다분수.jpg" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">바다분수</h2>
        <p class="card__description">
          바다에서 일정 높이까지 물을 분출하는 인공 분수로, 목포를 대표하는 관광명소 중 하나입니다.
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
  </div>
</template>
<style>
.card {
  width: 300px;
  height: 200px;
  margin-left: 20px;
  margin-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 25rem;
  background-color: #fff;
  border-radius: 1rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  transition: box-shadow 0.2s ease-in-out;
}

.card:hover {
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.5);
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between; /* 옵션 */
}
.card__image {
  height: 15rem;
  width: 100%;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  overflow: hidden;
}

.card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card__content {
  padding: 2rem;
  text-align: center;
}

.card__title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.card__description {
  font-size: 0.9rem;
  margin-bottom: 2rem;
}

.card__button {
  background-color: #1d1d1d;
  color: #fff;
  padding: 1rem 2rem;
  border: none;
  border-radius: 2rem;
  font-size: 1.6rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.card__button:hover {
  background-color: #fff;
  color: #1d1d1d;
}</style>