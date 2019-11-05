<template>
<v-card class="overflow-hidden mx-auto back-ground">
        <v-app-bar extended prominent flat text  class="back-ground" dark height="57">
          <v-layout row wrap>
                <div class="my-2">
                <v-btn icon class="link" v-bind:to=" '/do_reserve/'+field.company.id+ '/reserve' ">
                <v-icon color="white" dark size="45">mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              <v-row justify="center" align="center" >
                <span class="font-weight-bold font" >Reservar</span>
              </v-row>
                <v-flex xs12 md12>
              <v-row justify="center" align="center">
                <v-icon color="white" size="25">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption font" > {{ this.dayss[new Date().getDay() ]}}, {{  this.months[new Date().getMonth()] }} - {{ new Date().getDate()}} | {{ new Date().getFullYear() }}</span>
              </v-row>
            </v-flex>
          </v-layout>
          <v-divider inset class="transparent" vertical></v-divider>
                <v-icon color="white" size="35" class="my-2">mdi-soccer</v-icon>
        </v-app-bar>
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto" style="border-radius: 25px 25px 0px 0px;" max-height="620">
      <v-container class="bottom" >
        <form action="">
          <v-hover>
          <v-card :elevation=12 style="border-radius: 25px;">
                                <v-card-title class="back-ground">
                                    <v-row justify="center">
                                  <span class="white--text title" v-if="field.type == 1">Cancha {{ field.name }} de 5 Jugadores </span>
                                  <span class="white--text title" v-else-if="field.type == 2">Cancha {{ field.name }} de 7 Jugadores </span>
                                  <span class="white--text title" v-else>Cancha {{ field.name }} de 11 Jugadores </span>
                                    </v-row>
                                </v-card-title>
                                <v-card-text>
                                  <span class="black--text font-weight-medium">{{field.company.name}} , {{field.company.town.name}}</span><br>
                                  <span class="black--text font-weight-medium">Cliente: Juanito Pérez</span>
                                    <v-hover >
                                      <v-card max-width="100%" class="mx-auto" color="back-ground" >
                                        <v-card-text> 
                                          <span class="subheading white--text font-weight-medium">Horarios disponibles (hoy)</span>
                                          
                                          <v-chip-group column multiple active-class="lime accent-3 black--text" >
                                            <v-row justify="space-around" class="ma-2">
                                            <v-chip small v-for="(time, i)  in field.schedules" :key="i" :v-if="time.status == 2">
                                              {{ time.start_time }}
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
                                    <div v-for="(implement, i) in this.implements" :key="i">{{ implement.name}} - Q{{implement.price}}</div><br>  
                                    <div style="margin-top: -1em; margin-left: 3em;">
                                            <v-layout row wrap class="pa-0"  v-for="(implem, i) in this.implements" :key="i" >
                                              <input type="checkbox" name="check" id="check" @change="showInput()"  light color="light-green accent-4">
                                              <v-avatar size="25" class="ma-2">
                                                <img :src="implem.image" alt="alt">
                                              </v-avatar>
                                                  <v-flex xs2 md1>
                                                <input type="number" style="display: none;" id="content" min=0 max=10  maxlength=3 >
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
          </v-hover>


        </form>
      </v-container>
    </v-sheet>
 </v-card>
</template>


<script>
import axios from 'axios'
export default {
    data () {
       return {
          fieldId: this.$route.params.fieldId,
          field: [ ],
          company: [],
          implements: [ ],
          months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
          dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab'],
          
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
        getField() {
        const path = `http://192.168.88.222:8000/sport/field-schedule/${this.fieldId}/`   
        axios.get(path).then((response) => {
        this.field = response.data
        console.log(this.field);       
        return axios.get('http://192.168.88.222:8000/sport/implements/')
      }).then((response)=>{
        this.implements = response.data
        console.log(this.implements);

      }).catch((error) => {
          console.log(error);
        })
        },
        showInput() {
        var element = document.getElementById("content");
        var check = document.getElementById("check");
        if (check.checked) {
            element.style.display='block';
        }
        else {
            element.style.display='none';
        }
    }
    },
    created(){
      this.getField()
    },

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
     margin-bottom:  50px;
   }
 .back-ground {
    background-color: #011427;
  }
</style>