<template>
  <div>
  <Header></Header>
  <Main1></Main1>
  <About></About>
  <Card></Card>
  <Footer></Footer>
  </div>
</template>
<script>

import Header from './components/Header'
import Main1 from './components/Main1'
import About from './components/About'
import Footer from './components/Footer'
import Card from './components/Card'
export default {
  components: {
    Header, 
    Main1,
    About,
    Footer,
    Card,

  },
}
</script>

<style>

</style>