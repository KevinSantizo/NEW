import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || null,
        user: localStorage.getItem('user') || null,
    },
    mutations: {
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
                axios({url: 'http://192.168.88.222:8000/api/api-token-auth/', data: user, method: 'POST' })
                .then(async (resp) => {
                  const parseResponde = await resp.data
                  const token = parseResponde.token
                  var base64Url = token.split('.')[1];
                  var base64 = base64Url.replace('-', '+').replace('_', '/');
                  console.log(JSON.parse(window.atob(base64)))        
                  const user = JSON.parse(window.atob(base64)).user_id
                  console.log(user, 'ID USUARIO')
                  localStorage.setItem('token', token)
                  localStorage.setItem('user', user)
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
          axios({url: 'http://192.168.88.222:8000/api/users/', data: user, method: 'POST' })
          .then(resp => {
          const token = resp.data.token
          const user = resp.data.user
          localStorage.setItem('token', token)
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user)
          resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
        })
    },
    reservation({commit}, res){
        return new Promise((resolve, reject) => {
        axios({url: 'http://192.168.88.222:8000/api/make-reservation/', data: res, method: 'POST' })
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
    logout({commit}){
      return new Promise((resolve) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    },
    },
      getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    },
})
