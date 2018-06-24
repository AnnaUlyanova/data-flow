const path = require('path')

module.exports = {
  entry: './index.js',
  output: {
    path: path.join(__dirname, '../build'),
    filename: 'bundle.js'
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    rules: [{
      loader: 'babel-loader',
      options: {
              presets: ['es2015', 'react']
            }
      exclude: /node_modules/
    }]
  },
  devtool: 'source-map'
}
