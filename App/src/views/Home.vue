<template>
    <v-card class="overflow-hidden mx-auto">
      <v-app-bar  flat text  class="indigo"  dark height="57">
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="left" align="top">
                
              </v-row>
              <v-row justify="center" align="center">
                <v-toolbar-title>
                    <span class="white--text font-weight-bold" dense>¡Bienvenido!</span>
                      <v-divider inset vertical class="mx-1"></v-divider>
                    <img src="@/assets/ball.svg" color="white" alt="" style="width: 35px;">
                </v-toolbar-title>              </v-row>
            </v-flex>
          </v-layout>
        </v-app-bar>
      <BottomNavigation/> 
      <v-sheet id="scroll-area-1" class="overflow-y-auto indigo lighten-5 " max-height="650" >
      <v-container class="bottom" >
      <v-layout row wrap>
        <v-flex xs12 sm6 lg3> 
          <v-hover v-slot:default="{ hover }">
            <v-card  router to="/reserve"  flat  class="ma-3 link" :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
              <v-img  src="@/assets/reser.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
              </v-img>
              <v-card-actions> 
                <v-btn text class="font-weight-bold">Reservar <v-icon right size="20">mdi-calendar</v-icon>
                </v-btn>
                <v-btn icon>
                    <v-icon color="grey darken-4">mdi-soccer</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-hover>
        </v-flex>
        <v-flex xs12 sm6 lg3> 
          <v-hover v-slot:default="{ hover }">
            <v-card  router to="/companies" flat  class="ma-3 link" :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }">
              <v-img src="@/assets/favo.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
              </v-img>
                <v-card-actions>
                  <v-btn text center class="font-weight-bold ">Canchas Favoritas<v-icon right size="22">mdi-star</v-icon></v-btn>
                  <v-btn icon>
                    <v-icon color="grey darken-4">mdi-soccer</v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-hover>
          </v-flex>
          <v-flex xs12 sm6 lg3>
            <v-hover v-slot:default="{ hover }">
              <v-card   router to="/companies" flat class="ma-3 link" :elevation="hover? 12 : 2"  :class="{'on-hover': hover}">
                <v-img src="@/assets/centro.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                  <v-row class="fill-height pa-4" align="center" justify="center">
                    <div class="display-3">{{ companies.length}}</div>
                  </v-row>
                </v-img>
                <v-card-actions>
                  <v-btn text center class="font-weight-bold  link" router to="/companies">Compañías<v-icon right size="22">mdi-domain</v-icon></v-btn>
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
                  <v-card router to="/companies" flat class="ma-3 link" :elevation="hover? 12 : 2"  :class="{'on-hover': hover}">
                    <v-img src="@/assets/partido.jpg" class="white--text"  height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                      <v-row class="fill-height pa-4" align="center" justify="center">
                        <div class="display-3">{{ reservations.length}}</div>
                      </v-row>
                    </v-img>
                    <v-card-actions>
                      <v-btn text center class="font-weight-bold  link"  @click="" router to="/companies">Partidos<v-icon right size="22">mdi-whistle</v-icon></v-btn>
                      <div class="flex-grow-1" ></div>
                      <v-btn icon>
                        <v-icon color="grey darken-4">mdi-soccer</v-icon>
                      </v-btn>
                    </v-card-actions>
                  </v-card>
              </v-hover>
          </v-flex>
      </v-layout>
          
            <template>
              <div class="green accent-4 text-center my-1  round"><span class="white--text">Reservaciones de la semana</span></div>
              <template v-if="reservations.length == 0">
                <v-row justify="center" align="center">
                <v-chip class="ma-2" close color="red darken-3" outlined justify="center">
                  No tienes Reservaciones
              </v-chip>    
              </v-row>
              <v-row justify="center" align="center">
                <router-link :to="{name: 'companies'}">Reserva aquí</router-link>
              </v-row>
              </template>
              <template v-else>
                <v-simple-table class="elevation-3 round">
                  <thead>
                    <tr class="round">
                      <th class="text-center  font-weight-bold  black--text subtitle-1 ">No.</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Id Reservación</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Compañía</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Fecha</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Horario</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Tipo de Cancha</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Precio</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Cliente</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr class="tex-center" v-for="(reservation, index) in reservations" :key="index">
                      <td class="text-center">{{ index+1 }}</td>
                      <td class="text-center ">{{ reservation.id }}</td>
                      <td class="text-center ">{{ reservation.company_reserve.name }}</td>
                      <td class="text-center ">{{ reservation.schedule_date }}</td>
                      <td class="text-center ">{{ reservation.schedule_time }}</td>
                      <td class="text-center "  v-if="reservation.field_reserve.type == 1">5 jugadores</td>
                      <td class="text-center" v-else-if="reservation.field_reserve.type==2">7 jugadores</td>
                      <td class="text-center" v-else>11 Jugadores</td>
                      <td class="text-center ">{{ reservation.field_reserve.price }}</td>
                      <td class="text-center ">{{ reservation.customer_reserve.first_name}}</td>
                      <td><v-chip class="ma-3" label light  color="success" small>Completado</v-chip></td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </template>
            </template>
      
      </v-container>
      </v-sheet>      
    </v-card>

</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

  export default {
    data: () => ({
        modalShow: false,
        reservations: [ ] ,
        companies: [ ],
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
    }),
      components: {
    BottomNavigation
  },
    methods: {
      getAll(){ 
      const path = 'http://192.168.88.222:8000/sport/reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        return axios.get('http://192.168.88.222:8000/sport/companies/');
        }).then((response) => {
          this.companies = response.data
        }).catch((error) => {
          console.log(error);
        })
        }
    },
    created(){
      this.getAll()
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
   .link{
      text-decoration:  none;
   }
   .container {
     max-width: 100%;
     max-height: 100%;

   }
   .description {
     position: absolute;
     margin-top: 3.5em;
     margin-left: 0.2em;
   }
   .item-icon {
     position: absolute;
     left: 0.5em;
     bottom: 0.5em;
   }
   .icon {
     position: absolute;
     left: 2.5em;
     bottom: 1.4em;
   }
    .item-icon2 {
     position: absolute;
     left: -0.5em;
     top: 0.5em;
   }
   .icon2 {
     position: absolute;
     left: 2.5em;
     bottom: -0.3em;
   }
  .bottom {
     margin-bottom: 125px;
   }
</style>