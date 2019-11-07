<template>
    <v-card class="overflow-hidden mx-auto ">
      <v-toolbar extended prominent flat text  class="transparent" height="57">
        <v-row>
          <v-col cols="12" sm="6" offset-sm="3">
            <v-toolbar-title>
                <span class="font-color font-weight-bold headline font">Bienvenido, Enrique</span>
                  <v-divider inset vertical class="mx-1"></v-divider>
                <img src="@/assets/ball.svg" color="white" alt="" style="width: 35px;">
            </v-toolbar-title>
                <span class="font-color font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
          </v-col>
      </v-row>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon outlined class="font-color">mdi-magnify</v-icon>
          </v-btn>           
      </v-toolbar>
      <BottomNavigation/> 
      <v-sheet id="scroll-area-1" class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620" >
      <v-container class="bottom" >
     <v-row no-gutters>
      <v-col sm="5" md="2">
          <v-hover>
            <v-card  router to="/reserve" class="ma-1 link red lighten-1"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/reser.jpg" >
              </v-img>
              </v-avatar>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text class="font-weight-bold body-2 font ma-1" style="bottom: 0em;">Reservar<v-icon right size="15">mdi-calendar</v-icon>
                </span>
            </v-card>
          </v-hover>
      </v-col>
      <v-col sm="5" md="2">
          <v-hover>
            <v-card class="ma-1 link indigo lighten-1"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/favo.jpg">
              </v-img>
              </v-avatar>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text center class="font-weight-bold body-2 font ma-1" style="bottom: 0em; ">Favoritas<v-icon right size="15">mdi-star</v-icon></span>
            </v-card>
            </v-hover>
      </v-col>
      <v-col sm="5" md="2">
              <v-hover>
                 <v-card class="ma-1 link teal accent-4"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12 >
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/oliver.jpg">
              </v-img>
              </v-avatar>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text center class="font-weight-bold body-2 font ma-1" style="bottom: 0em;">Chamusca<v-icon right size="15">mdi-soccer</v-icon></span>
            </v-card>
              </v-hover>
      </v-col>
      <v-col sm="5" md="2">
            <v-hover>
              <v-card  router to="/companies" class="ma-1 link cyan accent-4"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/centro.jpg" >
              </v-img>
              </v-avatar>
                    <span class="subtitle-1 font">{{ companies.length}}</span>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text center class="font-weight-bold body-2 font ma-1" style="bottom: 0em;">Compañías<v-icon right size="15">mdi-domain</v-icon></span>
            </v-card>
            </v-hover>
       </v-col>
      <v-col sm="5" md="2">
              <v-hover>
                 <v-card  router to="/companies" class="ma-1 link blue-grey"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12 >
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/partido.jpg">
              </v-img>
              </v-avatar>
                <span class="subtitle-1 font">{{ reservations.length}}</span>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text center class="font-weight-bold body-2 font ma-1" style="bottom: 0em;">Partidos<v-icon right size="15">mdi-whistle</v-icon></span>
            </v-card>
              </v-hover>
      </v-col>
      <v-col sm="5" md="2">
              <v-hover>
                 <v-card class="ma-1 link deep-orange accent-2"  style="border-radius: 10px;" dark width=115 height=135 :elevation=12>
              <v-avatar size=55 class="ma-3">
              <v-img  src="@/assets/torneo.jpg">
              </v-img>
              </v-avatar>
                <span class="subtitle-1 font">{{ reservations.length}}</span>
              <v-divider class="mx-2 transparent">
              </v-divider>
                <span text center class="font-weight-bold body-2 font ma-1" style="bottom: 0em;">Torneos<v-icon right size="15">mdi-trophy</v-icon></span>
            </v-card>
              </v-hover>
      </v-col>
       
    </v-row>
     <v-slide-group>
        <v-slide-item v-for="(image, index) in images" :key="index" v-slot:default="{ active, toggle }">
          <v-card :color="active ? 'primary' : 'grey lighten-1'" style="border-radius: 20px;" class="ma-2" height="200" width="300" @click="toggle">
            <v-img :src="image.src" class="text-right" height="200" width="300">
              <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
            </v-img>
          </v-card>
        </v-slide-item>
      </v-slide-group>
    <!--
              <div class="green accent-4 text-center my-1  round"><span class="white--text font">Reservaciones de la semana</span></div> -->
              <!--<template v-if="reservations.length == 0">
                <v-row justify="center" align="center">
                <v-chip class="ma-2 font" close color="red darken-3" outlined justify="center">
                  No tienes Reservaciones
              </v-chip>    
              </v-row>
              <v-row justify="center" align="center">
                <router-link :to="{name: 'companies'}" class="font">Reserva aquí</router-link>
              </v-row>
              </template>
              <template v-else>
                <v-simple-table class="elevation-3 round" style="width: 100%;">
                  <thead>
                    <tr class="round" style="padding: 0;">
                      <th class="text-center font-weight-bold black--text subtitle-1 font">Compañía</th>
                      <th class="text-center font-weight-bold black--text subtitle-1 font" style="padding: 0;">Fecha</th>
                      <th class="text-center font-weight-bold black--text subtitle-1">Horario</th> -->
                      <!--<th class="text-center font-weight-bold black--text subtitle-1 font">Tipo de Cancha</th>
                      <th class="text-center font-weight-bold black--text subtitle-1 font">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr class="tex-center" v-for="(reservation, index) in reservations" :key="index">
                      <td class="text-center font">{{ reservation.company_reserve.name }}</td>
                      <td class="text-center font">{{ reservation.schedule_date }}</td>
                      <td class="text-center ">{{ reservation.schedule_time }}</td> -->
                      <!-- <td class="text-center font"  v-if="reservation.field_reserve.type == 1">5 jugadores</td>
                      <td class="text-center font" v-else-if="reservation.field_reserve.type==2">7 jugadores</td>
                      <td class="text-center" font v-else>11 Jugadores</td>
                      <td><v-chip class="ma-3 font" label light  color="success" small>Completado</v-chip></td>
                    </tr>
                  </tbody>
                </v-simple-table>
              </template> -->
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
      const path = 'http://192.168.1.25:8000/sport/reservations/'
      //const path = 'http://192.168.88.222:8000/sport/reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        console.log(this.reservations);
        
        return axios.get('http://192.168.1.25:8000/sport/companies/');
        //return axios.get('http://192.168.88.222:8000/sport/companies/');
        }).then((response) => {
          this.companies = response.data
          console.log(this.companies);
          
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
     margin-bottom: 125px;
   }
   .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427;
  }
</style>