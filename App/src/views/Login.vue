<template>
    <v-container class="indigo lighten-5" style="height: 100%; width: 100%;">
        <v-row justify="center" align="center" class="my-1 " >
            <div class="form-group ma-6 pa-10">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> INICIA SESIÓN CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> INICIA SESIÓN CON GOOGLE</v-btn>
                <v-divider class="my-3"></v-divider>
                    <div class="form-group ">
                        <v-form ref="form" v-model="form" class="form">
                            <v-text-field color="black" label="Email" type="email" placeholder ="Ingresa tu email" outlined height=5 autofocus></v-text-field>
                            <v-text-field color="black" label="Password" type="password" placeholder="Ingresa tu contraseña" outlined></v-text-field>
                            <v-btn block  color="light-green accent-4 white--text" class="link" router to="/home" >INICIA SESIÓN</v-btn>          
                        </v-form>
                        <v-row justify="center" align="center" class="my-1">
                            <router-link class="caption my-2" :to="{name: 'companies'}">¿Olvidaste tu contraseña?</router-link>
                        </v-row>
                        <v-divider></v-divider>
                    </div>
                <template>
                    <v-row justify="center" align="center" class="my-1">
                        <div>
                        <span class="caption">¿Aún no tienes cuenta? </span>
                        </div>
                        <v-divider inset vertical class="mx-1"></v-divider>
                        <div>
                        <router-link class="caption " :to="{name: 'register'}"><span> Regístrate</span></router-link>
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

.link {
    text-decoration: none;
}
</style>
