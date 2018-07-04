import React from 'react'
import ReactDOM from 'react-dom'

import ByMonths from './containers/By-Months'
import ByCategory from './containers/By-Category'

function App () {
  return (
    <div>
      <h1>Hello, world!</h1>
      <ByMonths />
      <ByCategory />
    </div>
  )
}

 export default App
