<template>
      <v-card class="overflow-hidden mx-auto">
        <v-app-bar flat text  class="indigo"  dark height="57">
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="center" align="center">
                <v-icon color="white" size="25">mdi-calendar </v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" >{{ this.days[new Date().getDay() ]}}, {{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="white" size="35">mdi-soccer</v-icon>
        </v-app-bar>
      <BottomNavigation/>
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto indigo lighten-5" max-height="650">
      <v-container class="bottom" >
      <v-item-group v-model="selected" multiple> 
        <v-row>
          <v-col v-for="(company, i) in companies" :key="i" cols="12" md="3">
              <v-hover >
                <v-card  max="300" :elevation=12 style="border-radius: 10px;">
                  <v-item v-slot:default="{ active, toggle }">
                    <v-img  :src="company.image" height="10em" class="text-right pa-2" @click="toggle"  >
                      <v-btn icon  text color="red accent-4" @click="toggle" :input-value="active">
                        <v-icon active-class="red accent-4"  @click="toggle" :input-value="active">
                          {{ active ? 'mdi-heart' : 'mdi-heart-outline' }}
                        </v-icon>
                      </v-btn>
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
                </v-item>
                    <v-card-actions>
                      <div class="ma-2 ">
                        <v-row>
                          <div>
                            <span class="ma-3 font-weight-medium font" >Email: {{ company.email }}</span><br>
                              <span class="ma-3 caption font-weight-medium font">Tel. {{ company.phone }}</span>
                          </div>
                        </v-row>
                      </div>
                      <v-spacer></v-spacer>
                      <row>
                      <router-link v-bind:to=" 'companies/'+company.id+'/info' "  class="link" style="bottom: 0.5em; position: absolute; right: 0.5em;" ><v-chip outlined small label color="primary"><v-icon small>mdi-information-variant</v-icon></v-chip></router-link>
                      </row>                    
                    </v-card-actions>
                  </v-card>
                </v-hover>
              </v-col>
            </v-row>
          </v-item-group>
          </v-container>
      </v-sheet>
      </v-card>

</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

export default {
  data: () => ({
        companies: [ ],
        show: false,
        selected: [],
        expand: false,
        expand2: false,
        show: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false
    }),
     components: {
    BottomNavigation
  },
    methods: {
      getCompanies() {
      const path = 'http://192.168.1.20:8000/sport/companies/'
      //const path = 'http://192.168.88.222:8000/sport/companies/'
      axios.get(path).then((response)=> {
        this.companies = response.data
        console.log(response.data);
        
      })
      }
    },
    created(){
      this.getCompanies()
    }
}
</script>

<style scoped>
   @import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
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
     margin-bottom: 75px;
   }
   .font {
     font-family: 'Ubuntu', sans-serif;
   }
   .link {
     text-decoration: none;
   }
</style>
