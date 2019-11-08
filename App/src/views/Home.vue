<template>
    <v-card class="overflow-hidden mx-auto back-ground">
        <v-app-bar extended prominent flat text  class="back-ground" dark height="57">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-toolbar-title>
                <span class=" font-weight-bold headline font">Bienvenido, Enrique</span>
                  <v-divider inset vertical class="mx-1"></v-divider>
                <img src="@/assets/ball.svg" color="white" alt="" style="width: 35px;">
            </v-toolbar-title>
            <span class=" font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
          </v-col>
      </v-row>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon outlined class="font-color">mdi-magnify</v-icon>
          </v-btn>           
      </v-app-bar>
      <BottomNavigation/> 
      <v-sheet id="scroll-area-1" class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px; " max-height=620>
      <v-container class="bottom" height="100%">
     <v-row justify="center">
          <v-hover>
            <v-card  router to="/reserve" class="my-1 ma-2 link "  style="border-radius: 10px; background-color: #011427 !important;" dark width=375 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/reser.jpg" >
              </v-img>
              </v-avatar>
              <v-row align="center" justify="center" style="bottom: 4em; position: absolute; left: 5em;">                       
                <v-col cols="12" sm="9" offset-sm="3">
                  <span class="body-2 font">{{ companies.length}} Compañías</span><br>  
                  <span class="body-2 font">{{ fields.length}} Canchas</span>
                  </v-col>
                </v-row>
                 <!-- <span class="subtitle-1 font" style="position: absolute; top: 3.7em; left: 3em;">{{ companies.length}} Compañías</span><br>
                 <span class="caption font" style="position: absolute; top: 3.7em; left: 6.7em;">{{ fields.length }} Canchas</span>-->
              <v-row class="pa-5">
                <span text class=" font-weight-bold title font ma-2">Reservar<v-icon right size="20">mdi-calendar</v-icon>
                </span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card class=" link deep-orange darken-4 my-1 ma-1 "  style="border-radius: 10px;" dark width=375 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/favo.jpg">
              </v-img>
              </v-avatar>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: 0em; ">Favoritas<v-icon right size="20">mdi-star-outline</v-icon></span>
              </v-row>
            </v-card>
            </v-hover>
      
              <v-hover>
                 <v-card class="my-1 link  light-green accent-4 ma-1 "  style="border-radius: 10px;" dark width=375 height=135 :elevation=12 >
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/oliver.jpg">
              </v-img>
              </v-avatar>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: 0em;">Chamusca<v-icon right size="20">mdi-soccer</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>
      
            <v-hover>
              <v-card  router to="/companies" class="my-1 link pink darken-4 ma-1 "  style="border-radius: 10px;" dark width=375 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/centro.jpg" >
              </v-img>
              </v-avatar>
                    <span class="subtitle-1 font">{{ companies.length}}</span>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: 0em;">Compañías<v-icon right size="20">mdi-domain</v-icon></span>
              </v-row>
            </v-card>
            </v-hover>
      
              <v-hover>
                 <v-card  router to="/companies" class="my-1 link red darken-4 ma-1 "  style="border-radius: 10px;" dark width=375 height=135 :elevation=12 >
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/partido.jpg">
              </v-img>
              </v-avatar>
                <span class="subtitle-1 font">{{ reservations.length}}</span>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: 0em;">Partidos<v-icon right size="20">mdi-whistle</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>
    
              <v-hover>
                 <v-card class="link purple darken-4 my-1 ma-1 "  style="border-radius: 10px;" dark width=375  height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/torneo.jpg">
              </v-img>
              </v-avatar>
                <span class="subtitle-1 font">{{ reservations.length}}</span>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: 0em;">Torneos<v-icon right size="20">mdi-trophy</v-icon></span>
              </v-row>
            </v-card>
              </v-hover>
    </v-row>
    <v-divider class="back-ground"></v-divider>
    <div><span>hola</span></div>
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
                   <v-slide-group >
                          <v-slide-item v-for="(reservation, i ) in reservations" :key="i">
                          <v-hover >
                            <v-card width="175" height="150" class="ma-2 indigo lighten-5" :elevation=6 style="border-radius: 10px;">
                              
                              <v-card-subtitle style="position: absolute; top: 8.7em;" class="caption font font-weight-medium">Horarios disponibles:</v-card-subtitle>
                              <v-card-title>
                              <span v-if="reservation.field_reserve.type == 1" class="caption font-weight-bold font">5 Jugadores</span>
                              <span v-else-if="reservation.field_reserve.type == 2" class="caption font-weight-bold font">7 Jugadores</span>
                              <span v-else class="caption font-weight-bold font">11 Jugadores</span>                              
                              </v-card-title>                                
                                <v-chip x-small label dark class="ma-2 font-weight-bold light-blue darken-4 font"  style="bottom: 2em; left: 0.5em;" >{{ reservation.field_reserve.price }}</v-chip>
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
        images: [
          { src: "https://bogota.gov.co/sites/default/files/styles/despliegue_1366x768_px/public/field/image/Nueva%20cancha%20sint%C3%A9tica%20en%20el%20Parque%20Las%20Cruces%20beneficiar%C3%A1%20comunidad%20de%20tres%20localidades%20P.jpg"},
          { src: "https://lh3.googleusercontent.com/6ygjCkkb-sYeWWJLh964wzsu-rnQcpquw2I9ebvQ4xzKCxoFnE0tWpuPXN7yV85rCdgEWqJq=w1080-h608-p-no-v0"},
          { src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1vYclJ6emIr9MCaXt8cH754_vIRt-ouh_I6IuIj58t_SPrjxd&s"},
          { src: "https://www.parqueygrama.com/wp-content/uploads/2017/03/grama-sintetica-para-canchas-de-futbol-2.png"},
          { src: "https://www.pqs.pe/sites/default/files/styles/852x479/public/archivos/2015/actualidad/01/sabugattas/pastosintetico-lacanchita-futbol7-3.jpg?itok=awaMBCao"},
          { src: "http://www.tucaqueta.com/wp-content/uploads/2017/01/Cancha.jpg"},
          { src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQEgGMX5i7iqw9ALETWvwt1shQtrmQp7LBnCqqY3DNLgKAMV7-sA&s"},
          { src: "https://files.alerta.rcnradio.com/alerta_tolima_prod/public/styles/article_desktop/public/migration/canchas14deoctubre.png?itok=thGx-QGr"},
          { src: "https://www.eluniversal.com.co/sites/default/files/201706/cancha_2.jpg"},
          { src: "http://www.eje21.com.co/site/wp-content/uploads/2016/04/Cancha-sintetica-de-la-terminal-de-manizales.jpg"},
          { src: "https://files.rcnradio.com/public/styles/img_galeria/public/2019-02/whatsapp_image_2019-02-11_at_4.22.50_pm_1_0.jpeg?itok=pjSrd8tA"}
        ],
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
    }),
      components: {
    BottomNavigation
  },
    methods: {
      getAll(){ 
      const path = 'http://192.168.1.104:8000/sport/reservations/'
      //const path = 'http://192.168.88.222:8000/sport/reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        console.log(this.reservations);
        
        return axios.get('http://192.168.1.104:8000/sport/companies/')
        //return axios.get('http://192.168.88.222:8000/sport/companies/');
        }).then((response) => {
          this.companies = response.data
          console.log(this.companies);
          
          return axios.get('http://192.168.1.104:8000/sport/fields/')
        }).then((response) => {
          this.fields = response.data
          console.log(this.fields);
          
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
     margin-bottom: 100px;
   }
   .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427;
  }
</style>