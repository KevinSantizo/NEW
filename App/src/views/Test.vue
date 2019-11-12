    <template>
  <v-container class="grey lighten-5">
    <v-row no-gutters >
      <template>
        <v-col cols="6">
          <v-card height="150" width="100%"  outlined tile>
              <v-row class="ma-4 my-6" align="center" justify="center">                       
                  <v-img   width=100 height=100 src="@/assets/toreserve.jpg" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)">
                  <v-row class="fill-height" align="center" justify="center">                    
                    <span class="title font-weight-light white--text font">Reservar<v-icon size=15 color=white>mdi-calendar</v-icon></span>
                   </v-row>  
                    <span  class="body-1 font-weight-bold font">{{ companies.length}} Compañías</span>
                </v-img>
                                <!--  <div  class="subtitle-1 font-weight-bold font">{{ companies.length}} Compañías</div>
                  <div  class="subtitle-1 font-weight-bold font">{{ fields.length}} Canchas</div>-->
              </v-row>

          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card class="" height="150" outlined >
              <v-row class="fill-height pa-4" align="center" justify="center">                       
                  <div  class="subtitle-1 font-weight-bold font">{{ companies.length}} Compañías</div>
                  <v-divider inset vertical class="mx-2" ></v-divider>
                  <div  class="subtitle-1 font-weight-bold font">{{ fields.length}} Canchas</div>
              </v-row>
                <span text class=" font-weight-bold title font ma-3" style="bottom: -0.5em; position: absolute; right: 0em;">Reservar<v-icon right size="20">mdi-calendar</v-icon>
                </span>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card class="" height="150" outlined tile>
              Column
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card class="pa-2" height="150" outlined tile>
              Column
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card class="pa-2" height="150" outlined tile>
              Column
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card class="pa-2" height="150" outlined tile>
              Column
          </v-card>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>


<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

  export default {
    data: () => ({
        modalShow: false,
        reservations: [ ] ,
        companies: [ ],
        fields: [ ],      
    }),
      components: {
        BottomNavigation
  },
    methods: {
      getAll(){ 
      const path = 'http://192.168.1.109:8000/sport/reservations/'
      //const path = 'http://192.168.88.222:8000/sport/reservations/'
      axios.get(path).then((response) => {
        this.reservations = response.data
        console.log(this.reservations);
        
        return axios.get('http://192.168.1.109:8000/sport/companies/')
        //return axios.get('http://192.168.88.222:8000/sport/companies/');
        }).then((response) => {
          this.companies = response.data
          console.log(this.companies);
          
          return axios.get('http://192.168.1.109:8000/sport/fields/')
        }).then((response) => {
          this.fields = response.data
          console.log(this.fields);
          let d = new Date()
          let n = d.getHours()
          console.log(n);
          
        }).catch((error) => {
          console.log(error);
        })
        },
    },
    created(){
      this.getAll()
    },

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
      text-decoration:  none;
   }
   .container {
     max-width: 100%;
     max-height: 100%;

   }
   .description {
     position: absolute;
     margin-top: 3.5em;
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
     padding-bottom: 70px;
     margin-top: 100px;
   }
   .back-ground {
    background-color: #011427;
  }
  .font-color {
    color: #011427;
  }
  .border-1 {
    border-radius: 0px 0px 50px 50px;
  }
</style>