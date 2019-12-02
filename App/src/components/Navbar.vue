<template>
   <nav>
       <v-app-bar flat text app class="grey lighten-4" height="57" >
           <v-app-bar-nav-icon class="dark" color="black" @click="drawer = !drawer"></v-app-bar-nav-icon>
           <v-toolbar-title class="grey--text">
               <span class="black--text font-weight-bold" dense>¡Welcome!</span>
               <img src="@/assets/ball.svg" alt="" style="width: 35px; position: absolute;">
           </v-toolbar-title>
           <v-spacer></v-spacer>
           <v-btn text color="grey">
               <span dense class="black--text font-weight-bold">Sign Out</span>
               <v-icon right color="black">mdi-exit-to-app</v-icon>
           </v-btn>
       </v-app-bar>

       <v-navigation-drawer dense app v-model="drawer"  temporary class="grey lighten-4" height="100%">
           <template v-slot:prepend>
               <v-list-item> 
                   <v-list-item-avatar> 
                        <img src="@/assets/apitec.png" alt="">
                    </v-list-item-avatar>  
                    <v-list-item-content>
                        <v-list-item-title  class="font-weight-medium title black--text">Apitec</v-list-item-title>
                    </v-list-item-content>
                    <v-btn icon @click="drawer = !drawer">
                     <v-icon color="grey">mdi-chevron-left</v-icon>
                    </v-btn>
               </v-list-item>
           </template>
           <v-divider class="grey darken-1 mx-3"></v-divider>
           <v-list >
            <v-list-item-group v-model="item" dense  color="grey lighten-1">
               <v-list-item dense  v-for="item in items" :key="item.title" min-width="2" router :to="item.route">
                   <v-list-item-icon>
                        <v-icon medium color="black">{{ item.icon }}</v-icon>
                    </v-list-item-icon>
                    
                     <v-list-item-content>
                        <v-list-item-title class="font-weight-medium subtitle-1 black--text">{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                </v-list-item-group>
           </v-list>
       </v-navigation-drawer>
       <v-icon>
       </v-icon>
   </nav>
</template>


<script>
    export default {
        data() {
            return {
            drawer: false,
            item: 1,
            items : [
                {title: 'Inicio', icon: 'mdi-view-dashboard', route: '/'},
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