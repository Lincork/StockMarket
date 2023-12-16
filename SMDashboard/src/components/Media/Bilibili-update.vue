<template>
  <el-carousel indicator-position="outside" :interval="4000" arrow="always">
    <el-carousel-item v-for="(item, index) in carouselItems" :key="index">
      <img :src="item.imageUrl" alt="">
      <h3 text="2xl" justify="center">Main Video {{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<script>

export default {
  name: "Bilibili Update",
  data() {
    return {
      carouselItems: [
        { imageUrl: 'https://i1.hdslb.com/bfs/archive/a485151d2292beb553f706e6f7b1546e0f6664cf.jpg@518w_290h_1c_!web-video-share-cover.avif' },
        { imageUrl: 'https://i0.hdslb.com/bfs/archive/36122c1f9ff3360b55ea0825d0833566ddfc41fe.jpg@518w_290h_1c_!web-video-share-cover.avif' },
        { imageUrl: 'https://i0.hdslb.com/bfs/archive/be19301f98d76a09c7739f1ecbb580df7cd90947.jpg@518w_290h_1c_!web-video-share-cover.avif' },
        // 添加更多图片项...
      ]
    };
  }
};
</script>

<style scoped>

</style>