<template>
    <v-container class="indigo lighten-5"  style="height: 100%; width: 100%;">
            <div class="form-group ma-2">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                    <v-divider class="my-3"></v-divider>
                            <v-form ref="form" v-model="form" >
                                <v-row class="form1">
                                <v-col cols="12" sm="6">
                                <v-text-field color="black" label="Nombres" type="text" class="form1" placeholder ="Ingresa tus nombres" outlined  autofocus></v-text-field>
                                </v-col>
                            <v-col cols="12" sm="6" class="form1">
                            <v-text-field color="black" label="Apelidos" type="text"  class="form1"  placeholder="Ingresa tus apellidos " outlined></v-text-field>
                            </v-col>
                            </v-row>
                            <v-text-field color="black" label="Teléfono" type="text" class="form"  placeholder="Ingresa tu teléfono " outlined></v-text-field>
                            <v-text-field color="black" label="Email" type="email" class="form"  placeholder="Ingresa tu email " outlined></v-text-field>
                            <v-text-field color="black" label="Contraseña" type="password" class="form"  placeholder="Crea tu contraseña " outlined></v-text-field>

                            <v-btn block  color="light-green accent-4 white--text" >CREAR MI CUENTA</v-btn>          
                        </v-form>
                <template>
                    <v-row justify="center" align="center" class="my-1">
                        <div>
                        <span class="caption">¿Ya tienes una cuenta? </span>
                        </div>
                        <v-divider inset vertical class="mx-1"></v-divider>
                        <div>
                        <router-link class="caption" :to="{name: 'login'}"><span>Inicia Sesión</span></router-link>
                        </div>
                    </v-row>
                    <v-row justify="center" align="center" class="my-1">
                        <img src="@/assets/ball.svg" alt="" style="width: 35px;">
                    </v-row>
                </template>
            </div>
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
.form {
   margin-top: 0em;
}

.form1 {
    margin-top: -0.5em;
}

</style>
