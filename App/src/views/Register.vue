<template>
    <v-container height="100%" class="my-8">
        <v-row justify="center" align="center" >
            <div class="form-group ma-3">
                <!--<v-btn class="my-1" disabled block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block disabled color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>-->
                    <v-row justify="center">
                        <span class="display-1 font ">Registro</span>
                    </v-row>
                    <v-divider class="my-2"></v-divider>
                    <div style="margin-top: -0.5em !important;">
                    <form  @submit.prevent="register">
                        <div class="row">
                        <div class="col">
                            <v-text-field outlined name="first_name" class="font" v-model="form.first_name" required  id="name" dense label="Nombres"></v-text-field>
                        </div>
                        <div class=" col">
                            <v-text-field outlined name="last_name" class="font" v-model="form.last_name" dense label="Apellidos"></v-text-field>
                        </div>
                        </div>
                        <div class="" > 
                            <v-text-field outlined  name="username" class="font" v-model="form.username" dense label="Elija un nombre de usuario"></v-text-field>
                        </div>
                        <v-select dense item-text="name" class="font" item-value="id" outlined v-model="form.town"  :items="departments" label="Municipio" required></v-select>                        
                         <div class="" >
                            <v-text-field  name="phone" class="font" v-model="form.phone" label="Ingrese su teléfono" dense outlined></v-text-field>
                        </div>
                         <div class="" >
                            <v-text-field name="email" dense outlined class="font" :rules="emailRules" v-model="form.email" label="Ingrese su e-mail"></v-text-field> 
                        </div>
                        <div class="" >
                            <v-text-field name="password" v-model="form.password" outlined class=" font" @click:append="show1 = !show1" dense label="Ingrese su contraseña" required :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :type="show1 ? 'text' : 'password'"></v-text-field>
                        </div>
                        <v-row justify="center" class="my-1 ma-0">
                            <v-btn block dark :elevation=10 type="submit" color="light-green accent-4" class="font link my-3" >REGISTRARSE</v-btn>          
                        </v-row>
                    </form>
                    <v-divider class="my-1"></v-divider>
                <template>
                    <v-row justify="center" align="center" class="my-1">
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
                </template>
                </div>
            </div>
        </v-row>
    </v-container>
</template>

<script>
import axios from'axios'
import swal from 'sweetalert'

let URL =  'https://api-backend-canchas.herokuapp.com/'
    export default {
         data(){
             return {
                 departments: [],   
                 selected: '',
                show1: false,
                 emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /.+@.+\..+/.test(v) || 'El correo debe ser válido. (example@outlook.com)',
                ],
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
            const path = URL+'api/towns/'
            //const path = 'https://api-backend-canchas.herokuapp.com/api/towns/'
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
            this.$router.push('/'))
        },

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
