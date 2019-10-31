<template>
 <div class="indigo lighten-5">
        <v-app-bar flat text app class="indigo" dark height="57">
          <v-app-bar-icon></v-app-bar-icon>
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="left" align="top">
                <div style="position: absolute; left: 0.2em; top: 0.5em;">
                <v-btn icon class="link" router to="/reserve">
                <v-icon color="white" dark size="30 " >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              </v-row>
              <v-row justify="center" align="center">
                <v-icon color="white" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption" > {{ this.dayss[new Date().getDay() ]}},{{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="white" size="35">mdi-soccer</v-icon>
        </v-app-bar>
        <v-divider inset vertical> </v-divider>
     <div style="top: 1em;">
      <v-slide-group class="" style="top: -2em;">
        <v-slide-item v-for="(image, index) in images" :key="index" v-slot:default="{ active, toggle }">
          <v-card :color="active ? 'primary' : 'grey lighten-1'" class="ma-4" height="100" width="200" @click="toggle">
            <v-img :src="image.src" class="text-right" height="100" width="200">
              <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
            </v-img>
          </v-card>
        </v-slide-item>
      </v-slide-group>
        </div>
      
        <div class="row no-gutters">
          <div class="col-md-4 pa-1" style="bottom: 2em;">
            <v-img class="text-left " :src="company.image" height="200" style="border-radius: 10px;">
              <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
            </v-img>
            <v-card-actions>
              <v-row justify="left" no-gutters>
                <div>
                  <v-icon color="black" size="15" class="caption">mdi-map-marker</v-icon><span class="subtitle-2 ma-2">{{ company.name }}, {{ company.address }}- {{ company.town.name }}, {{ company.town.department.name}}</span>
                </div> 
                    <span>
                      <v-icon size=15 color="amber accent-4">mdi-star</v-icon> 
                      <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                      <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                      <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                      <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                    </span>
                  
              </v-row>
            </v-card-actions>
          </div>
          <div class="col-md-8 " style="top: -1em;">
          <span class="card-title  ma-3 my-1">Elije  una de las Canchas.</span>
            <div class="card-body ma-2" style="border: 1px solid grey; border-radius: 10px; witdh: 100%;">
              <template>
                <v-layout row wrap >
                  <v-flex  v-for="(field, i ) in company.field_set" :key="i" class="ma-1 pa-2" xsm12 md4>
                    <v-hover >
                      <v-card class="reserve"  color="indigo lighten-2" >
                        <v-row justify="left" align="left" class="ma-3 my-1">
                          <div>
                            <span class="my-1 font-weight-bold">Cancha</span>
                            <span class="ma-1 font-weight-bold  green--text" color="teal darken-4">{{ field.name}}</span>
                            <div class="span">
                              <span v-if="field.type == 1" class="caption font-weight-medium black--text">5 Jugadores</span>
                              <span v-else-if="field.type == 2" class="caption font-weight-medium">7 Jugadores</span>
                              <span v-else class="caption font-weight-medium">11 Jugadores</span>
                            </div> 
                            <div class="span">
                              <v-chip small label class="ma-2 font-weight-medium black--text orange"  outlined style="left: -0.8em;" >{{ field.price }}</v-chip>
                            </div> 
                          </div>
                          <v-row justify="end" align="center" class="pa-1"> 
                            <v-dialog v-model="dialog"  persistent  max-width="600px" >
                              <template v-slot:activator="{ on }">
                                <v-btn text small class="link font-weight-bold" v-on="on">Reservar<v-icon right size=15>mdi-chevron-right</v-icon>
                                </v-btn>
                              </template>
                              <form action="">
                              <v-card>
                                <v-card-title class="indigo">
                                  <span class="headline">Reservar</span>
                                </v-card-title>
                                
                                <v-card-text>
                                  <span class="black--text font-weight-medium">Cancha B, 5 jugadores</span><br>
                                  <span class="black--text font-weight-medium">Futeca, xela</span><br>
                                  <span class="black--text font-weight-medium">Cliente: Juanito Pérez</span>
                                    <v-hover >
                                      <v-card max-width="100%" class="mx-auto" color="indigo" >
                                        <v-card-text> 
                                          <span class="subheading black--text font-weight-medium">Horarios disponibles (hoy)</span>
                                          
                                          <v-chip-group column multiple active-class="lime accent-3 black--text" >
                                            <v-row justify="space-around" class="ma-2">
                                            <v-chip small v-for="(time, i)  in times" :key="i"  >
                                              {{ time }}
                                            </v-chip>
                                            </v-row>
                                          </v-chip-group>
                                        </v-card-text>
                                      </v-card>
                                    </v-hover>
                                    <v-divider inset vertical></v-divider>
                                    <v-spacer></v-spacer>
                                    <span class="black--text font-weight-medium">Resto de la semana</span>
                                       <v-slide-group multiple show-arrows>
                                          <v-slide-item
                                            v-for="(day, i) in days"
                                            :key="i"
                                            v-slot:default="{ active, toggle }"
                                          >
                                            <v-btn
                                              small
                                              class="mx-2"
                                              :input-value="active"
                                              active-class="lime accent-3 black--text"
                                              depressed
                                              rounded
                                              @click="toggle"
                                            >
                                              {{ day }}
                                            </v-btn>
                                          </v-slide-item>
                                        </v-slide-group>   
                                        <v-divider class="ma-1"></v-divider>                                 
                                    <span class=" black--text font-weight-medium">Extras: </span>
                                    <span>Balón Q20.00 c/u</span> <v-divider inset vertical class="mx-1"></v-divider> <span>Gabachas Q25.00</span> 
                                    <div style="margin-top: -1em; margin-left: 3em;">
                                            <v-layout row wrap class="pa-1">
                                              <v-checkbox  v-model="enabled" hide-details  light color="lime accent-3"></v-checkbox>
                                              <v-icon left color="black" size=30>mdi-soccer</v-icon>
                                                  <v-flex xs2 md1>
                                                <v-text-field type="number" :disabled="!enabled" name="input-1" id="test" min=0 max=10  maxlength=3 ></v-text-field>
                                              </v-flex>
                                              <v-checkbox  v-model="enable" hide-details color="light-green accent-4"></v-checkbox>
                                              <v-icon left color="black" size=30>mdi-tshirt-crew-outline</v-icon>
                                            <v-flex xs2 md1>
                                                <v-text-field type="number" :disabled="!enable" name="input-1" id="test2" min=0 max=50  maxlength=3 ></v-text-field>
                                              </v-flex>
                                            </v-layout>
                                            </div>
                                </v-card-text>
                              <v-card-actions>
                              <v-spacer></v-spacer>
                              <v-btn color="red accent-4" outlineded text @click="dialog = false">Cancelar</v-btn>
                              <v-btn color="light-green accent-4"  @click="dialog = false">Guardar</v-btn>
                              </v-card-actions>
                              </v-card>
                              </form>
                            </v-dialog>
                          </v-row>
                        </v-row>
                      </v-card>  
                    </v-hover>          
                  </v-flex>
                </v-layout>
              </template>
            </div>
          </div>
        </div>
    </div>
  </template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'
