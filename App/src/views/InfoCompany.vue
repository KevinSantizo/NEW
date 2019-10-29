<template>
    <v-card class="over-flow-hidden">
        <v-app-bar flat text app class="indigo"  dark height="57">
            <v-layout row wrap>
                <v-flex xs12 md12>
                    <v-row justify="left" align="top">
                <div style="position: absolute; left: 0.2em; top: 0.5em;">
                <v-btn icon  class="link" router to="/companies">
                <v-icon color="white" dark size="30 " >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              </v-row>
                <v-row justify="center" align="center">
                    <v-icon color="black" size="15" >mdi-map-marker</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold subtitle-1">Quetzaltenango, quetzaltenango</span>
                </v-row>
                <v-row justify="center" align="center">
                    <v-icon color="black" size="15">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}},{{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
                </v-row>
                </v-flex>
            </v-layout>
        </v-app-bar>
        <span>{{ company.name }}</span>
        <div v-for="(field, i) in company.field_set" :key="i">
            <span>{{ field.name }}</span>
        </div>
    </v-card>
</template>

<script>
import axios from 'axios'
export default {
    data () {
       return {
           companyId: this.$route.params.companyId,
           company: [],
           days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
           months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
       }
       },
    methods: {
        getCompany(){
      const path = `http://192.168.1.20:8000/sport/field-company/${this.companyId}/`   
    axios.get(path).then((response)=> {
        this.company = response.data;
      }).catch((error) => {
          console.log(error);
        })
        }
    },
    created(){
      this.getCompany()
    }
}
</script>


<style scoped>
.link {
    text-decoration:  none;
}
</style>