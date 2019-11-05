<template>
    <v-container height="100%">
        <v-row justify="center" align="center" >
            <div class="form-group ma-6 pa-12">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> INICIA SESIÓN CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> INICIA SESIÓN CON GOOGLE</v-btn>
                <v-divider class="my-3"></v-divider>
                    <div>
                        <form>
                            <span for="email" class="font body-2">E-mail</span>
                            <input class="form-control transparent my-2 font body-2" type="text" id="email" placeholder="Ingrese su email" style="border: 1px solid grey !important;">
                            <span for="password" class="font body-2">Contraseña</span>
                            <input class="form-control  transparent my-2 font body-2" type="text" id="password" placeholder="Ingrese su contraseña" style="border: 1px solid grey !important;">
                            <v-btn block  color="light-green accent-4 white--text" class="font link my-3" router to="/home" >INICIA SESIÓN</v-btn>          
                        </form>
                        <v-row justify="center" align="center" class="my-1">
                            <router-link class="caption my-2 font" :to="{name: 'companies'}">¿Olvidaste tu contraseña?</router-link>
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
                        <router-link class="caption font" :to="{name: 'register'}"><span> Regístrate</span></router-link>
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
    export default {
         data: () => ({
      loading: false,
      selection: 1,
    }),

    methods: {
      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
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
