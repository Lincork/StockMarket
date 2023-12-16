<template>
    <el-row :gutter="5">
      <el-col :span="12"><div class="grid-content ep-bg-purple" />
          <Bilibili></Bilibili>
      </el-col>

      <el-col :span="12"><div class="grid-content ep-bg-purple" />
        <el-row :gutter="5">
          <el-col :span="6">
            <h3 text="2xl" justify="center">Video 1</h3>
          </el-col>
          <el-col :span="6">
            <h3 text="2xl" justify="center">Video 2</h3>
          </el-col>
        </el-row>

        <el-row :gutter="5">
          <el-col :span="6">
            <h3 text="2xl" justify="center">Video 3</h3>
          </el-col>
          <el-col :span="6">
            <h3 text="2xl" justify="center">Video 4</h3>
          </el-col>
        </el-row>

      </el-col>

    </el-row>

</template>

<script>
import Bilibili from '../../components/Media/Bilibili-update.vue'

export default {
  name: "app",
  components: {
    Bilibili,
  }
};
</script>

<style scoped>


</style>