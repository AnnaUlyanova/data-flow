import React from 'react'
import ReactDOM from 'react-dom'

import ByMonths from './containers/By-Months'
import ByCategory from './containers/By-Category'

function App () {
  return (
    <div>
      <h1>NZ Fees Statistics</h1>
      <ByMonths />
      <ByCategory />
    </div>
  )
}

 export default App
