<template>
    <div class="sidebar">
        <el-menu
            class="sidebar-el-menu"
            :default-active="onRoutes"
            :collapse="sidebar.collapse"
            background-color="#dddddd"
            text-color="#53687d"
            active-text-color="#015788"
            unique-opened
            router
        >
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-sub-menu :index="item.index" :key="item.index" v-permiss="item.permiss">
                        <template #title>
                            <el-icon>
                                <component :is="item.icon"></component>
                            </el-icon>
                            <span>{{ item.title }}</span>
                        </template>
                        <template v-for="subItem in item.subs">
                            <el-sub-menu
                                v-if="subItem.subs"
                                :index="subItem.index"
                                :key="subItem.index"
                                v-permiss="item.permiss"
                            >
                                <template #title>{{ subItem.title }}</template>
                                <el-menu-item v-for="(threeItem, i) in subItem.subs" :key="i" :index="threeItem.index">
                                    {{ threeItem.title }}
                                </el-menu-item>
                            </el-sub-menu>
                            <el-menu-item v-else :index="subItem.index" v-permiss="item.permiss">
                                {{ subItem.title }}
                            </el-menu-item>
                        </template>
                    </el-sub-menu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index" :key="item.index" v-permiss="item.permiss">
                        <el-icon>
                            <component :is="item.icon"></component>
                        </el-icon>
                        <template #title>{{ item.title }}</template>
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useSidebarStore } from '../store/sidebar';
import { useRoute } from 'vue-router';

const items = [
    {
        icon: 'Odometer',
        index: '/dashboard',
        title: '数据总览',
        permiss: '2',
    },
    {
        icon: 'PieChart',
        index: '/global',
        title: '宏观经济',
        permiss: '2',
    },
    {
        icon: 'grid',
        index: '/industries',
        title: '行业研究',
        permiss: '2',
    },
    {
        icon: 'DocumentCopy',
        index: '/news',
        title: '新闻热点',
        permiss: '2',
        subs: [
          {
            index: '/news',
            title: '实时资讯',
            permiss: '5',
          },
          {
            index: '/media',
            title: '视频更新',
            permiss: '5',
          },
        ]
    },
    {
        icon: 'grid',
        index: '/data',
        title: '数据中心',
        permiss: '2',
    },
    {
        icon: 'rank',
        index: '/stock',
        title: '股票分析',
        permiss: '5',
    },
    {
        icon: 'rank',
        index: '/highcharts',
        title: 'Highcharts',
        permiss: '5',
        subs: [
          {
            index: '/highcharts-line',
            title: '折线图',
            permiss: '5',
          },
          {
            index: '/highcharts-timeseries',
            title: '时间序列',
            permiss: '5',
          },
        ]
    },
      {
        icon: 'Setting',
        index: '/icon',
        title: '设置',
        permiss: '10',
    },

];

const route = useRoute();
const onRoutes = computed(() => {
    return route.path;
});

const sidebar = useSidebarStore();
</script>

<style scoped>
.sidebar {
    display: block;
    position: absolute;
    left: 0;
    top: 50px;
    bottom: 0;
    overflow-y: scroll;

}
.sidebar::-webkit-scrollbar {
    width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
    width: 180px;
}
.sidebar > ul {
    height: 100%;
    background: #dddddd;
}
</style>
