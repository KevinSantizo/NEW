<template>
    <v-card class="overflow-hidden mx-auto back-ground">
        <v-app-bar extended prominent flat text  class="back-ground" dark height="57">
          <v-layout row wrap>
            <v-flex xs12 md12>
                <div class="my-2">
                <v-btn icon class="link" style="color: transparent;" router to="/companies">
                <v-icon color="white" dark size="45" >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              <v-row justify="center" align="center">
                <v-icon color="white" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="white" size="35" class="my-2">mdi-soccer</v-icon>
        </v-app-bar>
        <v-sheet id="scroll-area-1" class="overflow-y-auto " style="border-radius: 25px 25px 0px 0px;" height="620" >
    <v-container class="bottom" >
            <v-item-group> 
            <v-row justify="center">
                <v-hover>
                <v-card  width="400"  class="my-1"  style="border-radius: 10px;">
                    <v-img :src="company.image">
                        <div style="position: absolute; right: 0em;">
                            <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
                        </div>
                        <v-row align="end" class="lightbox white--text  my-5 pa-2 fill-height">
                            <v-col>
                                <div class="subheading font">{{ this.name }}</div>
                                <div class="body-1 font">{{ company.email }}</div>
                            </v-col>
                        </v-row>
                    </v-img>
                    <v-card-actions>
                    <v-rating v-model="rating" background-color="amber darken-4" color="amber darken-4"></v-rating>
                    <v-spacer></v-spacer>
                    <v-chip small class="light-green accent-4 font-weight-bold font" dark>Destacada</v-chip>
                      </v-card-actions>
                </v-card>
                </v-hover>
                </v-row>
            <v-hover>
            <v-card class="mx-auto overflow-hidden my-2 transparent" :elevation=12 style="max-width: 600px; border: 1px solid white; border-radius: 10px;">
                    <v-slide-group>
                        <v-slide-item v-for="(image, index) in images" :key="index" v-slot:default="{ active, toggle }">
                            <v-card :color="active ? 'primary' : 'grey lighten-1'" class="ma-2" height="100" width="200" @click="toggle">
                                <v-img :src="image.src" class="text-right" height="100" width="200">
                                <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
                                </v-img>
                            </v-card>
                        </v-slide-item>
                    </v-slide-group>
            <v-card-title style="margin-top: 0em;">
            <span class="font-weight-medium font" style="color: red !important;">{{ name }} - {{company.town.name}}</span>
           <v-divider inset vertical class="mx-1 transparent">
           </v-divider>
           <v-chip label outlined><span class="caption font font-color">{{company.address }}, {{ company.town.name }} - {{ company.town.department.name}}</span></v-chip>
        </v-card-title>
                      <div class="pa-2 caption font font-color">
                        <em>Portions of the materials used are trademarks and/or copyrighted works of Epic Games, Inc. All rights reserved by Epic. This material is not official and is not endorsed by Epic.</em>
                    </div>
            </v-card>
            </v-hover>
            <v-row justify="center">
            <div style="width: 400px;" class="ma-5 my-1">
                <v-row no-gutters>
                    <v-col sm="5" md="6">
                        <v-hover>
                         <v-card class="my-2 indigo darken-4 " :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-stadium</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Canchas</span>
                                <v-divider inset vertical class="mx-2"></v-divider>
                                <span class="font">{{ company.fields.length }}</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>
                        <v-card class="my-2 light-green accent-4" :elevation=12 dark height="75" width="170"  style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-trophy</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Torneos</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>
                        <v-card class="my-2 orange darken-4" :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-soccer</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Partidos</span>
                                <v-divider inset vertical class="mx-2"></v-divider>
                                <span class="font"></span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>   
                        <v-card class="my-2 cyan" :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-calendar</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Reservar</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                </v-row>  
            </div>
            </v-row>
            </v-item-group>
        </v-container>
      </v-sheet>
    </v-card>
</template>

<script>
import axios from 'axios'
export default {
    data () {
       return {
        companyId: this.$route.params.companyId,
        company: [],
        name: '',
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
        rating: 3,
       }
       },
      
    methods: {
        getCompany(){
        const path = `http://192.168.88.222:8000/api/field-company/${this.companyId}/`   
        //const path = `https://api-backend-canchas.herokuapp.com/api/field-company/${this.companyId}/`   
        axios.get(path).then((response)=> {
        this.company = response.data
        this.name = this.company.name
        //console.log(this.name);
        //console.log(this.company);
      })
        }
    },
    created(){
      this.getCompany()
    }
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
.back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427 !important;
  }
</style>