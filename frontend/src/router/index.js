import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Results from '../views/Results.vue'
// import GoogleMap from '../views/GoogleMap.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:scenario/:state',
    name: 'results',
    component: Results
  }
  // {
  //   path: '/:scenario/:feature/:state',
  //   name: 'map',
  //   component: GoogleMap,
  //   props: route => ({ data: route.params.data })
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
