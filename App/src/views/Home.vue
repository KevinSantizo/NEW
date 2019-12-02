<template>
  <v-container class=" overflow-hidden mx-auto">
    <v-app-bar  class="grey lighten-2" text height=85 app>
      <v-app-bar-nav-icon color="black" x-large @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-row justify="center">
      <v-toolbar-title style="margin-top: 0.5em;">
        <span class=" font-weight-black title font black--text">Bienvenido {{ user_name }}</span>
          <v-divider inset vertical class="mx-1 black"></v-divider>
          <img src="@/assets/balloon.png" app color="white" alt="" style="width: 25px; border-radius: 100px;">
          <v-divider class="my-1 transparent"></v-divider>
      </v-toolbar-title>
      </v-row>
    </v-app-bar>
    <v-navigation-drawer dense dark app v-model="drawer"  temporary class="grey lighten-2" style="border-radius: 0px 35px 35px 0px;">
      <template v-slot:prepend>
          <v-list-item> 
              <v-avatar class="profile my-5"  size="75"> 
                    <img src="https://static.platzi.com/static/website/v2/images/avatar_default.afdd5b436fc2.png" alt="">
                </v-avatar> 
                <v-divider inset vertical class="mx-2 transparent"> 
                </v-divider> 
                <v-list-item-content>
                    <v-list-item-title  class="font-weight-medium title font black--text">{{ name }}</v-list-item-title>
                    <span class="font black--text">{{last_name}}</span>
                </v-list-item-content>
                <v-btn icon @click="drawer = !drawer">
                <v-icon class="color-c" size=40>mdi-chevron-left</v-icon>
                </v-btn>           
          </v-list-item>
        </template>
           <v-divider class="grey darken-1 "></v-divider>
          <v-list shaped>
          <v-list-item-group  v-model="items" class="link">
              <v-list-item  class="link black--text" v-for="item in items" :key="item.title" router :to="item.to" min-width="2" >
                  <v-list-item-icon>
                      <v-icon medium class="link black--text" size=25>{{ item.icon }}</v-icon>
                  </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title class="font-weight-medium subtitle-1 link font black--text">{{ item.title }}</v-list-item-title>
                  </v-list-item-content>
              </v-list-item>
              <v-divider class="grey darken-1 "></v-divider>
               <v-btn  v-if="isLoggedIn" v-bind:to="{ name: 'logout' }"  small class="ma-2 link indigo--text" tile text>
                 <v-icon color="black" left>mdi-power</v-icon> <span class="font black--text">Cerrar Sesión</span>
               </v-btn>
              </v-list-item-group> 
          </v-list>
      </v-navigation-drawer>
    <BottomNavigation/> 
      <v-container class="bottom">
        <v-row justify="center">
        <v-icon color="indigo" size="20">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font indigo--text" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
        <v-carousel cycle height="200" hide-delimiter-background :show-arrows="false" class="my-3">
          <v-carousel-item v-for="(company, i) in this.companies" :key="i" >
            <v-img class="white--text " height="200" :src="company.image" gradient="to bottom, rgba(0.5,0,0,0.5), rgba(0.5,0,0,0.5)" style="border-radius: 10px;">
              <v-row class="fill-height" align="center" justify="center">
                <div class="display-1"> <span class="font">{{ company.name }}</span><br>
                <v-row justify="center" align="center">
                  <span><v-icon right size=35>mdi-stadium</v-icon></span>  
                </v-row>
                </div>
              </v-row>
            </v-img>                               
          </v-carousel-item>
        </v-carousel>
         <v-row justify="left" align="left">
          <div class="ma-4 font-weight-bold title font indigo--text"> Haz tus reservaciones</div>
          </v-row>
          <v-hover>
              <v-card  router to="/reserve" class="my-1 ma-2 link "  style="border-radius: 10px; background-color: #DF2935 !important;" dark width=375 height=200 :elevation=12>
              <v-row class="fill-height pa-4 ma-2" align="center" justify="center">  
                <div  class="display-1 font-weight-bold font">
                  <span text class="font" >Reservar</span><br>
                  <v-row justify="center">
                  <span><v-icon right size=40 >mdi-calendar</v-icon></span>  
                  </v-row>
                </div>                      
              </v-row>
              </v-card>
          </v-hover>
            <v-divider class="black mx-4"></v-divider>
          <v-hover>
            <v-card  router to="/companies" class="my-3 link ma-1 "  style="border-radius: 10px; background-color: #004E64" dark width=375 height=200 :elevation=12>
              <v-row class="fill-height pa-4 ma-2" align="center" justify="center">  
                <div  class="display-1 font-weight-bold font">
                  <span text class="font" >Lugares<v-icon right size="40">mdi-domain</v-icon></span><br>
                  <v-row justify="center">
                    <span>{{ companies.length}}</span>  
                  </v-row>
                </div>  
              </v-row>                    
            </v-card>
          </v-hover>
         <!-- <v-hover>
            <v-card class=" link my-1 ma-1 "  style="border-radius: 10px; background-color: #0EB588;" dark width=375 height=200 :elevation=12>
              <v-avatar size=90 class="ma-1"  style="position: absolute;">
                <v-img  src="@/assets/favorite.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="subtitle-1 font-weight-bold font">Canchas Favoritas</div>
              </v-row>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Favoritas<v-icon right size="20">mdi-star-outline</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card disabled  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" class="my-1 link accent-4 ma-1 "  style="border-radius: 10px; background-color: #FF0022" dark width=375 height=200 :elevation=12 >
              <v-avatar size=90 class="ma-1" style="position: absolute;">
                <v-img  src="@/assets/oliver.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="subtitle-1 font-weight-bold font">Buscar Chamuscas</div>
                  <v-divider inset vertical class="mx-1"></v-divider>
                    <v-avatar size=90 class="ma-1" >
                    <v-img  src="@/assets/prox.png" >
                    </v-img>
                  </v-avatar>
              </v-row>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Chamusca<v-icon right size="20">mdi-soccer</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card disabled  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" class="link my-1 ma-1 "  style="border-radius: 10px; background-color: #FED766;" dark width=375  height=200 :elevation=12>
              <v-avatar size=75 class="ma-3" style="position: absolute;">
                <v-img  src="@/assets/torneo.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">   
              <v-avatar size=75 class="ma-3 profile">                    
                 <v-img  src="@/assets/prox.png" style="width: 35px; height: 75px;" >
                </v-img>
              </v-avatar>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Torneos<v-icon right size="20">mdi-trophy</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>-->
        </v-row>
            <v-divider class="black"></v-divider>
              <template v-if="this.user_today_reservation.quantity==0">
              <div class="back-ground accent-4 text-center my-1 round"  label><span class="title white--text">Hoy</span></div>
                <v-row justify="center" align="center">
                <v-chip class="ma-2" close color="red darken-3" outlined justify="center">
                  No tienes Reservaciones
              </v-chip>    
              </v-row>
              <v-row justify="center" align="center">
                <router-link :to="{name: 'reserve'}">Reserva aquí</router-link>
              </v-row>
              </template>
              <div v-else >
              <div class="back-ground accent-4 text-center my-1 round"  label v-if="this.user_today_reservation.quantity==1">
                <span class="title white--text">Hoy: {{this.user_today_reservation.quantity}} reservación</span>
              </div>
              <div class="back-ground accent-4 text-center my-1 round"  label v-else>
                <span class="title white--text">Hoy: {{this.user_today_reservation.quantity}} reservaciones</span>
              </div>
                <v-row justify="center" class="ma-3" >
                  <v-fab-transition>
                <v-btn  color="black"  class="link" router to="/reserve"  fab dark  outlined>
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </v-fab-transition>
                  </v-row>
                  <v-divider></v-divider>
                 <v-slide-group>
                  <v-slide-item v-for="reservation in this.user_today_reservation.reservations" :key="reservation.id" :reservation="reservation"> 
                    <v-hover >
                      <v-card class="link ma-1 amber lighten-5" style="border-radius: 5px;"  width=325>
                        <v-img gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)"  src="https://img.freepik.com/foto-gratis/representacion-3d-balon-futbol-linea-campo-futbol_41667-272.jpg?size=626&ext=jpg" class="white--text align-end"  height="215px">
                      <v-icon  style="top: 0.2em; right: 0.2em; position: absolute;" size="30" color="white">mdi-soccer</v-icon>
                      <v-card-title><span></span>{{ reservation.field_reserve.company.name }}, {{ reservation.field_reserve.company.town.department.name }}</v-card-title>
                        <v-card-subtitle>
                        <span class="body-2 font-weight-bold font  white--text">Fecha: {{ reservation.field_reserve.company.address }}</span><br>
                        <span class="body-2 font-weight-bold font  white--text">Fecha: {{ reservation.schedule_date }}</span><br>
                        <span class="body-2 font-weight-bold font  white--text">Hora: {{ reservation.schedule.start_time}} </span><br>
                        <span v-if="reservation.field_reserve.type == 1" class="body-2 font-weight-bold font  white--text">Tipo de cancha: 5 Jugadores</span>
                        <span v-else-if="reservation.field_reserve.type == 2" class="body-2 font-weight-bold font  white--text">7 Jugadores</span>
                        <span v-else class="body-2 font-weight-bold font  white--text">11 Jugadores</span><br>
                        </v-card-subtitle>    
                        <v-card class="profile" width=75 heigth=50 style="position: absolute; bottom: 0.5em; right: 0.5em; border-radius: 10px;">
                        <img :src="'https://api-backend-canchas.herokuapp.com'+reservation.field_reserve.company.image" alt="Image" width=75 height=50 >
                        </v-card>
                    </v-img>                    
                    <v-card-actions>
                        <v-chip label dark small class="font-weight-bold back-ground font ">Total: Q.{{ reservation.field_reserve.price }}</v-chip>                    
                        <v-btn icon><v-icon class="color-c" size="33">mdi-soccer-field</v-icon></v-btn>
                        <v-spacer></v-spacer>
                        <v-btn class="link" icon color="blue-grey darken-1" ><v-icon size=25 color="blue-grey darken-1">mdi-pencil-outline</v-icon></v-btn>
                        <v-divider inset vertical class="ma-2"></v-divider>
                        <v-btn class="link" icon  color="red darken-4"  data-toggle="modal" ><v-icon size=25 color="red darken-4">mdi-trash-can-outline</v-icon></v-btn>
                  </v-card-actions>      
                    </v-card>
                  </v-hover>       
            </v-slide-item>
          </v-slide-group>
          </div>
      </v-container>
  </v-container>
