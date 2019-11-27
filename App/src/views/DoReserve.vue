<template>
  <v-card class="overflow-hidden mx-auto back-ground">
    <v-app-bar extended prominent flat text  class="back-ground" dark height="57">
      <v-layout row wrap>
        <v-flex xs12 md12>
          <div class="my-2">
            <v-btn icon class="link" router to="/reserve">
              <v-icon color="amber lighten-5" dark size="45">mdi-chevron-left</v-icon>
            </v-btn>
          </div>
          <v-row justify="center" align="center">
            <v-icon color="amber lighten-5" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
          </v-row>
        </v-flex>
      </v-layout>
      <v-divider inset class="transparent" vertical></v-divider>
      <v-icon color="amber lighten-5" size="35" class="my-2">mdi-soccer</v-icon>
    </v-app-bar>
  <v-sheet  id="scroll-area-1"  class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620">
    <v-container class="bottom amber lighten-5">
    <v-row justify="center">
      <div class="col-md-4 pa-1">
        <v-img class="text-left ma-2 my-1" :src="company.image" height="200"  style="border-radius: 10px;" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
          <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
        </v-img>
      <v-card-actions>
        <v-row justify="left" no-gutters>
          <div>
            <v-icon color="black" size="15" class="caption">mdi-map-marker</v-icon><span class="subtitle-2 ma-2 font">{{ company.name }}, {{ company.address }}- {{ company.town.name }}, {{ company.town.department.name}}</span>
          </div> 
        </v-row>
      </v-card-actions>
      </div>
    </v-row>
      <v-slide-group style="top: -1em;">
        <v-slide-item v-for="(image, index) in images" :key="index" v-slot:default="{ active, toggle }">
          <v-card :color="active ? 'primary' : 'grey lighten-1'" class="ma-2" height="100" width="200" @click="toggle">
            <v-img :src="image.src" class="text-right" height="100" width="200" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
              <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
            </v-img>
          </v-card>
        </v-slide-item>
      </v-slide-group>
      <v-carousel style="bottom: 1.5em;" cycle height="260" interval=3000 delimiter-icon="mdi-minus">
        <v-carousel-item v-for="(field, i ) in company.fields" :key="i"> 
          <v-hover >
            <v-row justify="center" v-if="field.quantity==0">
            <v-card width="275" v-bind:to=" '/field/' +field.id+'/reservar' "  disabled height="200" class="ma-2 indigo lighten-5 link" :elevation=6 style="border-radius:">
              <v-img class="white--text " height="200" src="https://img.freepik.com/foto-gratis/representacion-3d-balon-futbol-linea-campo-futbol_41667-276.jpg?size=626&ext=jpg" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
              <v-card-title style="position: absolute; top: -0.5em; left: -0.5em;" class="font">Cancha {{ field.name }}</v-card-title>
                <v-row class="fill-height" align="center" justify="center">                       
                  <v-chip label outlined dark color="white" class="headline font-weight-bold font link"> Reservar <v-icon right>mdi-calendar-clock</v-icon></v-chip>
              </v-row>
                  <v-card-subtitle style="position: absolute; top: 7.5em;" class="font font-weight-bold">Sin horarios <v-icon >mdi-emoticon-sad-outline</v-icon></v-card-subtitle>
                    <v-card-title style="position: absolute; bottom: 1.2em;">
                      <span v-if="field.type == 1" class="caption font-weight-bold font">5 Jugadores</span>
                      <span v-else-if="field.type == 2" class="caption font-weight-bold font">7 Jugadores</span>
                      <span v-else class="caption font-weight-bold font">11 Jugadores</span>                              
                  </v-card-title>
                  <v-chip small label dark class="ma-2 font-weight-bold back-ground font" style="bottom: 4em;">Q.{{ field.price }}</v-chip>
              </v-img>                               
            </v-card>
            </v-row>
             <v-row justify="center" v-else>
            <v-card width="275" v-bind:to=" '/field/' +field.id+'/reservar' "   height="200" class="ma-2 indigo lighten-5 link" :elevation=6 style="border-radius:">
              <v-img class="white--text " height="200" src="https://img.freepik.com/foto-gratis/representacion-3d-balon-futbol-linea-campo-futbol_41667-276.jpg?size=626&ext=jpg" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
              <v-card-title style="position: absolute; top: -0.5em; left: -0.5em;" class="font">Cancha {{ field.name }}</v-card-title>
                <v-row class="fill-height" align="center" justify="center">                       
                  <v-chip label outlined dark color="white" class="headline font-weight-bold font link"> Reservar <v-icon right>mdi-calendar-clock</v-icon></v-chip>
                </v-row>
                  <v-card-subtitle style="position: absolute; top: 7.5em;" class="font font-weight-bold">Horarios disponibles: {{ field.quantity }}</v-card-subtitle>
                    <v-card-title style="position: absolute; bottom: 1.2em;">
                      <span v-if="field.type == 1" class="caption font-weight-bold font">5 Jugadores</span>
                      <span v-else-if="field.type == 2" class="caption font-weight-bold font">7 Jugadores</span>
                      <span v-else class="caption font-weight-bold font">11 Jugadores</span>                              
                  </v-card-title>
                  <v-chip small label dark class="ma-2 font-weight-bold back-ground font" style="bottom: 4em;">Q.{{ field.price }}</v-chip>
              </v-img>                               
            </v-card>
            </v-row>
          </v-hover>          
        </v-carousel-item>
      </v-carousel>
    </v-container>
  </v-sheet>
  </v-card>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

let URL = 'http://127.0.0.1:8000/'

export default {
  components: {
    BottomNavigation
  },
  data(){  
    return {
      companyId: this.$route.params.companyId,
      company: [],
      field: [],
      months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
      dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab',],
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
      }
  },
    methods: {
       getCompany() {
        const path = `http://127.0.0.1:8000/api/field-company/${this.companyId}/`
        //const path = `https://api-backend-canchas.herokuapp.com/api/field-company/${this.companyId}/`
          axios.get(path).then((response)=> {
          this.company = response.data;
          //console.log('Company ' + this.company);
          return axios.get(URL+'api/thefield/')
          //return axios.get('https://api-backend-canchas.herokuapp.com/api/field-schedule/')
      }).then((response)=>{
        this.field = response.data
        console.log(this.field);
      })
      },
    },
    created(){
      this.getCompany()
    },
    /*created(){
      this.getDate()
    }*/
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
  .font {
     font-family: 'Ubuntu', sans-serif;
   }
   .link {
     text-decoration: none;
   }
   .heart {
     position: absolute;
     margin-left: 13.7em;
     margin-top:  0.2em;
   }
   .bottom {
     margin-bottom: 20px;
   }
 .back-ground {
    background-color: #011427 !important;
  }
  .font-color {
    color: #011427 !important;
  }
</style>