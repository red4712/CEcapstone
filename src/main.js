import { createApp } from 'vue'
import App from './App.vue'
import About from './About.vue'
import QnA from './QnA.vue'
import Board from './Board.vue'
import AR from './AR.vue'
import Game from './Game.vue'

createApp(App).mount('#app') 
createApp(About).mount('#About')
createApp(QnA).mount('#QnA')
createApp(Board).mount('#Board')
createApp(AR).mount('#AR')
createApp(Game).mount('#Game')