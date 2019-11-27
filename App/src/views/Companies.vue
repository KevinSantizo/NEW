<template>
      <v-card class="overflow-hidden mx-auto back-ground">
        <v-app-bar extended prominent flat text  class="back-ground" dark height="57">
         <v-flex xs12 md12>
          <v-row justify="center" align="center" class="my-9">
            <v-icon color="amber lighten-5" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font"> {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
          </v-row>
        </v-flex>
          <v-divider inset class="transparent" vertical></v-divider>
            <v-icon color="amber lighten-5" size="35" class="my-2">mdi-soccer</v-icon>
        </v-app-bar>
      <BottomNavigation/>
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620">
        <v-container class="bottom amber lighten-5" style="height: 100%;">
            <v-row  justify="space-around">
              <v-col v-for="(company, i) in companies" :key="i" cols="12" md="3">
                  <v-hover >
                    <v-card  v-bind:to=" 'companies/'+company.id+'/info' " class="link amber lighten-5" max="300" :elevation=12 style="border-radius: 10px;">
                        <v-img  :src="company.image" height="10em" class="text-right pa-2" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
                            <v-card-title class="title white--text">
                              <v-row class="fill-height flex-column" justify="space-between">
                                <div class="description">
                                  <span class="mt-4  caption  text-left font">{{ company.name }},</span>
                                  <span class="mt-4  caption  text-left font"> {{ company.address }}</span>
                                  <v-divider inset vertical class="mx-1"></v-divider>
                                  <span>
                                    <v-icon size=18 color="amber accent-4">mdi-star</v-icon> 
                                    <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                                    <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                                    <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                                    <v-icon size=18 color="amber accent-4">mdi-star</v-icon>
                                  </span>
                              </div>
                            </v-row>
                          </v-card-title>
                        </v-img>
                        <v-card-actions>
                          <div class="">
                            <v-row>
                              <div>
                                <span class="ma-5 font-weight-bold font font-color"  >Email: {{ company.email }}</span><br>
                                  <span class="ma-5 caption font-weight-bold font font-color">Tel. {{ company.phone }}</span>
                              </div>
                            </v-row>
                          </div>
                          <v-spacer></v-spacer>
                          <v-row>
                          <v-btn  outlined v-bind:to=" 'companies/'+company.id+'/info' " class="link font-color"  style="bottom: 0.5em; position: absolute; right: 0.5em;" icon><v-icon>mdi-information-variant</v-icon></v-btn>
                          </v-row>                    
                        </v-card-actions>
                      </v-card>
                    </v-hover>
                  </v-col>
                </v-row>
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

  data: () => ({
    companies: [ ],
    months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
    dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab',],
  }),

  mounted () {
    //const path = 'https://api-backend-canchas.herokuapp.com/api/companies/'
    const path = URL+'api/companies/'
    axios.get(path).then((response)=> {
    this.companies = response.data
    console.log(this.companies);
    })   
  }
}
</script>

<style scoped>
   @import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');

   .description {
     position: absolute;
     margin-top: 5.5em;
     margin-left: 0.2em;
   }
   .bottom {
     padding-bottom: 70px;
   }
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
