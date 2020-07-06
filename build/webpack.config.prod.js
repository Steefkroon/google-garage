'use strict'

const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    context: path.join(__dirname, '../web'),
    mode: 'production',
    entry: [
        './app.js'
    ],
    output: {
        path: path.join(__dirname, '../app/static/dist'),
        filename: "[name].bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            hash: true,
            title: 'Google Garage',
            filename: '../../templates/index.html',
            template: '../web/index.html'
        })
    ]
}