</template>
<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

let URL = 'https://api-backend-canchas.herokuapp.com/'
  export default {
     components: {
        BottomNavigation
  },

    data () {
      return {
      months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
      dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab',],
      reservations: [ ] ,
      user_reservations: [],
      companies: [ ],
      fields: [ ],     
      users: [ ],
      user_reservation_today: [ ],
      user_today_reservation:[ ],
      user_name: '',
      slide: 'first',
      name: '',
      last_name: '',
      drawer: false, 
      items : [
              {title: 'Inicio', icon: 'mdi-home', to  : '/home'},
              {title: 'Mis Reservaciones', icon: 'mdi-calendar', to: '/account'},
          ],
        }
    },

  mounted () {
      Promise.all([
      axios.get(URL+'api/companies/'),
      axios.get(URL+'api/fields/'),
      ]).then((responses)=>{
        this.companies = responses[0].data
        this.fields = responses[1].data        
        //console.log(this.companies);
        //console.log(this.fields);
      })
  },
    created(){
      this.getUser()
    },
  computed: {
    isLoggedIn (){
      return this.$store.getters.isLoggedIn
    }
   }, 

    methods: {
      getUser(){
        axios.get(URL+'api/user-reservation-today/').then((response)=>{
          this.user_reservation_today = response.data
          let find_user = this.user_reservation_today.find (v => v.id == this.$store.state.user)
          this.user_today_reservation = find_user
          this.user_name = find_user.username
          this.name = find_user.first_name
          this.last_name = find_user.last_name
          //console.log(this.user_today_reservation);
          //console.log(this.user_name);
          //console.log(this.name);
          //console.log(this.user_reservation_today);
        })
      }
    },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
  .font {
     font-family: 'Ubuntu', sans-serif;
   }
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
      text-decoration:  none !important;
   }
   .container {
     max-width: 100%;
     max-height: 100%;
   }
  .bottom {
     padding-bottom: 70px;
   }
   .back-ground {
    background-color: #011427 !important;
  }
  .font-color {
    color: #011427;
  }
  .border-1 {
    border-radius: 0px 0px 50px 50px;
  }
  .color-c {
    color: #011427 !important;
  }
  .custom-caption {
  text-align: center;
  padding: 12px;
  color: white;
  background-color: rgba(0, 0, 0, .3);
  }
</style>