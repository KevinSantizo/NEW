import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Companies from './views/Companies'
import Reserve from './views/Reserve'
import DoReserve from './views/DoReserve'
import Login from './views/Login'
import Register from './views/Register'
import InfoCompany from '@/views/InfoCompany'
import Reservation from '@/views/Reservation'
import Account from '@/views/Account'
import Test from '@/views/Test'
import Logout from '@/views/Logout.vue'


Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { 
      path: '/', 
      name: 'login', 
      component: Login,  

    },
    { 
      path: '/home', 
      name: 'home', 
      component: Home 
    },
    { 
      path: '/companies', 
      name: 'companies', 
      component: Companies 
    },
    { 
      path: '/reserve', 
      name: 'reserve', 
      component: Reserve 
    },
    { 
      path: '/do_reserve/:companyId/reserve', 
      name: 'do_reserve', 
      component: DoReserve 
    },
    { 
      path: '/register', 
      name:'register', 
      component: Register
    },
    { 
      path:'/companies/:companyId/info', 
      name:'InfoCompany', 
      component: InfoCompany
    },
    { 
      path:'/field/:fieldId/reservar', 
      name:'Reservation', 
      component: Reservation
    },
    { 
      path:'/account', 
      name: 'account', 
      component: Account
    },
    { 
      path:'/test', 
      name: 'test',  
      component: Test
    },
    { 
      path: '/logout', 
      name: 'logout', 
      component: Logout 
    },
  ]
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/') 
  } else {
    next() 
  }
})
export default router
