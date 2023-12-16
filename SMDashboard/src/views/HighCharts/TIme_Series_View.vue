<template>
  <div class="element-card">
    <el-card shadow="hover">
      <Large_Dataset></Large_Dataset>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Zoomable></Zoomable>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Irregular_Intervals></Irregular_Intervals>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Plot_Bands></Plot_Bands>
    </el-card>
  </div>
</template>

<script>
import Large_Dataset from "../../components/Charts/Time_Series/Large_Dataset.vue";
import Zoomable from "../../components/Charts/Time_Series/Zoomable.vue";
import Irregular_Intervals from "../../components/Charts/Time_Series/Irregular_Intervals.vue";
import Plot_Bands from "../../components/Charts/Time_Series/Plot_Bands.vue";
export default {
  name: "app",
  components: {
    Large_Dataset,
    Zoomable,
    Irregular_Intervals,
    Plot_Bands,
  }
};
</script>

<style scoped>
.element-card {
  display: grid;
  place-items: center;
}

</style>