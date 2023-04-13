<template>
  <div>
  <Header></Header>
  <Image></Image>
  <Main1></Main1>
  <Card></Card>
  <Footer></Footer>
  </div>
</template>
<script>
import Header from './components/Header'
import Main1 from './components/Main1'
import Footer from './components/Footer'
import Card from './components/Card'
import Image from './components/Image'
export default {
  components: {
    Header, 
    Main1,
    Footer,
    Card,
    Image,
  },
}
</script>

<style>

</style>