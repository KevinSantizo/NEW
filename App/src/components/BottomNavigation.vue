<template>
  <v-bottom-navigation class="back-ground border" dark absolute height=60>
    <v-btn icon class="link ma-2" router to="/home" >
      <!--<span class="caption font-weight-bold font">Inicio</span>-->
      <v-icon app text size=35>mdi-home-outline</v-icon>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn  icon class="link ma-2">
      <!--<span class="caption font-weight-bold font">Partidos</span>-->
      <v-icon size=35>mdi-soccer</v-icon>
    </v-btn>
    <v-spacer></v-spacer>
     <v-btn icon class="link ma-2"  router to="/companies" >
      <!--<span  class="caption font-weight-bold font">Torneos</span>-->
      <v-icon size=35>mdi-domain</v-icon>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn icon class="link ma-2" router to="/account" >
      <!--<span class="caption font-weight-bold font">Mi Perfil</span>-->
      <v-icon size=35>mdi-account-outline</v-icon>
    </v-btn>

  </v-bottom-navigation>
</template>

<script>
export default {
    data:() => ({
        show: false,
        selected: [],
        expand: false,
        expand2: false,
        months: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',],
        activeBtn: 1,
        showNav: true,
        color: false
    })
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
   .back-ground {
    background-color: #011427;
  }
  .border {
    border-radius: 50px 50px 0px 0px;
  }
</style>