<template>
  <v-card class="overflow-hidden ">
    <v-app-bar absolute dark flat text scroll-target="#playground-example" extended  collapse-on-scroll class="back-ground">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="margin-top: 2em;">
        <span class=" font-weight-bold title font">Bienvenido</span>
          <v-divider inset vertical class="mx-1"></v-divider>
          <img src="@/assets/balloon.png" app color="white" alt="" style="width: 25px; border-radius: 100px;">
          <v-divider class="my-1"></v-divider>
        <span class=" font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
      </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
    <v-icon outlined class="font-color">mdi-magnify</v-icon>
    </v-btn>           
    </v-app-bar>
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
                         <v-divider class="grey darken-1 "></v-divider>

               <v-btn  v-if="isLoggedIn" v-bind:to="{ name: 'logout' }"  small class="ma-2 link" tile outlined color="white">
                 <span>Cerrar Sesión</span>
                 <v-icon left>mdi-account-plus-outline</v-icon>
               </v-btn>
              </v-list-item-group>
              
          </v-list>
      </v-navigation-drawer>
    <BottomNavigation/> 
    <v-sheet  id="playground-example" class="overflow-y-auto" max-height=725  >
      <v-container class="bottom" style="height: 100%;">
        <v-row justify="center">
          <v-hover>
              <v-card  router to="/reserve" class="my-1 ma-2 link "  style="border-radius: 10px; background-color: #DF2935 !important;" dark width=375 height=200 :elevation=12>
                <v-avatar size=90 class="ma-1"  style="position: absolute;">
                  <v-img  src="@/assets/reser.jpg" >
                  </v-img>
                </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div  class="subtitle-1 font-weight-bold font">{{ companies.length}} Compañías</div>
                <v-divider inset vertical class="mx-2" ></v-divider>
                <div  class="subtitle-1 font-weight-bold font">{{ fields.length}} Canchas</div>
              </v-row>
                <span text class=" font-weight-bold title font ma-3" style="bottom: -0.5em; position: absolute; right: 0em;">Reservar<v-icon right size="20">mdi-calendar</v-icon>
                </span>
              </v-card>
          </v-hover>
          <v-hover>
            <v-card  router to="/companies" class="my-1 link ma-1 "  style="border-radius: 10px; background-color: #004E64" dark width=375 height=200 :elevation=12>
            <v-avatar size=90 class="ma-1"  style="position: absolute;">
              <v-img  src="@/assets/centro.jpg" >
              </v-img>
            </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="headline font-weight-bold font">{{ companies.length}}</div>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Compañías<v-icon right size="20">mdi-domain</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
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
                <span class="grey--text caption">(Próximamente)</span>
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
                <div class="subtitle-1 font-weight-bold font">Inscríbete a un Torneo <br></div>
                  <v-divider inset vertical class="mx-1"></v-divider>
                <span class="grey--text caption">(Próximamente)</span>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Torneos<v-icon right size="20">mdi-trophy</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
        </v-row>
        <v-divider class="back-ground"></v-divider>
        <template v-if="reservations.length == 0">
          <v-row justify="center" align="center">
            <v-chip class="ma-2 font" close color="red darken-3" outlined justify="center">No tienes Reservaciones</v-chip>    
          </v-row>
          <v-row justify="center" align="center">
            <router-link :to="{name: 'reserve'}" class="font">Reserva aquí</router-link>
          </v-row>
        </template>
      <template v-else>
        <v-row justify="center">
          <span class="font-color font font-weight-bold">Tus Reservaciones <v-icon class="font-color">mdi-calendar</v-icon></span>
        </v-row>
        <v-slide-group >
          <v-slide-item v-for="(reservation, i ) in reservations" :key="i">
            <v-hover >
            <v-card  width="200" height="125" class="ma-2 amber lighten-4" :elevation=6 style="border-radius: 10px;">
              <v-card-title  class="caption font font-weight-medium">{{ reservation.schedule.field.company.name}} {{ reservation.schedule.field.company.town.name}}</v-card-title>
              <v-card-subtitle>
                <span class="caption font-weight-bold font">Fecha: {{ reservation.schedule_date}}</span><br>
                <span class="caption font-weight-bold font">Hora: {{ reservation.schedule.start_time }}</span>   <br>
                <span class="caption font-weight-bold font">Cliente: {{ reservation.customer_reserve.first_name }} {{ reservation.customer_reserve.last_name }}</span><br>
                <span class="caption font-weight-bold font">Precio: {{ reservation.field_reserve.price}}</span>                                            
              </v-card-subtitle>          
              </v-card>
            </v-hover>          
          </v-slide-item>
        </v-slide-group>
      </template>
      </v-container>
    </v-sheet>      
  </v-card>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'
  export default {
          components: {
        BottomNavigation
  },
    data () {
      return {
        modalShow: false,
        reservations: [ ] ,
        companies: [ ],
        fields: [ ],     
        drawer: false, 
        items : [
                {title: 'Inicio', icon: 'mdi-home', to  : '/home'},
                {title: 'Mis Reservaciones', icon: 'mdi-calendar', to: '/account'},
            ],
        }
    },

    methods: {
      getAll(){ 
        const path = 'http:///127.0.0.1:8000/sport/reservations/'
        //const path = 'http://192.168.88.222:8000/sport/reservations/'
          axios.get(path).then((response) => {
          this.reservations = response.data
          console.log(this.reservations);
          
          return axios.get('http:///127.0.0.1:8000/sport/companies/')
          //return axios.get('http://192.168.88.222:8000/sport/companies/');
          }).then((response) => {
            this.companies = response.data
            console.log(this.companies);
            
            return axios.get('http:///127.0.0.1:8000/sport/fields/')
          }).then((response) => {
            this.fields = response.data
            console.log(this.fields);
          }).catch((error) => {
            console.log(error);
          })
      },
  },
  
  computed:{
     isLoggedIn (){
       return this.$store.getters.isLoggedIn
   },
    created(){
      this.getAll()
    }
  }
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
     margin-top: 100px;
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
</style>