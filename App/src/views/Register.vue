<template>
    <v-container height="100%" class="my-0">
        <v-row justify="center" align="center" >
            <div class="form-group ma-3">
                <v-btn class="my-1" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                    <v-divider class="my-2"></v-divider>
                    <div style="margin-top: -1em !important;">
                    <form  @submit.prevent="register">
                        <div class="row">
                        <div class="col">
                            <label for="name" class="font font-weight-medium body-2">Nombre</label>
                            <input type="text" name="first_name" v-model="form.first_name" class="form-control  border font body-2 transparent" required style="border: 1px solid grey !important;" id="name" placeholder="Ingrese su nombre">
                        </div>
                        <div class=" col">
                            <label for="last_name"  class="font font-weight-medium body-2">Apellido</label>
                            <input type="text" name="last_name" v-model="form.last_name" class="form-control  border font body-2 transparent" required style="border: 1px solid grey !important;" id="last_name" placeholder="Ingrese su apellido">
                        </div>
                        </div>
                        <div class="" > 
                            <label for="username"  class="font font-weight-medium my-2 body-2">Nombre de Usuario</label>
                            <input type="text" name="username" v-model="form.username" class="form-control  border font body-2 transparent" required style="border: 1px solid grey !important;" id="username" placeholder="Elja un nombre de usuario">
                        </div>
                        <label for="town"  class="font font-weight-medium my-2 body-2">Municipio</label>
                         <select name="town" v-model="form.town" class="form-control  border body-2 transparent" required style="border: 1px solid grey !important;" id="town">
                            <option value="" disabled>Elija una opción</option>
                            <option v-for="(dep, i) in departments" :key=i :id="dep.id" :value="dep.id">{{ dep.name }}, {{dep.department.name}}</option>
                        </select>
                        <!-- <label for="">This: {{selected}}</label><br>-->
                        
                         <div class="" >
                            <label for="phone"  class="font font-weight-medium my-2 body-2">Teléfono</label>
                            <input type="text" name="phone" v-model="form.phone" class="form-control  border font body-2 transparent" required style="border: 1px solid grey !important;" id="phone" placeholder="Ingrese su teléfono">
                        </div>
                         <div class="" >
                            <label for="email"  class="font font-weight-medium my-2 body-2">Email</label>
                            <input type="email" name="email" v-model="form.email" class="form-control  border font body-2 transparent" required style="border: 1px solid grey !important;" id="email" placeholder="Ingrese su e-mail">
                        </div>
                        <div class="" >
                            <label for="password"  class="font font-weight-medium my-2 body-2">Contraseña</label>
                            <input type="password" name="password" v-model="form.password" class="form-control border font body-2 transparent" required style="border: 1px solid grey !important;" id="password" placeholder="Ingrese su contraseña">
                        </div>
                        <v-row justify="center" class="my-1 ma-0">
                            <v-btn block  type="submit" color="light-green accent-4 white--text" class="font link my-3" >REGISTRARSE</v-btn>          
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
            const path = 'http://192.168.88.222:8000/api/towns/'
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
