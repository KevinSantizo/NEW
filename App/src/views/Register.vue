<template>
    <v-container height="100%" class="my-0">
        <v-row justify="center" align="center" >
            <div class="form-group ma-3">
                <v-btn class="my-1" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                    <v-divider class="my-2"></v-divider>
                    <div style="margin-top: -1em !important;">
                    <form>
                        <div class="row">
                        <div class="col">
                            <label for="name" class="font font-weight-medium body-2">Nombre</label>
                            <input type="text" class="form-control  border font body-2 transparent" style="border: 1px solid grey !important;" id="name" placeholder="Ingrese su nombre">
                        </div>
                        <div class=" col">
                            <label for="last_name"  class="font font-weight-medium body-2">Apellido</label>
                            <input type="text" class="form-control  border font body-2 transparent" style="border: 1px solid grey !important;" id="last_name" placeholder="Ingrese su apellido">
                        </div>
                        </div>
                         <label for="department"  class="font font-weight-medium body-2" >Departamento</label>
                         <select class="form-control border body-2 transparent" style="border: 1px solid grey !important;" id="department">
                            <option  v-for="(dep, i) in departments" :key=i :value="dep.id">{{ dep.name }}</option>
                        </select>
                        <label for="town"  class="font font-weight-medium my-2 body-2">Municipio</label>
                         <select class="form-control  border body-2 transparent" style="border: 1px solid grey !important;" id="town">
                            <option v-for="(municipio, i) in departments.town_set" :key="i" :value=" municipio.id ">{{ municipio.name }}</option>
                        </select>
                         <div class="" >
                            <label for="phone"  class="font font-weight-medium my-2 body-2">Teléfono</label>
                            <input type="text" class="form-control  border font body-2 transparent" style="border: 1px solid grey !important;" id="phone" placeholder="Ingrese su teléfono">
                        </div>
                         <div class="" >
                            <label for="email"  class="font font-weight-medium my-2 body-2">Email</label>
                            <input type="text" class="form-control  border font body-2 transparent" style="border: 1px solid grey !important;" id="email" placeholder="Ingrese su e-mail">
                        </div>
                        <div class="" >
                            <label for="password"  class="font font-weight-medium my-2 body-2">Contraseña</label>
                            <input type="password" class="form-control border font body-2 transparent" style="border: 1px solid grey !important;" id="password" placeholder="Ingrese su contraseña">
                        </div>
                        <v-row justify="center" class="my-1 ma-0">
                            <v-btn block  color="light-green accent-4 white--text" class="font link my-3" router to="/home" >REGISTRARSE</v-btn>          
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
    export default {
         data(){
             return {
                 departments: [],   
             }
         },

    methods: {
        getDepartments(){
            const path = 'http://127.0.0.1:8000/sport/department-child/'
            axios.get(path).then((response) => {
                this.departments = response.data
                console.log(this.departments);
            }).catch((error) => {
                console.log(error);
            })
        }
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
    border: 1px solid grey !important;

}
</style>
