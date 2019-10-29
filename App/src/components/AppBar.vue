<template>
  <v-app-bar  flat text app class="grey lighten-4"  height="57">
        <v-layout row wrap>
            <v-flex xs12 md12>
            <v-row justify="center" align="center">
                <v-icon color="black" size="15" >mdi-map-marker</v-icon><span class="font-weight-bold subtitle-1">Quetzaltenango, quetzaltenango</span>
            </v-row>
            <v-row justify="center" align="center">
                <v-icon color="black" size="15">mdi-calendar</v-icon><span class="font-weight-bold caption" >{{ this.days[new Date().getDay() ]}},{{ new Date().getDate()}} de {{  this.months[new Date().getMonth()] }} {{ new Date().getFullYear() }}</span>
            </v-row>
            </v-flex>
        </v-layout>
    </v-app-bar>
</template>

<script>
export default {
  data: () => ({
        
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        
    }),
     components: { BottomNavigation },
    methods: {
    },
}
</script>

<style scoped>
  
</style>
