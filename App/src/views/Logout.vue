<template>
    
</template>

<script>
export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },
    created (){
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    }
}
</script>