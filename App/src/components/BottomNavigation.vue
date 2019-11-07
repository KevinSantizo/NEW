<template>
  <v-bottom-navigation class="back-ground" dark absolute height=75>
    <v-btn class="link" router to="/home" >
      <span class="caption font-weight-bold font">Inicio</span>
      <v-icon size=20>mdi-home</v-icon>
    </v-btn>
    <v-btn class="link" router to="/companies" >
      <span class="caption font-weight-bold font">Compañías</span>
      <v-icon size=20>mdi-domain</v-icon>
    </v-btn>
     <v-btn class="link" router to="/reserve" >
      <span  class="caption font-weight-bold font" >Reservar</span>
      <v-icon size=20>mdi-calendar</v-icon>
    </v-btn>
    <v-btn class="link" router to="/account" >
      <span class="caption font-weight-bold font">Mi Perfil</span>
      <v-icon size=20>mdi-account</v-icon>
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
     position: absolute;
     max-width: 100%;
   }
   .description {
     position: absolute;
     margin-top: 6.5em;
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
     margin-bottom:  10px;
   }
   .link {
     text-decoration: none;
   }
   .back-ground {
    background-color: #011427;
  }
</style>