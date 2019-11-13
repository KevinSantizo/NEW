<template>
   <v-card  class="overflow-hidden mx-auto back-ground">
        <v-toolbar extended prominent flat text  class="back-ground" dark height="57">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
              <v-toolbar-title class="ma-9" style="top: -1em; position: absolute;">
                <span class=" font-weight-bold title font">Enrique</span>
                <v-divider class="my-1"></v-divider>
                <span class=" font-weight-medium subtitle-1 font">Reservaciones: {{reservations.length}}</span>
              </v-toolbar-title>
            <v-spacer>
            </v-spacer>
            <v-btn icon text>
          <v-icon color="white" size="30" class="my-2">mdi-settings-box</v-icon>
            </v-btn>
        </v-toolbar>
        <v-navigation-drawer dense dark absolute v-model="drawer"  temporary class="back-ground" >
      <template v-slot:prepend>
          <v-list-item> 
              <v-avatar class="profile my-5" tile style="border-radius: 10px;"> 
                    <img src="@/assets/apitec.png" alt="">
                </v-avatar> 
                <v-divider inset vertical class="mx-2 transparent"> 
                </v-divider> 
                <v-list-item-content>
                    <v-list-item-title  class="font-weight-medium title">Apitec</v-list-item-title>
                </v-list-item-content>
                <v-btn icon @click="drawer = !drawer">
                <v-icon color="grey" size=40>mdi-chevron-left</v-icon>
                </v-btn>
          </v-list-item>
        </template>
           <v-divider class="grey darken-1 "></v-divider>
          <v-list>
          <v-list-item-group  v-model="items" class="link">
              <v-list-item  class="link"   v-for="item in items" :key="item.title" router :to="item.to" min-width="2" >
                  <v-list-item-icon>
                      <v-icon medium color="white" class="link" size=25>{{ item.icon }}</v-icon>
                  </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title class="font-weight-medium subtitle-1 link">{{ item.title }}</v-list-item-title>
                  </v-list-item-content>
              </v-list-item>
              </v-list-item-group>
          </v-list>
      </v-navigation-drawer>
              <BottomNavigation/>
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620">
        <v-container class="bottom" style="height: 100%;">
          <v-row justify="center">
             <v-hover v-for="(reservation, i) in reservations" :key="i">
              <v-card class="link ma-1 amber lighten-4" outlined style="border-radius: 10px;"  width=375 height=150 gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"  :elevation=12>
                <v-card-title  class="caption font font-weight-bold">{{ reservation.schedule.field.company.name}} {{ reservation.schedule.field.company.town.name}}</v-card-title>
              <v-card-subtitle>
                <span v-if="reservation.field_reserve.type == 1" class="caption font-weight-bold font">Tipo de cancha: 5 Jugadores</span>
                <span v-else-if="reservation.field_reserve.type == 2" class="caption font-weight-bold font">7 Jugadores</span>
                <span v-else class="caption font-weight-bold font">11 Jugadores</span><br>
                <span class="caption font-weight-bold font">Fecha: {{ reservation.schedule_date}}</span><br>
                <span class="caption font-weight-bold font">Hora: {{ reservation.schedule.start_time }}</span>     
                </v-card-subtitle>          
                <v-chip small  label dark class="ma-1 font-weight-bold light-blue darken-4 font">Total: Q.{{ reservation.field_reserve.price }}</v-chip>                    
              </v-card>
          </v-hover>
          </v-row>
        </v-container>

      </v-sheet>
 </v-card>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

export default {
  data: () => ({
    reservations:[ ],
     drawer: false, 
        items : [
                {title: 'Inicio', icon: 'mdi-home', to  : '/home'},
                {title: 'Mis Reservaciones', icon: 'mdi-calendar', to: '/account'},
            ],
            colors: [
              {color: 'indigo darken-4'},
            ]
    }),
     components: {
    BottomNavigation
  },
  methods: {
    getReservations(){
      const path = 'http:///127.0.0.1:8000/sport/reservations/'
      axios.get(path).then((response)=>{
        this.reservations = response.data
        console.log(this.reservations);
        
      }).catch((error)=>{
        console.log(error)
      })
    }
  },
  created(){
    this.getReservations()
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
  .font {
     font-family: 'Ubuntu', sans-serif;
   }
   .back-ground {
    background-color: #011427;
  }
  .bottom {
     padding-bottom: 70px;
   }
   .link {
     text-decoration: none;
   }
</style>
