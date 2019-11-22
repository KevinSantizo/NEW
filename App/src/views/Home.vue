<template>
  <v-card class="overflow-hidden ">
    <v-app-bar absolute dark flat text scroll-target="#playground-example" extended  collapse-on-scroll class="back-ground">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="margin-top: 2em;">
        <span class=" font-weight-bold title font">Bienvenido {{ user_name }}</span>
          <v-divider inset vertical class="mx-1"></v-divider>
          <img src="@/assets/balloon.png" app color="white" alt="" style="width: 25px; border-radius: 100px;">
          <v-divider class="my-1"></v-divider>
        <span class=" font-weight-medium subtitle-1 font">Haz tus reservaciones</span>
      </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
    <v-icon outlined class="font-color">mdi-magnify</v-icon>
    </v-btn>           
    </v-app-bar>
    <v-navigation-drawer dense dark absolute v-model="drawer"  temporary class="back-ground" >
      <template v-slot:prepend>
          <v-list-item> 
              <v-avatar class="profile my-5"  size="75"> 
                    <img src="https://static.platzi.com/static/website/v2/images/avatar_default.afdd5b436fc2.png" alt="">
                </v-avatar> 
                <v-divider inset vertical class="mx-2 transparent"> 
                </v-divider> 
                <v-list-item-content>
                    <v-list-item-title  class="font-weight-medium title">{{ name }}</v-list-item-title>
                    <span>{{last_name}}</span>
                </v-list-item-content>
                <v-btn icon @click="drawer = !drawer">
                <v-icon color="grey" size=40>mdi-chevron-left</v-icon>
                </v-btn>
               
          </v-list-item>
        </template>
           <v-divider class="grey darken-1 "></v-divider>
          <v-list shaped>
          <v-list-item-group  v-model="items" class="link" color="amber darken-1">
              <v-list-item  class="link"   v-for="item in items" :key="item.title" router :to="item.to" min-width="2" >
                  <v-list-item-icon>
                      <v-icon medium class="link" size=25>{{ item.icon }}</v-icon>
                  </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title class="font-weight-medium subtitle-1 link">{{ item.title }}</v-list-item-title>
                  </v-list-item-content>
              </v-list-item>
                         <v-divider class="grey darken-1 "></v-divider>

               <v-btn  v-if="isLoggedIn" v-bind:to="{ name: 'logout' }"  small class="ma-2 link" tile text color="white">
                 <v-icon left>mdi-exit-to-app</v-icon> <span>Cerrar Sesión</span>
                
               </v-btn>
              </v-list-item-group>
              
          </v-list>
      </v-navigation-drawer>
    <BottomNavigation/> 
    <v-sheet  id="playground-example" class="overflow-y-auto" max-height=725  >
      <v-container class="bottom" style="height: 100%;">
        <v-row justify="center">
          <v-hover>
              <v-card  router to="/reserve" class="my-1 ma-2 link "  style="border-radius: 10px; background-color: #DF2935 !important;" dark width=375 height=200 :elevation=12>
                <v-avatar size=90 class="ma-1"  style="position: absolute;">
                  <v-img  src="@/assets/reser.jpg" >
                  </v-img>
                </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div  class="subtitle-1 font-weight-bold font">{{ companies.length}} Compañías</div>
                <v-divider inset vertical class="mx-2" ></v-divider>
                <div  class="subtitle-1 font-weight-bold font">{{ fields.length}} Canchas</div>
              </v-row>
                <span text class=" font-weight-bold title font ma-3" style="bottom: -0.5em; position: absolute; right: 0em;">Reservar<v-icon right size="20">mdi-calendar</v-icon>
                </span>
              </v-card>
          </v-hover>
          <v-hover>
            <v-card  router to="/companies" class="my-1 link ma-1 "  style="border-radius: 10px; background-color: #004E64" dark width=375 height=200 :elevation=12>
            <v-avatar size=90 class="ma-1"  style="position: absolute;">
              <v-img  src="@/assets/centro.jpg" >
              </v-img>
            </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="headline font-weight-bold font">{{ companies.length}}</div>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Compañías<v-icon right size="20">mdi-domain</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card class=" link my-1 ma-1 "  style="border-radius: 10px; background-color: #0EB588;" dark width=375 height=200 :elevation=12>
              <v-avatar size=90 class="ma-1"  style="position: absolute;">
                <v-img  src="@/assets/favorite.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="subtitle-1 font-weight-bold font">Canchas Favoritas</div>
              </v-row>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Favoritas<v-icon right size="20">mdi-star-outline</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card disabled  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" class="my-1 link accent-4 ma-1 "  style="border-radius: 10px; background-color: #FF0022" dark width=375 height=200 :elevation=12 >
              <v-avatar size=90 class="ma-1" style="position: absolute;">
                <v-img  src="@/assets/oliver.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                <div class="subtitle-1 font-weight-bold font">Buscar Chamuscas</div>
                  <v-divider inset vertical class="mx-1"></v-divider>
                                <v-avatar size=90 class="ma-1" >

                 <v-img  src="@/assets/prox.png" >
                </v-img>
                              </v-avatar>
              </v-row>
              <v-row class="pa-5">
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Chamusca<v-icon right size="20">mdi-soccer</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
          <v-hover>
            <v-card disabled  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" class="link my-1 ma-1 "  style="border-radius: 10px; background-color: #FED766;" dark width=375  height=200 :elevation=12>
              <v-avatar size=75 class="ma-3" style="position: absolute;">
                <v-img  src="@/assets/torneo.jpg">
                </v-img>
              </v-avatar>
              <v-row class="fill-height pa-4" align="center" justify="center">   
              <v-avatar size=75 class="ma-3 profile">                    
                 <v-img  src="@/assets/prox.png" style="width: 35px; height: 75px;" >
                </v-img>
              </v-avatar>
              </v-row>
              <v-row class="pa-5"> 
                <span text center class=" font-weight-bold title font ma-2" style="bottom: -0.5em; position: absolute; right: 0em;">Torneos<v-icon right size="20">mdi-trophy</v-icon></span>
              </v-row>
            </v-card>
          </v-hover>
        </v-row>
      </v-container>
    </v-sheet>      
  </v-card>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'
  export default {
          components: {
        BottomNavigation
  },
    data () {
      return {
        modalShow: false,
        reservations: [ ] ,
        user_reservations: [],
        companies: [ ],
        fields: [ ],     
        users: [ ],
        user_name: '',
        name: '',
        last_name: '',
        drawer: false, 
        items : [
                {title: 'Inicio', icon: 'mdi-home', to  : '/home'},
                {title: 'Mis Reservaciones', icon: 'mdi-calendar', to: '/account'},
            ],
        }
    },

    mounted(){
        //const path = 'https://api-backend-canchas.herokuapp.com/api/reservations/'
        const path = 'http://192.168.88.222:8000/api/companies/'
          axios.get(path).then((response) => {
          this.companies = response.data
          //console.log(this.companies);
           
          return axios.get('http://192.168.88.222:8000/api/fields/')
          }).then((response) => {
            this.fields = response.data
            //console.log(this.fields);
          })
         
  },

    computed: {
     isLoggedIn (){
       return this.$store.getters.isLoggedIn
   }
  },
  methods: {
    getUser(){
      const path = 'http://192.168.88.222:8000/api/users/'
      axios.get(path).then((response) =>{
        this.users = response.data
        //console.log(this.users);
        let find_user = this.users.find (v => v.id == this.$store.state.user)
        this.user_name = find_user.username
        this.name = find_user.first_name
        this.last_name = find_user.last_name
        //console.log(this.user_name);
        //console.log('Username ' +find_user.username);
      })
    },

  },
    created(){
      this.getUser()
    }

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
   .link{
      text-decoration:  none !important;
   }
   .container {
     max-width: 100%;
     max-height: 100%;
   }
  .bottom {
     padding-bottom: 70px;
     margin-top: 100px;
   }
   .back-ground {
    background-color: #011427 !important;
  }
  .font-color {
    color: #011427;
  }
  .border-1 {
    border-radius: 0px 0px 50px 50px;
  }
</style>