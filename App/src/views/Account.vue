<template>
   <v-card  class="overflow-hidden mx-auto indigo">
        <v-toolbar extended prominent flat text app class="indigo" dark height="57">
          <v-divider inset class="transparent" vertical></v-divider>
            <v-avatar size="75" style="top: 0.5em;">
              <img src="https://static.platzi.com/static/website/v2/images/avatar_default.afdd5b436fc2.png" alt="Avatar">
            </v-avatar>
              <v-toolbar-title class="font title" style="top: 0.3em; left: 4.5em; position: absolute;">Kevin Santizo</v-toolbar-title>
               <v-toolbar-items style="top: 2em; left: 5em; position: absolute;">
                <v-btn text small>News</v-btn>
                <v-divider inset vertical></v-divider>
                <v-btn text small>Blog</v-btn>
                <v-divider inset vertical></v-divider>
                <v-btn text small>Music</v-btn>
                <v-divider inset vertical></v-divider>
              </v-toolbar-items>
            <v-spacer>
            </v-spacer>
            <v-btn icon text>
          <v-icon color="white" size="25" class="my-2">mdi-settings</v-icon>
            </v-btn>
        </v-toolbar>
              <BottomNavigation/>
      <v-sheet  id="scroll-area-1"  class="overflow-y-auto indigo lighten-5" style="border-radius: 25px 25px 0px 0px;" max-height="620">
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            v
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>
            <div class="ma-3">
              <span>hola</span>
            </div>

      </v-sheet>
 </v-card>
</template>

<script>
import axios from 'axios'
import BottomNavigation from '@/components/BottomNavigation'

export default {
  data: () => ({
        
    }),
     components: {
    BottomNavigation
  },
   
    
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Ubuntu&display=swap');
  .font {
     font-family: 'Ubuntu', sans-serif;
   }
  
</style>
