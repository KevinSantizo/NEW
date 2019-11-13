<template>
    <v-card class="overflow-hidden ">
        <v-app-bar absolute dark flat text scroll-target="#playground-example" extended  collapse-on-scroll class="back-ground">
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title style="margin-top: 2em;">
          <span class=" font-weight-bold headline font">Bienvenido, Enrique</span>
            <v-divider inset vertical class="mx-1"></v-divider>
          <img src="@/assets/balloon.png" app color="white" alt="" style="width: 35px; border-radius: 100px;">
          <v-divider class="my-1"></v-divider>
          <span class=" font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
                <!--<span class=" font-weight-bold headline font">Bienvenido, Enrique</span>
                  <v-divider inset vertical class="mx-1"></v-divider>
                <img src="@/assets/ball.svg" color="white" alt="" style="width: 35px;">-->
        </v-toolbar-title>
        <!--<v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-toolbar-title>
                <span class=" font-weight-bold headline font">Bienvenido, Enrique</span>
                  <v-divider inset vertical class="mx-1"></v-divider>
                <img src="@/assets/ball.svg" color="white" alt="" style="width: 35px;">
            </v-toolbar-title>
            <span class=" font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
          </v-col>
        </v-row>-->
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon outlined class="font-color">mdi-magnify</v-icon>
          </v-btn>           
      </v-app-bar>
      <BottomNavigation/> 
      <v-sheet  id="playground-example" class="overflow-y-auto " max-height="725">
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
                 <v-card class="my-1 link accent-4 ma-1 "  style="border-radius: 10px; background-color: #FF0022" dark width=375 height=200 :elevation=12 >
              <v-avatar size=90 class="ma-1" style="position: absolute;">
              <v-img  src="@/assets/oliver.jpg">
              </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                  <div class="subtitle-1 font-weight-bold font">Buscar Chamuscas</div>
              </v-row>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Chamusca<v-icon right size="20">mdi-soccer</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>
       <!--
              <v-hover>
                 <v-card  router to="/companies" class="my-1 link ma-1 "  style="border-radius: 10px; background-color: #533A71;" dark width=375 height=200 :elevation=12 >
              <v-avatar size=75 class="ma-3" style="position: absolute;">
              <v-img  src="@/assets/partido.jpg">
              </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                  <div class="subtitle-1 font-weight-bold font">{{ reservations.length}}</div>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Partidos<v-icon right size="20">mdi-whistle</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>
   
              <v-hover>
                 <v-card class="link my-1 ma-1 "  style="border-radius: 10px; background-color: #FED766;" dark width=375  height=200 :elevation=12>
              <v-avatar size=75 class="ma-3" style="position: absolute;">
              <v-img  src="@/assets/torneo.jpg">
              </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                  <div class="subtitle-1 font-weight-bold font">Inscríbete a un Torneo <br></div>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Torneos<v-icon right size="20">mdi-trophy</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>-->
    </v-row>
    <v-divider class="back-ground"></v-divider>
              <template v-if="reservations.length == 0">
                <v-row justify="center" align="center">
                <v-chip class="ma-2 font" close color="red darken-3" outlined justify="center">
                  No tienes Reservaciones
              </v-chip>    
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
                            <v-card  width="175" height="150" class="ma-2 indigo lighten-5" :elevation=6 style="border-radius: 10px;">
                              <v-card-title  class="caption font font-weight-medium">{{ reservation.schedule.field.company.name}} {{ reservation.schedule.field.company.town.name}}</v-card-title>
                              <v-card-subtitle>
                                <span v-if="reservation.field_reserve.type == 1" class="caption font-weight-bold font">5 Jugadores</span>
                                <span v-else-if="reservation.field_reserve.type == 2" class="caption font-weight-bold font">7 Jugadores</span>
                                <span v-else class="caption font-weight-bold font">11 Jugadores</span><br>
                                <span class="caption font-weight-bold font">Fecha: {{ reservation.schedule_date}}</span><br>
                                <span class="caption font-weight-bold font">Hora: {{ reservation.schedule.start_time }}</span>                         
                              </v-card-subtitle>          
                                <v-chip x-small label dark class="ma-2 font-weight-bold light-blue darken-4 font">Q.{{ reservation.field_reserve.price }}</v-chip>
                             <v-row justify="end">
                            </v-row>
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
    data: () => ({
        modalShow: false,
        reservations: [ ] ,
        companies: [ ],
        fields: [ ],      
    }),
      components: {
        BottomNavigation
  },
    methods: {
      getAll(){ 
      const path = 'http://192.168.1.109:8000/sport/reservations/'
      //const path = 'http://192.168.88.222:8000/sport/reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        console.log(this.reservations);
        
        return axios.get('http://192.168.1.109:8000/sport/companies/')
        //return axios.get('http://192.168.88.222:8000/sport/companies/');
        }).then((response) => {
          this.companies = response.data
          console.log(this.companies);
          
          return axios.get('http://192.168.1.109:8000/sport/fields/')
        }).then((response) => {
          this.fields = response.data
          console.log(this.fields);
          let d = new Date()
          let n = d.getHours()
          console.log(n);
          
        }).catch((error) => {
          console.log(error);
        })
        },
    },
    created(){
      this.getAll()
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
     padding-bottom: 70px;
     margin-top: 100px;
   }
   .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427;
  }
  .border-1 {
    border-radius: 0px 0px 50px 50px;
  }
</style>