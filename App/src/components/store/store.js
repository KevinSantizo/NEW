import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import swal from 'sweetalert'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user: {},
    },
    mutations: {
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.token = ''
        },
    },
    actions:{
        login({commit}, user){
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url: 'https://api-backend-canchas.herokuapp.com/api/api-token-auth/', data: user, method: 'POST' })
                .then(resp => {
                  const token = resp.data.token
                  var base64Url = token.split('.')[1];
                  var base64 = base64Url.replace('-', '+').replace('_', '/');
                  console.log(JSON.parse(window.atob(base64)))        
                  const user = resp.data.user
                  localStorage.setItem('token', token)
                  localStorage.setItem('user.id', JSON.parse(window.atob(base64)))
                  axios.defaults.headers.common['Authorization'] = token
                  commit('auth_success', token, user)
                  resolve(resp)
                }) .catch(err => {
                    commit('auth_error')
                    localStorage.removeItem('token')
                    reject(err)
            })
        })
    },
    register({commit}, user){
        return new Promise((resolve, reject) => {
          commit('auth_request')
          axios({url: 'https://api-backend-canchas.herokuapp.com/api/users/', data: user, method: 'POST' })
          .then(resp => {
            const user = resp.data.user
            commit('auth_success', user)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            reject(err)
          })
        })
    },
    reservation({commit}, res){
        return new Promise((resolve, reject) => {
          commit('auth_request')
          axios({url: 'https://api-backend-canchas.herokuapp.com/api/do-reservation/', data: res, method: 'POST' })
          .then(resp => {
            const res = resp.data.res
            commit('auth_success', res)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            reject(err)
          })
        })
    },
    logout(context){
        if(context.getters.isLoggedIn){
          return new Promise((resolve, reject) => {
                localStorage.removeItem('token')
                context.commit('logout')
                resolve()    
              })
              .catch(err => {
                localStorage.removeItem('token')
                context.commit('logout')
                reject(err)
              })
        }
      },
    },
      getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    },
})
