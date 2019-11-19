<template>
    <v-container height="100%">
        <v-row justify="center" align="center" >
            <div class="form-group ma-6 pa-12">
                <v-btn class="my-3"  block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> INICIA SESIÓN CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> INICIA SESIÓN CON GOOGLE</v-btn>
                <v-divider class="my-3"></v-divider>
                    <div>
                        <form @submit.prevent="login" id="login-form">
                            <span for="username" class="font body-2">Username</span>
                            <input class="form-control transparent my-2 font body-2" autofocus type="text" v-model="username" name="username"   id="username" required placeholder="Ingrese su nombre de usuario" style="border: 1px solid grey !important;">
                            <span for="password" class="font body-2">Contraseña</span>
                            <input class="form-control  transparent my-2 font body-2" autofocus type="password" v-model="password" name="password" id="password" required placeholder="Ingrese su contraseña" style="border: 1px solid grey !important;">
                            <v-btn type="submit" form="login-form" block color="light-green accent-4 white--text" class="font link my-3" >INICIA SESIÓN</v-btn>          
                        </form>     
                        <v-row justify="center" align="center" class="my-1">
                           <!-- <router-link class="caption my-2 font">¿Olvidaste tu contraseña?</router-link>-->
                        </v-row>
                        <v-divider></v-divider>
                    </div>
                <template>
                    <v-row justify="center" align="center" class="my-1">
                        <div>
                        <span class="caption font">¿Aún no tienes cuenta? </span>
                        </div>
                        <v-divider inset vertical class="mx-1"></v-divider>
                        <div>
                        <router-link class="caption font"  :to="{name: 'register'}"><span> Regístrate</span></router-link>
                        </div>
                    </v-row>
                    <v-row justify="center" align="center" class="my-1">
                        <img src="@/assets/ball.svg" alt="" style="width: 35px;">
                    </v-row>
                </template>
            </div>
        </v-row>
    </v-container>
</template>


<script>
    import axios from 'axios'
    export default {
         data (){
             return {
                username: '',
                password: '',

             }
    },

    methods: {
        login (){
            let username = this.username
            let password = this.password
            this.$store.dispatch('login', { username, password })
            .then(() => this.$router.push('/home'))
            .catch(err => alert('Usuario y/o contraseña inválidos'))
      },
          /*getToken() {
              alert('token')
              const path = 'http://192.168.88.222:8000/api-token-auth/'
              axios.post(path, this.form).then((response) =>{
                  this.token = response.data
                  console.log(token);
              })
          },
          created(){
              this.getToken()
          },*/
      },
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
.form {
   margin-top: 0em;
}
.link {
    text-decoration: none;
}
</style>
