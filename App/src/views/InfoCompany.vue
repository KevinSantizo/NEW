<template>
    <div class="indigo lighten-5">
        <v-app-bar flat text app class="indigo"  dark height="57">
            <v-layout row wrap>
                <v-flex xs12 md12>
                    <v-row justify="left" align="top">
                <div style="position: absolute; left: 0.2em; top: 0.5em;">
                <v-btn icon class="link" router to="/companies">
                <v-icon color="white" dark size="30 " >mdi-chevron-left</v-icon>
                </v-btn>
              </div>
              </v-row>
                <v-row justify="center" align="center">
                    <v-icon color="white" size="15" >mdi-map-marker</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold subtitle-1">{{ company.town.name}}, {{ company.town.department.name}}</span>
                </v-row>
                <v-row justify="center" align="center">
                    <v-icon color="white" size="15">mdi-calendar</v-icon><v-divider inset vertical class="mx-1"></v-divider><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}}, {{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
                </v-row>
                </v-flex>
            </v-layout>
        </v-app-bar>
        <v-row no-gutters class="pa-2">
            <div>
                <v-hover>
                <v-card :elevation=20 width="400" class="my-3" style="border-radius: 10px;">
                    <v-img :src="company.image">
                        <div style="position: absolute; right: 0em;">
                            <v-icon color="white" size="25" class="ma-2">mdi-bookmark-outline</v-icon> 
                        </div>
                        <v-row align="end" class="lightbox white--text  my-5 pa-2 fill-height">
                            <v-col>
                                <div class="subheading">{{ company.name }}</div>
                                <div class="body-1">{{ company.email }}</div>
                            </v-col>
                        </v-row>
                    </v-img>
                    <v-card-actions>
                    <v-rating v-model="rating" background-color="amber accent-4"  color="amber accent-4"></v-rating>
                      </v-card-actions>
                </v-card>
                </v-hover>
            </div>
            <v-divider inset vertical class="mx-2" ></v-divider>
            <div style="width: 400px;" class="ma-5 my-1">
                <v-row no-gutters>
                    <v-col sm="5" md="6">
                        <v-hover>
                         <v-card class="my-2 indigo darken-4 " :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon>mdi-stadium</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="title">Canchas</span>
                                <v-divider inset vertical class="mx-2"></v-divider>
                                <span class="title">{{ company.field_set.length }}</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>
                        <v-card class="my-2 light-green accent-4" :elevation=12 dark height="75" width="170"  style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <v-icon>mdi-trophy</v-icon> 
                                <v-divider inset vertical class="mx-1 transparent"></v-divider>
                                <span class="title">Torneos</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>
                        <v-card class="my-2 orange darken-4" :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <span>Torneos</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                    <v-col sm="5" md="6">
                        <v-hover>   
                        <v-card class="my-2 light-blue darken-4" :elevation=12 dark height="75" width="170" style="border-radius: 20px;">
                            <v-row class="fill-height" align="center" justify="center">
                                <span>Torneos</span>
                            </v-row>
                        </v-card>
                        </v-hover>
                    </v-col>
                </v-row>     
            </div>
        </v-row>
    </div>
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
            colors: [
          'primary',
          'secondary',
          'yellow darken-2',
          'red',
          'orange',
        ],
        rating: 3,
       }
       },
      
    methods: {
        getCompany(){
      const path = `http://192.168.88.222:8000/sport/field-company/${this.companyId}/`   
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