<template>
  <div class="card-container">
    <div class="card">
      <div class="card__image">
        <img src="../assets/card1.png" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">Game 1</h2>
        <p class="card__description">
          Description for Game 1
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/card2.png" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">Game 2</h2>
        <p class="card__description">
          Description for Game 2
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/card3.png" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">Game 3</h2>
        <p class="card__description">
          Description for Game 3
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
    <div class="card">
      <div class="card__image">
        <img src="../assets/card4.png" alt="card image" />
      </div>
      <div class="card__content">
        <h2 class="card__title">Game 4</h2>
        <p class="card__description">
          Description for Game 4
        </p>
        <a href="#" class="card__button">Learn More</a>
      </div>
    </div>
  </div>
</template>
<style>
.card {
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
  font-size: 1.4rem;
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