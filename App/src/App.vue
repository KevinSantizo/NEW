<template>
  <v-app>
    <v-content>
      <router-view> </router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import BottomNavigation from '@/components/BottomNavigation'

export default {
  name: 'App',
  components: {
    
  },
  data: () => ({
    //
  }),
};
</script>
