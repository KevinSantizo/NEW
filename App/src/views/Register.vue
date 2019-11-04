<template>
    <v-container class="indigo lighten-5"  style="height: 100%; width: 35%;">
            <div class="form-group ma-2">
                <v-btn class="my-3" block  color="light-blue darken-4 white--text" ><v-icon left size="25">mdi-facebook</v-icon> REGÍSTRATE CON FACEBOOK</v-btn>
                <v-btn block  color="red darken-1 white--text" ><v-icon left size="25">mdi-google-plus</v-icon> REGÍSTRATE CON GOOGLE</v-btn>
                    <v-divider class="my-3"></v-divider>
                    <v-row justify="center">
                    <div style="position: absolute; top: 7em;">
                    <form>
                        <div class="row">
                        <div class="col">
                            <label for="name" class="font font-weight-medium">Nombre</label>
                            <input type="text" class="form-control form-control-sm" id="name" placeholder="Ingrese su nombre">
                        </div>
                        <div class=" col">
                            <label for="last_name"  class="font font-weight-medium">Apellido</label>
                            <input type="text" class="form-control form-control-sm" style="top: 0em;" id="last_name" placeholder="Ingrese su apellido">
                        </div>
                        </div>
                         <label for="department"  class="font font-weight-medium" >Departamento</label>
                         <select class="form-control form-control-sm" id="department">
                            <option  v-for="(dep, i) in departments" :key=i :value="dep.id">{{ dep.name }}</option>
                        </select>
                        <label for="town"  class="font font-weight-medium my-2">Municipio</label>
                         <select class="form-control form-control-sm" id="town">
                            <option v-for="(municipio, i) in departments.town_set" :key="i" :value=" municipio.id ">{{ municipio.name }}</option>
                        </select>
                         <div class="" >
                            <label for="phone"  class="font font-weight-medium my-2">Teléfono</label>
                            <input type="text" class="form-control form-control-sm" style="top: 0em;" id="phone" placeholder="Ingrese su teléfono">
                        </div>
                         <div class="" >
                            <label for="email"  class="font font-weight-medium my-2">Email</label>
                            <input type="text" class="form-control form-control-sm" style="top: 0em;" id="email" placeholder="Ingrese su e-mail">
                        </div>
                        <div class="" >
                            <label for="password"  class="font font-weight-medium my-2">Email</label>
                            <input type="password" class="form-control form-control-sm" style="top: 0em;" id="password" placeholder="Ingrese su contraseña">
                        </div>
                       
                        <v-row justify="center" class="my-4">
                        <button type="submit" class="btn btn-primary">Submit</button>
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
            </v-row>
            </div>
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
</style>