export default {
  data () {
    return {
           components: {
            BottomNavigation
          },
        companyId: this.$route.params.companyId,
        company: [],
        show: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        dayss: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false,
        dialog: false,
        enabled: false,
        enable: false,
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
  
      times: [
        '12:00 PM',
        '1:00 PM',
        '4:00 PM',
        '6:00 PM',
        '7:00 PM',
        '8:00 PM',
        '9:00 PM',
        '10:00 PM',
        '11:00 PM',
      ],
      days: [
        'M',
        'J',
        'V',
        'S',
        'D'
      ],
      test: 0,
      test2: 0
    }
  },
    methods: {
       getCompany() {
      const path = `http://192.168.88.222:8000/sport/field-company/${this.companyId}/`
      axios.get(path).then((response)=> {
        this.company = response.data;
        console.log(response.data);
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
   .reserve {
     width: 100%;
     border-radius: 5px;
     margin-top: -1.2em; 
   }
   .calendar {
     position: absolute;
     margin-top: 10.1em;
   }
   .span {
     position: relative;
     margin-top: -0.5em;
   }
   .description {
     position: absolute;
     margin-top: -0.8em;
     margin-left: 1em;
   }
   .back {
     position: absolute;
     margin-top: -1.5em;
     margin-left: -0.2em;
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
     margin-bottom:  50px;
   }
   .container {
    max-width: 100%;
    max-height: 100%;
  }
  .actions {
  bottom: 3em; 
  }
    .text{
  min-height: 30px !important;
}
</style>