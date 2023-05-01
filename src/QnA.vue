<template>
  <Header></Header>
  <Nav></Nav>
  <div>
    <h1 style="text-align:center">자주 묻는 질문</h1>
    <ul class="que_ul">
      <li class="que_li" v-for="faq in faqs" :key="faq.id" @click="toggleAnswer(faq)">
        <h2 class="que">{{ faq.question }}</h2>
        <p class="ans" v-if="faq.showAnswer">{{ faq.answer }}</p>
      </li>
    </ul>
  </div>
  <Footer></Footer>
</template>
<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Nav from "./components/Nav.vue";

export default {
  components: {
    Header,
    Footer,
    Nav,
  },
  name: "Faq",

  data() {
    return {
      faqs: [
        {
          id: 1,
          question: "Q. 시간 제한이 있나요?",
          answer:
            "A. 시간 제한은 없습니다. 다만, 게임 진행시 안전을 위해 일몰 전 게임을 마무리 하셔야 합니다",
          showAnswer: false,
        },
        {
          id: 2,
          question: "Q. 게임을 하려면, 핸드폰 혹은 인터넷 연결이 필요한가요?",
          answer:
            "A. 대부분 미션은 핸드폰에서 웹을 연결해 미션과 이동장소가 전달됩니다. 넉넉한 핸드폰 배터리와 인터넷 연결이 반드시 필요합니다.",
          showAnswer: false,
        },
        {
          id: 3,
          question: "Q. 나이 제한이 있나요?",
          answer:
            "A. 나이 제한은 없지만, 10세 미만의 아동 혹은 고연령대의 성인은 동반자 없이 혼자 문제 풀기가 어려울 수 있습니다.",
          showAnswer: false,
        },

        {
          id: 4,
          question: "Q. 몬스터를 잡지 못했어요. 어떻게 해야 하나요?",
          answer:
            "A. 몬스터를 잡을때마다 힌트를 제공해 드리고 있습니다. 몬스터를 잡지 못할 경우, 힌트를 보신다면 정답에 가까운 답을 아실 수 있어요. 단, 감점이 있다는 사실은 기억해 두세요..",
          showAnswer: false,
        },

        {
          id: 5,
          question:
            "Q. 목포시에서 가장 유명한 음식은 무엇인가요? 추천할만한 맛집이 있나요?",
          answer:
            'A. 목포시에서 가장 유명한 음식은 "모둠전"입니다. 모둠전은 여러 가지 해산물과 야채 등을 고추장으로 맛을 낸 뒤 부침에 튀겨서 먹는 음식입니다. 그 외에도 목포시는 해산물이 풍부한 지역이기 때문에 매운탕, 홍합, 조개, 회 등의 해산물 요리도 많이 먹힙니다. 추천할 만한 맛집으로는 "목포 미술관 식당"이 있습니다. 이곳에서는 전통적인 모둠전을 비롯하여 다양한 해산물 요리를 즐길 수 있습니다. 또한, "목포 매운탕 골목"에서는 목포 매운탕 전문점들이 모여 있어 매콤한 해산물 맛을 즐길 수 있습니다.',
          showAnswer: false,
        },
      ],
    };
  },

  methods: {
    toggleAnswer(faq) {
      faq.showAnswer = !faq.showAnswer;
    },
  },
};
</script>
<style scoped>
.que_ul {
  list-style: none;
  padding: 20;
}

.que_li {
  border-radius: 20px;
  margin-bottom: 20px;
  padding: 20px;
  margin-bottom: 2rem;
  cursor: pointer;
  background: gray;
  margin-right:100px;
  margin-left:100px;
}

.que {
  font-size: 14pt;
  margin-bottom: 1rem;
  text-align: center;
  color: black;
}

.ans {
  font-size: 15pt;
  /* line-height: 1; */
  text-align: center;
  color: black;
}
</style>
