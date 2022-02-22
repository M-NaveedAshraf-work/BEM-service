import Vue from 'vue'
import VueRouter from 'vue-router'
import Input from '../components/Input.vue'
import CapX from '../components/CapX_Cal.vue'
import UQ from '../components/UQ.vue'
import Output from '../components/Output.vue'
import 'echarts'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Input',
    component: Input
  },
  {
    path: '/CapX_Cal',
    name: 'CapX_Cal',
    component: CapX
  },
  {
    path: '/UQ',
    name: 'UQ',
    component: UQ
  },
  {
    path: '/Output',
    name: 'Output',
    component: Output
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
