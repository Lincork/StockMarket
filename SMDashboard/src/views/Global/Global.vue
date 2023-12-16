<template>
  <div class="element-card">
    <el-card shadow="hover">
      <TimeSeries></TimeSeries>
    </el-card>
  </div>
</template>

<script>
import TimeSeries from '../../components/Charts/Time_Series/Zoomable.vue'

export default {
  name: "app",
  components: {
    TimeSeries,
  }
};
</script>

<style scoped>
.element-card {
  display: grid;
  place-items: center;
}

</style>