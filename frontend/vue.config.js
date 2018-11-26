const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {

    chainWebpack: webpackConfig => {
        if (process.env.NODE_ENV === 'production') {
          const inlineLimit = 10000;
          const assetsPath = 'static/';
    
          webpackConfig
            .output
            .filename(path.join(assetsPath, 'js/[name].[chunkhash:8].js'))
            .chunkFilename(path.join(assetsPath, '/js/chunk[id].[chunkhash:8].js'))

            // webpackConfig.plugin('extract-css')
            // .use(ExtractTextPlugin, [{
            //   filename: path.join(assetsPath, 'css/[name].[contenthash:8].css'),
            //   allChunks: true
            // }])
            
    //     // webpackConfig.module
    //     //     .rule('css')
    //     //     .test(/\.css$/)
    //     //     .use('url-loader')
    //     //     .loader('url-loader')
    //     //     .options({
    //     //         limit: inlineLimit,
    //     //         name: path.join(assetsPath, 'css/[name].[hash:8].[ext]')
    //     //     })
    
        }
      



    }

}