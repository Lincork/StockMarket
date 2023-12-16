<template>
  <div class="element-card">
    <el-card shadow="hover">
      <Multil_Data></Multil_Data>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Symbols></Symbols>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Inverted_Axes></Inverted_Axes>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Data_Labels></Data_Labels>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Logarithmic_Axis></Logarithmic_Axis>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Entrance_Animation></Entrance_Animation>
    </el-card>
  </div>
  <div class="element-card">
    <el-card shadow="hover">
      <Clickable_Points></Clickable_Points>
    </el-card>
  </div>
</template>

<script>
import Multil_Data from "../../components/Charts/Line/Multil_Data.vue";
import Symbols from "../../components/Charts/Line/Symbols.vue";
import Inverted_Axes from "../../components/Charts/Line/Inverted_Axes.vue";
import Data_Labels from "../../components/Charts/Line/Data_Labels.vue";
import Logarithmic_Axis from "../../components/Charts/Line/Logarithmic_Axis.vue";
import Entrance_Animation from "../../components/Charts/Line/Entrance_Animation.vue";
import Clickable_Points from "../../components/Charts/Line/Clickable_Points.vue";

export default {
  name: "app",
  components: {
    Multil_Data,
    Symbols,
    Inverted_Axes,
    Data_Labels,
    Logarithmic_Axis,
    Entrance_Animation,
    Clickable_Points
  }
};
</script>

<style scoped>
.element-card {
  display: grid;
  place-items: center;
}

</style>