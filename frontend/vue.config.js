// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  devServer: {
    proxy: {
      '/upload': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  }
}
