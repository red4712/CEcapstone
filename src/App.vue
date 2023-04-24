<template>
  <Header></Header>
  <Nav></Nav>
  <Image></Image>
  <List></List>
  <Card></Card>
  <Main1></Main1>
  <MapKakao :latitude="37.39843974939604" :longitude="127.10972941510465" />
  <Footer></Footer>
</template>
<script>
import Header from "./components/Header";
import Main1 from "./components/Main1";
import Footer from "./components/Footer";
import Card from "./components/Card";
import Image from "./components/Image";
import List from "./components/List";
import Nav from "./components/Nav";
import MapKakao from "./components/MapKakao";
export default {
  components: {
    Header,
    Main1,
    Footer,
    Card,
    Image,
    List,
    Nav,
    MapKakao,
  },
};
</script>

<style></style>
