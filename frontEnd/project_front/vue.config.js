module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    host: "0.0.0.0",
    prot: 3000
    //     proxy: {
    //         '/api': {
    //             target: 'http://localhos:3000',
    //             changeOrigin: true,
    //             pathRewrite: {
    //                 '^/api': ''
    //             }
    //         }
    //     }
  }
};
