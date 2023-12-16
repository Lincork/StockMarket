import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import { usePermissStore } from '../store/permiss';
import Home from '../views/Other/home.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/dashboard',
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/dashboard',
                name: 'dashboard',
                meta: {
                    title: '系统首页',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/Dashboard/dashboard.vue'),
            },
            {
                path: '/table',
                name: 'basetable',
                meta: {
                    title: '表格',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "table" */ '../views/Other/table.vue'),
            },
            {
                path: '/charts',
                name: 'basecharts',
                meta: {
                    title: '图表',
                    permiss: '11',
                },
                component: () => import(/* webpackChunkName: "charts" */ '../views/Other/charts.vue'),
            },
            {
                path: '/form',
                name: 'baseform',
                meta: {
                    title: '表单',
                    permiss: '5',
                },
                component: () => import(/* webpackChunkName: "form" */ '../views/Other/form.vue'),
            },
            {
                path: '/notification',
                name: 'notification',
                meta: {
                    title: '消息中心',
                    permiss: '3',
                },
                component: () => import(/* webpackChunkName: "tabs" */ '../views/Other/tabs.vue'),
            },
            {
                path: '/donate',
                name: 'donate',
                meta: {
                    title: '鼓励作者',
                    permiss: '14',
                },
                component: () => import(/* webpackChunkName: "donate" */ '../views/Other/donate.vue'),
            },
            {
                path: '/permission',
                name: 'permission',
                meta: {
                    title: '权限管理',
                    permiss: '13',
                },
                component: () => import(/* webpackChunkName: "permission" */ '../views/Other/permission.vue'),
            },
            {
                path: '/upload',
                name: 'upload',
                meta: {
                    title: '上传插件',
                    permiss: '6',
                },
                component: () => import(/* webpackChunkName: "upload" */ '../views/Other/upload.vue'),
            },
            {
                path: '/icon',
                name: 'icon',
                meta: {
                    title: '自定义图标',
                    permiss: '10',
                },
                component: () => import(/* webpackChunkName: "icon" */ '../views/Other/icon.vue'),
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '个人中心',
                },
                component: () => import(/* webpackChunkName: "user" */ '../views/Other/user.vue'),
            },
            {
                path: '/editor',
                name: 'editor',
                meta: {
                    title: '富文本编辑器',
                    permiss: '8',
                },
                component: () => import(/* webpackChunkName: "editor" */ '../views/Other/editor.vue'),
            },
            {
                path: '/markdown',
                name: 'markdown',
                meta: {
                    title: 'markdown编辑器',
                    permiss: '9',
                },
                component: () => import(/* webpackChunkName: "markdown" */ '../views/Other/markdown.vue'),
            },
            {
                path: '/export',
                name: 'export',
                meta: {
                    title: '导出Excel',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "export" */ '../views/Other/export.vue'),
            },
            {
                path: '/import',
                name: 'import',
                meta: {
                    title: '导入Excel',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/Other/import.vue'),
            },
            {
                path: '/global',
                name: 'import',
                meta: {
                    title: '宏观分析',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/Global/Global.vue'),
            },
            {
                path: '/charts-line',
                name: 'LineCharts',
                meta: {
                    title: '线性图',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/StockAnalysis/Stock.vue'),
            },
            {
                path: '/industries',
                name: '申万行业分类',
                meta: {
                    title: '申万行业分类',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/Industries/Industries.vue'),
            },
            {
                path: '/news',
                name: '新闻热点',
                meta: {
                    title: '新闻热点',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/News/News.vue'),
            },
            {
                path: '/media',
                name: '视频更新',
                meta: {
                    title: '视频更新',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/News/Media.vue'),
            },
            {
                path: '/data',
                name: '数据中心',
                meta: {
                    title: '数据中心',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/DataCenter/DataCenter.vue'),
            },
            {
                path: '/stock',
                name: '股票分析',
                meta: {
                    title: '股票分析',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "import" */ '../views/StockAnalysis/Stock.vue'),
            },
            {
                path: '/highcharts-line',
                name: 'Line Charts',
                meta: {
                    title: '折线图',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/HighCharts/Line_View.vue'),
            },
            {
                path: '/highcharts-timeseries',
                name: 'Time Series Data',
                meta: {
                    title: '时间序列',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "dashboard" */ '../views/HighCharts/TIme_Series_View.vue'),
            },

        ],
    },
    {
        path: '/login',
        name: 'Login',
        meta: {
            title: '登录',
        },
        component: () => import(/* webpackChunkName: "login" */ '../views/Login/login.vue'),
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/Exception/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | vue-manage-system`;
    const role = localStorage.getItem('ms_username');
    const permiss = usePermissStore();
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permiss && !permiss.key.includes(to.meta.permiss)) {
        // 如果没有权限，则进入403
        next('/403');
    } else {
        next();
    }
});

export default router;
