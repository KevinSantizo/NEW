<template>
  <v-container class="my-5 round grey lighten-3">
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
    <v-layout row wrap>
        <v-flex xs12 sm6 lg3> 
            <v-hover v-slot:default="{ hover }">
            <v-card  router to="/companies"  flat  class="ma-3" :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                    <v-img  src="@/assets/reser.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                    </v-img>
                    <v-card-actions> 
                        <v-btn text class="font-weight-bold">Reservar <v-icon right size="20">mdi-calendar</v-icon>
                        </v-btn>
                        <div class="flex-grow-1"></div>
                        <v-btn icon>
                            <v-icon color="grey darken-4">mdi-soccer</v-icon>
                        </v-btn>

                    </v-card-actions>
                </v-card>
            </v-hover>
        </v-flex>
        <v-flex xs12 sm6 lg3> 
            <v-hover v-slot:default="{ hover }">
            <v-card  router to="/companies" flat  class="ma-3" :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
                <v-img src="@/assets/favo.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                </v-img>
                    <v-card-actions>
                        <v-btn text center class="font-weight-bold ">Canchas Favoritas<v-icon right size="22">mdi-star</v-icon></v-btn>
                        <div class="flex-grow-1" ></div>
                        <v-btn icon>
                            <v-icon color="grey darken-4">mdi-soccer</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-hover>
        </v-flex>
        <v-flex xs12 sm6 lg3>
            <v-hover v-slot:default="{ hover }">
                <v-card   router to="/companies" flat class="ma-3" :elevation="hover? 12 : 2"  :class="{'on-hover': hover}">
                <v-img src="@/assets/centro.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                <v-row class="fill-height pa-4" align="center" justify="center">
                            <div class="display-3">{{ companies.length}}</div>
                        </v-row>
                </v-img>
                    <v-card-actions>
                        <v-btn text center class="font-weight-bold " router to="/companies">Compañías<v-icon right size="22">mdi-domain</v-icon></v-btn>
                        <div class="flex-grow-1" ></div>
                        <v-btn icon>
                            <v-icon color="grey darken-4">mdi-soccer</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-hover>
        </v-flex>
        <v-flex xs12 sm6 lg3>
            <v-hover v-slot:default="{ hover }">
                <v-card router to="/companies" flat class="ma-3" :elevation="hover? 12 : 2"  :class="{'on-hover': hover}">
                   <v-img src="@/assets/partido.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                        <v-row class="fill-height pa-4" align="center" justify="center">
                            <div class="display-3">{{ reservations.length}}</div>
                        </v-row>
                  </v-img>
                    <v-card-actions>
                        <v-btn text center class="font-weight-bold " router to="/companies">Partidos<v-icon right size="22">mdi-whistle</v-icon></v-btn>
                        <div class="flex-grow-1" ></div>
                        <v-btn icon>
                            <v-icon color="grey darken-4">mdi-soccer</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-hover>
        </v-flex>
    </v-layout>
    <v-card text class="pa-5">
        <v-layout row wrap>
        <v-flex xs12 md12>
           <template>
             <div class="teal accent-4 text-center my-1  round"><span class="white--text">Reservaciones de la semana</span></div>
             <template >
               <v-row justify="center" align="center">
              <v-chip class="ma-2" close color="red darken-3" outlined justify="center">
                No tienes Reservaciones
             </v-chip>    
             </v-row>
            <v-row justify="center" align="center">
              <router-link :to="{name: 'companies'}">Reserva aquí</router-link>
            </v-row>
             </template>
             <template>
               <v-simple-table class="elevation-1 round">
                <thead class="grey darken-4 round round">
                  <tr class="round">
                    <th class="text-center grey--text subtitle-1 ">No.</th>
                    <th class="text-center grey--text subtitle-1">Id Reservación</th>
                    <th class="text-center grey--text subtitle-1">Compañía</th>
                    <th class="text-center grey--text subtitle-1">Fecha</th>
                    <th class="text-center grey--text subtitle-1">Horario</th>
                    <th class="text-center grey--text subtitle-1">Tipo de Cancha</th>
                    <th class="text-center grey--text subtitle-1">Precio</th>
                    <th class="text-center grey--text subtitle-1">Cliente</th>
                    <th class="text-center grey--text subtitle-1">Estado</th>
                  </tr>
                </thead>
                <tbody>

      </tbody>
  </v-simple-table>
  </template>
  
</template>

</v-flex>

</v-layout>

</v-card>
<div class="navbar" id="myNavbar">
  <a href="#home" class="active">Home</a>
  <a href="#news">News</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
</div>
</v-container>

</template>

<script>
import axios from 'axios'
  export default {
    data: () => ({
        modalShow: false,
        reservations: [ ] ,
        companies: [ ]
    }),

    methods: {
    }
}
</script>

<style scoped>
  .v-card {
    transition: opacity .4s ease-in-out;
  }
  .v-card:not(.on-hover) {
    opacity: 0.9;
  }
  .show-btns {
    color: rgba(255, 255, 255, 1) !important;
  }
  .round{
        border-radius: 10px;
   }
   .navbar {
  overflow: hidden;
  background-color: #333;  
  position: fixed;
  bottom: 0;
  width: 100%;
}

.navbar a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}


</style>