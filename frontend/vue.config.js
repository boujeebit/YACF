const path = require('path');

module.exports = {
    devServer: {
        proxy: 'http://localhost:8000'
    },

    chainWebpack: webpackConfig => {
        if (process.env.NODE_ENV === 'production') {
          const inlineLimit = 10000;
          const assetsPath = 'static/';
    
          webpackConfig
            .output
            .filename(path.join(assetsPath, 'js/[name].[chunkhash:8].js'))
            .chunkFilename(path.join(assetsPath, '/js/chunk[id].[chunkhash:8].js'))
        }
    }
}