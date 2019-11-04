<template>
<v-container>

    <span>hola</span>
    <span>Soy: </span>
</v-container>
</template>


<script>
import axios from 'axios'
export default {
    data () {
       return {
          fieldId: this.$route.params.fieldId,
          field: [ ],
       }
    },
    methods: {
        getField() {
      const path = `http://192.168.1.20:8000/sport/field-schedule/${this.fieldId}/`   
        axios.get(path).then((response) => {
        this.field = response.data
        console.log(this.field);       
      }).catch((error) => {
          console.log(error);
        })
        }
    },
    created(){
      this.getField()
    }
}

</script>
