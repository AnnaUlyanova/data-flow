
import React from 'react'
import ReactDOM from 'react-dom'

function ByMonths ({ monthlyExpenses }) {
  if (!monthlyExpenses) {
    return (
      <div>
        <h1>Null</h1>
      </div>
    )
  }
  return (
    <div>
      <h1>By Months</h1>
      <p>{monthlyExpenses}</p>
    </div>
  )
}

 export default ByMonths
