<template>
    <v-container class="overflow-hidden mx-auto back-ground"  style="padding-left: 3px; padding-right: 3px;">
        <v-app-bar extended app flat text  class="back-ground">
          <v-layout row wrap>
            <v-flex xs12 md12>
                <div class="my-2" style="position: absolute;">
                <v-btn icon class="link" style="color: transparent;" router to="/companies">
                <v-icon color="amber lighten-5" dark size="45" class="link" >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              <v-row justify="center" align="center">
                <v-icon color="amber lighten-5" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font white--text"> {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="amber lighten-5" size="35" class="my-2">mdi-soccer</v-icon>
        </v-app-bar>
    <v-container class="bottom amber lighten-5" style="border-radius: 25px 25px 0px 0px;">
            <v-row justify="center">
                <v-hover>
                <v-card  width="375"  class="amber lighten-5"  style="border-radius: 10px;">
                    <v-img :src="this.company.image" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.6)">
                        <div style="position: absolute; right: 0em;">
                            <v-icon color="amber lighten-5" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
                        </div>
                        <v-row align="end" class="lightbox white--text  my-5 pa-2 fill-height">
                            <v-col>
                                <div class="subheading font">{{ this.company.name }}</div>
                                <div class="body-1 font">{{ this.company.email }}</div>
                            </v-col>
                        </v-row>
                    </v-img>
                    <v-card-actions>
                    <v-rating v-model="rating" background-color="amber darken-4" readonly color="amber darken-4"></v-rating>
                    <v-spacer></v-spacer>
                    <v-chip small class="light-green accent-4 font-weight-bold font" dark>Destacada</v-chip>
                      </v-card-actions>
                </v-card>
                </v-hover>
                </v-row>
                <v-divider></v-divider>
            <v-hover>
            <v-card class="mx-auto overflow-hidden my-2 ma-2 amber lighten-5" style="max-width: 600px; border: 1px solid white; border-radius: 10px;">
                <v-slide-group>
                    <v-slide-item v-for="image in images" :key="image.id" :image="image">
                        <v-card class="ma-2" height="100" width="200" @click="toggle">
                            <v-img :src="image.src" class="text-right" height="100" width="200" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.3)">
                            <v-icon color="amber lighten-5" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
                            </v-img>
                        </v-card>
                    </v-slide-item>
                </v-slide-group>
            <v-card-title style="margin-top: 0em;">
            <span class="font-weight-medium font" style="color: red !important;">{{ this.company.name }} - {{this.company.town.name}}</span>
           <v-divider inset vertical class="mx-1 transparent">
           </v-divider>
           <v-chip label outlined><span class="caption font font-color">{{this.company.address }}, {{ this.company.town.name }} - {{ this.company.town.department.name}}</span></v-chip>
        </v-card-title>
                      <div class="pa-2 caption font font-color">
                        <em>Portions of the materials used are trademarks and/or copyrighted works of Epic Games, Inc. All rights reserved by Epic. This material is not official and is not endorsed by Epic.</em>
                    </div>
            </v-card>
            </v-hover>
            <v-divider></v-divider>
            <v-row justify="center">
            <div style="width: 400px;" class="ma-5 my-1">
                <v-row no-gutters justify="space-around">
                    <v-col sm="5" md="6">
                        <v-hover>
                         <v-card class="my-2 indigo darken-4 " :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-stadium</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Canchas</span>
                                <v-divider inset vertical class="mx-2"></v-divider>
                                <span class="font">{{ this.company.fields.length }}</span>
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
                              <!--<v-col sm="5" md="6">
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
                        <v-card class="my-2 cyan link" v-bind:to=" '/do_reserve/'+company.id+ '/reserve' " :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon right size=30>mdi-calendar</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="font">Reservar</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>-->
                </v-row>  
                <v-divider></v-divider>
                <span class="font">Dudas y Sugerencias</span>
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-text-field v-model="names" :counter="10" :rules="nameRules"  class="font" label="Nombre" required ></v-text-field>
                    <v-text-field v-model="email" :rules="emailRules" class="font" label="E-mail" required ></v-text-field>
                    <v-text-field v-model="message" :rules="messageRules"  class="font" label="Mensaje" required ></v-text-field>
                    <v-btn color="success" class="ma-1 font link"  @click="validate"  > Enviar </v-btn>
                    <v-btn color="error" class="ma-1 link font link" router to='/home'>Cancelar</v-btn>
                    <v-btn color="primary" class="ma-1 font link" @click="reset">Limpiar</v-btn>
                </v-form>
            </div>
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
import axios from 'axios'
let URL =  'https://api-backend-canchas.herokuapp.com/'
export default {
    data () {
       return {
        companyId: this.$route.params.companyId,
        company: [],
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
        valid: true,
        names: '',
        nameRules: [
            v => !!v || 'Nombre requerido',
            v => (v && v.length <= 10) || 'El nombre debe contener menos de 10 caracteres',
        ],
        email: '',
        emailRules: [
            v => !!v || 'E-mail requerido',
            v => /.+@.+\..+/.test(v) || 'E-mail  debe ser válido',
        ],
        message:'',
        messageRules: [
            v => !!v || 'Mensaje requerido',
            v => (v && v.length <= 100) || 'El nombre debe contener menos de 10 caracteres',
        ]
       }
       },
         computed: {
     isLoggedIn (){
       return this.$store.getters.isLoggedIn
   }
},
    methods: {
        validate () {
        if (this.$refs.form.validate()) {
          this.snackbar = true
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },

    mounted(){
        const path = `https://api-backend-canchas.herokuapp.com/api/field-company/${this.companyId}/`   
        //const path = `https://api-backend-canchas.herokuapp.com/api/field-company/${this.companyId}/`   
        axios.get(path).then((response)=> {
        this.company = response.data
        //console.log(this.company);
      })
    }
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
.font {
     font-family: 'Ubuntu', sans-serif;
   }
.link {
    text-decoration: none !important;
}
.back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427 !important;
  }

  .bottom {
     padding-bottom: 70px;
     margin-top: 10px;
   }
</style>