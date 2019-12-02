<template>
<<<<<<< HEAD
  <v-bottom-navigation class="back-ground border" dark fixed height=60>
    <v-btn fab icon class="link ma-2 " color="amber lighten-5" router to="/home" >
      <!--<span class="caption font-weight-bold font">Inicio</span>-->
      <v-icon app text size=35 color="amber lighten-5">mdi-home-outline</v-icon>
=======
 <v-bottom-navigation v-model="bottomNav" grow class="grey lighten-2" color="indigo" fixed>
    <v-btn fab class="link" router to="/home">
      <span class="font">Inicio</span>
      <v-icon size=30>mdi-home</v-icon>
>>>>>>> 92b61887b36fbc93c09062244d089c54d2d2edf8
    </v-btn>
    <v-btn fab class="link " router to="/reserve">
      <span class="font">Reservar</span>
      <v-icon size=30>mdi-plus-box</v-icon>
    </v-btn>

    <v-btn fab class="link" router to="/account">
      <span class="font">Mi Perfil</span>
      <v-icon size=30>mdi-account</v-icon>
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
        bottomNav: 'recent',      
        color: false,
        selected: []
    })
}
</script>
<style scoped>
   @import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
   .font {
     font-family: 'Ubuntu', sans-serif;
   }
   .link {
     text-decoration: none !important;
   }
   .back-ground {
    background-color: #011427;
  }
  .border {
<<<<<<< HEAD
    border-radius: 25px 25px 0px 0px;
=======
    border-radius: 35px 35px 0px 0px;
>>>>>>> 92b61887b36fbc93c09062244d089c54d2d2edf8
  }
</style>