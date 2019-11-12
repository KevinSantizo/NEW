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
      <form @submit="onSubmit">
        <v-hover>
          <v-card :elevation=12 style="border-radius: 25px;">
            <v-card-title class="back-ground">
              <v-row justify="center">
                <span class="white--text title font" v-if="field.type == 1">Cancha {{ field.name }} de 5 Jugadores </span>
                <span class="white--text title font" v-else-if="field.type == 2">Cancha {{ field.name }} de 7 Jugadores </span>
                <span class="white--text title font" v-else>Cancha {{ field.name }} de 11 Jugadores </span>
              </v-row>
            </v-card-title>
          <v-card-text>
            <span class="black--text font-weight-medium font">{{field.company.name}} , {{field.company.town.name}}</span><br>
          <v-row justify="center">
            <div class="form-group" style="width: 50%;">
              <label for="customer">Cliente</label>
                    <select name="customer_reserve"  class="form-control font" v-model.trim="form.customer_reserve" style="border: 1px solid #011427 !important;" >
                      <option  v-for="(customer, i)  in customers" :key="i" :id="customer.id" :value="customer.id" >{{customer.first_name}} {{customer.last_name}}</option>
                    </select>
                    <select  name="field_reserve"  class="form-control font" v-model.trim="form.field_reserve" style="border: 1px solid #011427 !important;" >
                      <option :id="field.id" :value="field.id" selected>{{field.name}} {{field.price}}</option>
                    </select>
                    <!--<input type="text" disabled name="field_reserve" :value="field.id" v-model.trim="form.field_reserve" class="form-control"  readonly>-->
              </div>
           </v-row>  
          <v-hover >
            <v-card max-width="100%" height=100 color="back-ground" >
              <v-card-text>
                <v-row justify="center">
                  <div class="subtitle-1 white--text font-weight-medium font">Horarios</div>
                </v-row>

                <v-row justify="center" align="center"> 
                  <div class="form-group" style="width: 50%;">
                    <select class="form-control transparent font" name="schedule" v-model.trim="form.schedule" id="exampleFormControlSelect1" style="border: 1px solid white !important;" >
                      <option  v-for="(time, i)  in schedules" :key="i" :id="time.id" :value="time.id" v-if="time.field.id == field.id " >{{ time.start_time }}</option>
                    </select>
                  </div>
                </v-row> 

              <!--<v-chip-group column multiple active-class="lime accent-3 black--text" >
              <v-row justify="space-around" class="ma-2">
              <v-chip small v-for="(time, i)  in schedules" :key="i" v-if="time.field.id == field.id ">
              {{ time.start_time }}
              </v-chip>
              </v-row>
              </v-chip-group>-->
              </v-card-text>
            </v-card>
      </v-hover>
      <v-divider></v-divider>
      <div class="form-group">
        <label for="date">Fecha:</label>
          <input type="date" name="schedule_date" v-model.trim="form.schedule_date" class="form-control" id="date" >
        </div>                                    
      <!--<span class="black--text font-weight-medium font">Resto de la semana <span class="caption grey--text" >(Próximamente)</span></span>
      <v-slide-group show-arrows>
      <v-slide-item
      v-for="(day, i) in days"
      :key="i"
      v-slot:default="{ active, toggle }"
      >
      <v-btn
      disabled
      small
      class="mx-2 font"
      :input-value="active"
      active-class="lime accent-3 black--text"
      depressed
      rounded
      @click="toggle"
      >
      {{ day }}
      </v-btn>
      </v-slide-item>
      </v-slide-group> -->  
        <v-divider class="ma-1"></v-divider>                                 
         <!--<div class=" black--text font-weight-medium font">Extras: <span class="ma-2 font "  v-for="(implement, i) in this.implements" :key="i">{{ implement.name }} +Q{{ implement.price}}</span></div>        
          <v-row v-for="(implem, i) in this.implements" :key="i"  class="my-3">
            <v-row   justify="center">
              <input type="checkbox" class="chk pa-4 checkbox-label" @click="checkbox('chk-'+implem.id, 'txt-'+implem.id)" :id="'chk-'+implem.id" :value="implem.name" :v-model="implem.name">
                <v-avatar size="30" class="ma-2" style="right: 0em; bottom: 0.5em;">
                  <img :src="implem.image" alt="implement">
                </v-avatar>
              <input type="number" input="test()" style="border: 1px solid grey !important; width: 75px;" class="form-control form-control-sm" :id="'txt-'+implem.id" disabled  min=0 max=50  placeholder="Cant.">
            </v-row>
          </v-row>-->
          <select   name="total"  class="form-control font" v-model.trim="form.total" style="border: 1px solid #011427 !important;" >
            <option :value="field.price" selected>{{field.price}}</option>
          </select>
        <span>Total: {{ field.price }}</span>
      </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
            <v-btn color="red accent-4"  class="link" outlineded text  router to='/home'>Cancelar</v-btn>
            <v-btn type="submit" color="light-green accent-4" outlined>Guardar</v-btn>
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
import swal from 'sweetalert'

export default {
    data () {
       return {
          fieldId: this.$route.params.fieldId,
          field: [ ],
          company: [],
          implements: [ ],
          schedules: [ ],
          customers: [ ],
          enabled: false,
          months: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
          dayss: ['Dom', 'Lun', 'Ma', 'Mie', 'Jue', 'Vie', 'Sab'],
          form: {
            schedule_date:'',
            total:'',
            schedule:'',
            customer_reserve:'',
            field_reserve:'',
            implement:'',
          },
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
        //const path = `http://192.168.88.222:8000/sport/field-schedule/${this.fieldId}/`   
        const path = `http://192.168.1.104:8000/sport/field-schedule/${this.fieldId}/`   
        axios.get(path).then((response) => {
        this.field = response.data
        console.log(this.field);           
        //return axios.get('http://192.168.88.222:8000/sport/implements/')  
        return axios.get('http://192.168.1.104:8000/sport/implements/')
      }).then((response)=>{
        this.implements = response.data
        console.log(this.implements);
        
        return axios.get('http://192.168.1.104:8000/sport/count/')
      }).then((response) => {
        this.schedules = response.data
        console.log(this.schedules);
        
        return axios.get('http://192.168.1.104:8000/user/do-customer/')
      }).then((response)=>{
        this.customers = response.data
        console.log(this.customers);
        
      }).catch((error) => {
          console.log(error);
        })
        },
        checkbox(_chk_id, _txt_id){
          let check = document.getElementById(_chk_id)
          let elementNum = document.getElementById(_txt_id)
          if(check.checked == true){
                elementNum.disabled = false
          }
          else{
            elementNum.disabled = true
          }
        },
        onSubmit(evt){
            event.preventDefault()
            const path = 'http://192.168.1.104:8000/sport/do-reservation/'
            //const path = 'http://192.168.88.222:8000/user/do-customer/'
            axios.post(path, this.form).then((response) => {
                this.form.schedule = response.data.schedule
                this.form.total = response.data.total
                this.form.schedule = response.data.schedule
                this.form.customer_reserve = response.data.customer_reserve
                this.form.field_reserve = response.data.field_reserve
                this.form.implement = response.data.implement
                swal("Reservación creada exitosamente", "", "success")
                this.$router.push({ name: 'home' })
            }).catch((error) => {
                swal("Reservación no creada", "", "error")  
            })
        }
    },
    created(){
      this.getField()
    },

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900');
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