<template>
    <v-card class="overflow-hidden mx-auto back-ground">
        <v-app-bar extended prominent flat text   class="back-ground"  dark height="57">
          <div class="ma-3">
                <v-icon color="white" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
         </div>
          <v-spacer ></v-spacer>
                <v-icon color="white" size="35" class="my-2">mdi-soccer</v-icon>
               <v-toolbar-title class="font font-weight-medium" style="top: 3em;  position: absolute;">Explorar</v-toolbar-title>
        </v-app-bar>
      <BottomNavigation/>  
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620">
        <v-container class="bottom" >
            <v-item-group> 
            <v-row justify-space-around>
            <v-col  v-for="(company, index) in companies" :key="index" cols="12" md="4"> 
                <v-hover >
                  <v-card :elevation=12  style="border-radius: 10px;">
                    <v-img :src="company.image" height="150px">
                    </v-img>
                    <v-footer class="white"  padless>
                      <v-row  no-gutters>
                        <v-col >
                        <div>
                          <span class="caption ma-2 font ">{{ company.name }} {{ company.address}}</span>
                        </div> 
                            <span class="caption ma-2">
                              <v-icon color="black" size="15" class="caption font">mdi-map-marker</v-icon>{{ company.town.name}}, {{ company.town.department.name }}
                            </span>
                            </v-col>
                      </v-row>
                    </v-footer>
                    <v-card-actions>
                      <div class="reserve">
                        <v-row  class="ma-1 my-1" v-if="company.fields.length == 0">
                          <div>
                            <v-chip small label class=" ma-1"  color="red" text-color="white" >Sin canchas <v-icon right small>mdi-close-box</v-icon></v-chip>
                          </div>
                          <v-spacer></v-spacer>
                            <v-btn text small v-bind:to=" '/do_reserve/'+company.id+ '/reserve' " class="link font-weight-bold font-color font" disabled>Reservar<v-icon  size=15>mdi-chevron-right</v-icon>
                            </v-btn>
                        </v-row>
                        <v-row  class="ma-1 my-1" v-else>
                          <div>
                            <span class="ma-1 font-weight-bold font-color font" color="teal darken-4">Canchas: {{ company.fields.length }}</span><br>
                          </div>
                          <v-spacer></v-spacer>
                            <v-btn text small v-bind:to=" '/do_reserve/'+company.id+ '/reserve' " class="link font-weight-bold font-color font" >Reservar<v-icon  size=15>mdi-chevron-right</v-icon>
                            </v-btn>
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

export default {
        
  data ()  {
    return {
        reservations: [ ] ,
        companies: [ ],
        show: false,
        months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab',],
        activeBtn: 1,
        showNav: true,
        }
    },
     components: {
    BottomNavigation
  },
    methods: {
      getCompanies() {
      const path = 'http://192.168.88.222:8000/api/field-company/'
      //const path = 'https://api-backend-canchas.herokuapp.com/api/field-company/'
      axios.get(path).then((response)=> {
        this.companies = response.data
        //console.log(response.data);
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
   .reserve {
     border: solid 0.5px grey;
     width: 100%;
     border-radius: 5px;
     margin-top: -0.5em; 
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
     padding-bottom: 70px;
   }
   .container {
    max-width: 100%;
    max-height: 100%;
  }
  .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427;
  }
</style>