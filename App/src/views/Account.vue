<template>
   <v-card  class="overflow-hidden mx-auto back-ground">
        <v-toolbar extended prominent flat text  class="back-ground" dark height="57">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
              <v-toolbar-title class="ma-9" style="top: 0em; position: absolute;">
                <span class=" font-weight-bold title font"></span>
                <span class=" font-weight-medium subtitle-1 font">Reservaciones <v-divider inset vertical></v-divider> {{ quant }}</span>
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
              <v-avatar class="profile my-5" tile style="border-radius: 10px;" size="75"> 
                    <img src="https://static.platzi.com/static/website/v2/images/avatar_default.afdd5b436fc2.png" alt="">
                </v-avatar> 
                <v-divider inset vertical class="mx-2 transparent"> 
                </v-divider> 
                <v-list-item-content>
                    <v-list-item-title  class="font-weight-medium title">{{name}}</v-list-item-title>
                    <span>{{last_name}}</span>
                </v-list-item-content>
                <v-btn icon @click="drawer = !drawer">
                <v-icon color="grey" size=40>mdi-chevron-left</v-icon>
                </v-btn>
          </v-list-item>
        </template>
           <v-divider class="grey darken-1 "></v-divider>
          <v-list shaped>
          <v-list-item-group  v-model="items" class="link" color="amber darken-1">
              <v-list-item  class="link"   v-for="item in items" :key="item.title" router :to="item.to" min-width="2" >
                  <v-list-item-icon>
                      <v-icon medium class="link" size=25>{{ item.icon }}</v-icon>
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
        <v-container class="bottom">
          <v-row justify="center">
             <v-hover v-for="(reservation, i) in user_reservations.reservations" :key="i">
              <v-card class="link ma-1" outlined style="border-radius: 10px;"  width=375 :elevation=12>
                <v-img src="https://img.freepik.com/foto-gratis/representacion-3d-balon-futbol-linea-campo-futbol_41667-272.jpg?size=626&ext=jpg" class="white--text align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)" height="200px">
              <v-icon  style="top: 0.2em; right: 0.2em; position: absolute;" size="30" color="white">mdi-soccer</v-icon>
              <v-card-title>{{ reservation.field_reserve.company.name }}, {{ reservation.field_reserve.company.town.department.name }}</v-card-title>
                <v-card-subtitle>
                <span v-if="reservation.field_reserve.type == 1" class="body-2 font-weight-bold font  white--text">Tipo de cancha: 5 Jugadores</span>
                <span v-else-if="reservation.field_reserve.type == 2" class="body-2 font-weight-bold font  white--text">7 Jugadores</span>
                <span v-else class="body-2 font-weight-bold font  white--text">11 Jugadores</span><br>
                <span class="body-2 font-weight-bold font  white--text">Fecha: {{ reservation.schedule_date }}</span><br>
                <span class="body-2 font-weight-bold font  white--text">Hora: {{ reservation.schedule.start_time}} </span><br>
                </v-card-subtitle>  
            </v-img>                    
             <v-card-actions>
                <v-chip label dark class="font-weight-bold light-blue darken-4 font">Total: Q.{{ reservation.field_reserve.price }}</v-chip>                    
                      <v-spacer></v-spacer>
                      <v-btn icon>
                        <v-icon color="light-blue darken-4" size="40">mdi-soccer-field</v-icon>
                      </v-btn>
                </v-card-actions>
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
    user_reservations: [ ],
    months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab',],
    user_name: '',
    name: '',
    last_name: '',
    quant: '',
    rating: 4.3,
    card: [
      {src: 'https://img.freepik.com/foto-gratis/representacion-3d-balon-futbol-linea-campo-futbol_41667-272.jpg?size=626&ext=jpg'}
    ],
     drawer: false, 
        items : [
                {title: 'Inicio', icon: 'mdi-home', to  : '/home'},
                {title: 'Mis Reservaciones', icon: 'mdi-calendar', to: '/account'},
            ],
    }),
     components: {
    BottomNavigation
  },
    computed: {
     isLoggedIn (){
       return this.$store.getters.isLoggedIn
   }
  },
  mounted() {
      const path = 'http://192.168.88.222:8000/api/user-reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        //console.log(this.reservations);
        let find_user_reservations = this.reservations.find(v => v.id == this.$store.state.user)
        this.user_reservations = find_user_reservations
        this.user_name = find_user_reservations.username
         this.name = find_user_reservations.first_name
        this.last_name = find_user_reservations.last_name
        //console.log(find_user_reservations);
        this.quant= find_user_reservations.quantity
        //console.log('Cantidad' + ' ' + this.quant);
        
      })
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
