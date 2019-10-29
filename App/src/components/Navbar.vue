<template>
    <nav>
        <v-app-bar flat text app class="grey lighten-4" height="57" >
            <v-row justify="center" align="center">
                <v-toolbar-title class="grey--text">
                    <span class="black--text font-weight-bold" dense>¡Bienvenido!</span>
                    <img src="@/assets/ball.svg" alt="" style="width: 35px;">
                </v-toolbar-title>
            </v-row>
        </v-app-bar>
    </nav>
</template>


<script>
    export default {
        data() {
            return {
            drawer: false,
            item: 1,
            items : [
                {title: 'Inicio', icon: 'mdi-view-dashboard', route: '/home'},
                {title: 'Mis Reservaciones', icon: 'mdi-calendar', route: '/reservations'},
                {title: 'Compañías', icon: 'mdi-domain', route: '/companies'},
                {title: 'Mis Partidos', icon:'mdi-soccer'},
                {title: 'Mi Perfil', icon: 'mdi-account', route: '/account'},
                {title: 'Configuración', icon: 'mdi-settings-box', route: '/settings'}
            ],
            }
        },
    }
</script>


<style scoped>
.link{
      text-decoration:  none;
   }
</style>