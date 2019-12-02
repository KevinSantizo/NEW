<template> 
<v-container height="100%" style="top: 10em; position: relative;">
    <v-row justify="center">
        <span class="display-1 font ">Iniciar Sesión</span>
    </v-row>
        <v-divider></v-divider>
    <v-form  ref="form" class="ma-8 font" @submit.prevent="login" id="login-form">
        <v-text-field outlined class="input-group--focused font" v-model="username" label="Nombre de Usuario" required></v-text-field>
        <v-text-field outlined class=" font" @click:append="show3 = !show3" v-model="password" label="Contraseña" required :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'" :type="show3 ? 'text' : 'password'"></v-text-field>
        <v-btn type="submit" dark :elevation=10 form="login-form" block color="light-green accent-4" class="font link mr-4" >INICIA SESIÓN</v-btn>     
    </v-form>
        <v-divider></v-divider>
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
</v-container>
</template>


<script>
  import { mdbInput, mdbBtn } from 'mdbvue';
    export default {
         name: 'Basic',
            components: {
            mdbInput,
            mdbBtn
            },
         data (){
             return {
                username: '',
                password: '',
                show2: true,
                   rules: {
                    required: value => !!value || "Field required",
                    min: value => value.length >= 4 || "Minimum 4 characters",
                },
                show3: false,
                isSwitch: false,
             }
    },

    methods: {
        login (){
            let username = this.username
            let password = this.password
            this.$store.dispatch('login', { username, password })
            .then(() => window.location.href = "/home")
            .catch(err => alert('Usuario y/o contraseña inválidos')+ err)
      },
          /*getToken() {
              alert('token'
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
