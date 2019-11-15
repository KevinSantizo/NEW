<template>
    <v-container height="100%" class="my-0">
        <v-card>
             <form  @submit.prevent="register">
        <v-card-text>
          <v-container>
            <v-row>
                  <v-btn class="my-1" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                    <v-divider ></v-divider>
              <v-col cols="12" sm="6" >
                    <label for="first_name">Nombre</label>
                    <input v-model="form.first_name" type="text" class="form-control form-control-sm border caption" id="first_name" placeholder="Ingresa tu nombre">
              </v-col>
              <v-col cols="12" sm="6" md="4">
                    <label for="last_name">Apellido</label>
                    <input v-model="form.last_name" type="text" class="form-control form-control-sm border caption" id="last_name" placeholder="Ingresa tu apellido">
              </v-col>
              <v-col cols="12" sm="6" md="4"    >
                    <label for="user_name">Nombre de usuario</label>
                    <input v-model="form.username" type="text" class="form-control  form-control-sm border caption" id="user_name" placeholder="Ingresa un nombre de usuario. Ej. user1019">              
                </v-col>
               <v-col cols="12"   sm="6" >
                <label for="email">Email</label>
                    <input v-model="form.email" type="email" class="form-control form-control-sm border caption" id="email" placeholder="Ingresa tu correo electrónico">             
                </v-col>
                <v-col cols="12" sm="6">
                    <label for="town">Municipio</label>
                    <select class="form-control form-control-sm" id="town"  v-model="form.town">
                        <option value="" disabled>Seleccione su Municipio...</option>
                        <option v-for="(town, i) in departments" :key="i" :value="town.id" :id="town.id">{{town.name}}, {{town.department.name}}</option>
                    </select>
              </v-col>
            <v-col cols="12" sm="6" >
                <label for="phone">Teléfono</label>
                    <input v-model="form.phone" type="text" class="form-control form-control-sm border caption" id="phone" placeholder="Ingresa tu número de teléfono">
            </v-col>
            <v-col cols="12" sm="6" >
                <label for="password">Contraseña</label>
                <input v-model="form.password" type="password" class="form-control form-control-sm border caption" id="password" placeholder="Ingresa tu número de contraseña">           
            </v-col>
            <v-row justify="center" class="ma-1" >
                <v-btn block  type="submit" color="light-green accent-4 white--text" class="font link my-3" >REGISTRARSE</v-btn>          
            </v-row>
            </v-row>
          </v-container>
        </v-card-text>
                </form>
        <template >
                    <v-col>
                    <v-row justify="center" align="center" class="">
                        <div>
                        <span class="caption">¿Ya tienes una cuenta? </span>
                        </div>
                        <v-divider inset vertical class="mx-1"></v-divider>
                        <div>
                        <router-link class="caption" :to="{name: 'login'}"><span>Inicia Sesión</span></router-link>
                        </div>
                    </v-row>
                    <v-row justify="center" align="center" class="my-1">
                        <img src="@/assets/ball.svg" alt="" style="width: 35px;">
                    </v-row>
                    </v-col>
                </template>
      </v-card>
    </v-container>
</template>


<script>
import axios from'axios'
import swal from 'sweetalert'
    export default {
         data(){
             return {
                 departments: [],   
                 selected: '',
                 form: {
                     town: '',
                     first_name: '',
                     last_name:'',
                     username:'',
                     phone:'',
                     email:'',
                     password:'',
                     is_admin: null,
                 }
             }
         },

    methods: {
        getDepartments(){            
            //const path = 'http://192.168.88.222:8000/user/towns/'
            const path = 'http:///127.0.0.1:8000/api/towns/'
            axios.get(path).then((response) => {
                this.departments = response.data
                console.log(this.departments);
            }).catch((error) => {
                console.log(error);
            })
        },
        register (){
            let data = {
                town: this.form.town,
                first_name: this.form.first_name,
                last_name: this.form.last_name,
                username: this.form.username,
                phone: this.form.phone,
                email: this.form.email,
                password: this.form.password,
                is_admin: this.form.is_admin
            }
             
            this.$store.dispatch('register', data).then(() =>  
            swal("Usuario creado exitosamente", "", "success"), 
            this.$router.push('/')).catch(err => console.log(err))
        }

       /*
          getTown(){
              for (const dep in this.departments) {
                let x = document.getElementById(dep.id).selected
                console.log(x);
              }
            }*/
            
        },
    created(){
        this.getDepartments()
    },
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
.form {
   margin-top: 0em;
}

.form1 {
    margin-top: -0.5em;
}
.font {
    font-family: 'Ubuntu', sans-serif;
}
.border {
    border: 1px solid teal !important;

}
</style>
