module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],

  chainWebpack: config => {
    config.module.rules.delete('eslint');
},

  pluginOptions: {
    quasar: {
      rtlSupport: true,
      treeShake: true
    }
  },

  transpileDependencies: [
    'vuetify',
    /[\\\/]node_modules[\\\/]quasar[\\\/]/
  ]
}
