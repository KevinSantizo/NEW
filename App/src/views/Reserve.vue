<template>
    <v-container class="overflow-hidden mx-auto back-ground" style="padding-right: 0px; padding-left: 0px;">
        <v-app-bar extended app flat text   class="back-ground"  dark >
          <div class="ma-3">
            <v-icon color="amber lighten-5" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
         </div>
          <v-spacer ></v-spacer>
                <v-icon color="amber lighten-5" size="35" class="my-2">mdi-soccer</v-icon>
               <v-toolbar-title class="font font-weight-medium" style="top: 3em;  position: absolute;">Explorar</v-toolbar-title>
        </v-app-bar>
      <BottomNavigation/>  
        <v-container class="bottom amber lighten-5 " style="border-radius: 25px 25px 0px 0px;">
          <v-item-group class="ma-2"> 
            <v-row justify-space-around>
            <v-col  v-for="(company, index) in companies" :key="index" cols="12" md="4"> 
                <v-hover >
                  <v-card :elevation=12  style="border-radius: 10px;" class="amber lighten-5" v-if="company.fields.length == 0" disabled>
                    <v-img :src="company.image" height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
                    </v-img>
                    <v-footer class="amber lighten-5"  padless>
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
                    <v-card-actions class="amber lighten-5">
                      <div class="reserve link" v-if="company.fields.length == 0" outlined >
                        <v-row  class="ma-1">
                          <div >
                            <v-chip outlined label class=" ma-1" disabled color="red" >Sin canchas <v-icon right small>mdi-close-box</v-icon></v-chip>                          
                          </div>
                          <v-spacer></v-spacer>
                            <v-btn text small class="link font-weight-bold font-color font my-1" disabled>Ver canchas<v-icon  size=20>mdi-stadium</v-icon>
                            </v-btn>
                        </v-row>
                      </div>
                    </v-card-actions>
                  </v-card>
                  <v-card :elevation=12  style="border-radius: 10px;" class="amber lighten-5 link" v-else v-bind:to=" '/do_reserve/'+company.id+ '/reserve'">
                    <v-img :src="company.image" height="150px" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,0.9)">
                    </v-img>
                    <v-footer class="amber lighten-5 link" padless>
                      <v-row  no-gutters>
                        <v-col >
                        <div>
                          <span class="caption ma-2 font  link">{{ company.name }} {{ company.address}}</span>
                        </div> 
                            <span class="caption ma-2">
                              <v-icon color="black" size="15" class="caption font link">mdi-map-marker</v-icon>{{ company.town.name}}, {{ company.town.department.name }}
                            </span>
                            </v-col>
                      </v-row>
                    </v-footer >
                    <v-card-actions class="amber lighten-5">
                      <v-btn class="reserve link color-c" v-bind:to=" '/do_reserve/'+company.id+ '/reserve'" outlined>
                        <v-row  class="ma-1">
                          <div class="my-1">
                            <span class="font-weight-bold color-c font-color font link">Canchas: {{ company.fields.length }}</span><br>
                          </div>
                          <v-spacer></v-spacer>
                            <span text small v-bind:to=" '/do_reserve/'+company.id+ '/reserve' " class="link font-weight-bold font-color font my-1" >Ver canchas<v-icon  size=20>mdi-stadium</v-icon>
                            </span>
                        </v-row>
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-hover>
            </v-col>
            </v-row>
            </v-item-group>
        </v-container>
    </v-container>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

let URL = 'https://api-backend-canchas.herokuapp.com/'
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
      const path = URL+'api/field-company/'
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
     text-decoration: none !important;
   }
   .heart {
     position: absolute;
     margin-left: 13.7em;
     margin-top:  0.2em;
   }
   .bottom {
     padding-bottom: 70px;
     padding-right: 0px;
     padding-left: 0px;
   }
   .container {
    max-width: 100%;
    max-height: 100%;
  }
  .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427 !important;
  }
  .color-c {
    color: #011427 !important;
  }
</style>