<template>
    <v-card class="overflow-hidden mx-auto">
        <v-app-bar flat text  class="indigo"  dark height="57">
          <v-layout row wrap>
            <v-flex xs12 md12>
              <v-row justify="center" align="center">
                <v-icon color="white" size="25">mdi-calendar </v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}}, {{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="white" size="35">mdi-soccer</v-icon>
        </v-app-bar>
      <BottomNavigation/>  
      <v-sheet id="scroll-area-1" class="overflow-y-auto indigo lighten-5" height="650" >
        <v-container class="bottom" >
            <v-item-group> 
            <v-row justify="space-around">
            <v-col  v-for="(company, index) in companies" :key="index" cols="12" md="4"> 
                <v-hover >
                  <v-card :elevation="hover ? 12 : 2" :class="{ 'on-hover': hover }" style="border: 1px solid indigo; border-radius: 10px;">
                    <v-img :src="company.image" height="150px">
                    </v-img>
                    <v-footer class="white ma-1"  padless>
                      <v-row justify="left" no-gutters>
                        <div>
                          <span class="subtitle-2 ma-2">{{ company.name }} {{ company.address}}</span>
                        </div> 
                        <v-col class="text-left  caption black--text" cols="12">
                          <div class="description">
                            <span>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon> 
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                              <v-icon size=15 color="amber accent-4">mdi-star</v-icon>
                            </span><br>
                            <span >
                              <v-icon color="black" size="15" class="caption">mdi-map-marker</v-icon>{{ company.town.name}}, {{ company.town.department.name }}
                            </span>
                          </div>
                        </v-col>
                      </v-row>
                    </v-footer>
                    <v-card-actions>
                      <div class="reserve">
                        <v-row justify="left" align="left" class="ma-1 my-1">
                          <div>
                            <span class="ma-1 font-weight-bold  green--text" color="teal darken-4">Canchas: 5</span><br>
                            <div class="span">
                              <span class="ma-1 caption">hola</span>
                            </div> 
                          </div>
                          <v-row justify="end" align="center" class="ma-1"> 
                            <v-btn text small v-bind:to=" 'do_reserve/'+company.id+ '/reserve' " class="link font-weight-bold">Reservar<v-icon right size=15>mdi-chevron-right</v-icon>
                            </v-btn>
                          </v-row>
                        </v-row>
                      </div>
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
import DoReserve from '@/views/DoReserve.vue'

export default {
  data: () => ({
        reservations: [ ] ,
        companies: [ ],
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
      const path = 'http://192.168.1.20:8000/sport/detail-company/'
      axios.get(path).then((response)=> {
        this.companies = response.data
        console.log(response.data);
      })
      },
    },
    created(){
      this.getCompanies()
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
     border: solid 0.5px grey;
     width: 100%;
     border-radius: 5px;
     margin-top: 1.2em; 
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
     margin-bottom: 300px;
   }
   .container {
    max-width: 100%;
    max-height: 100%;
  }
</style>