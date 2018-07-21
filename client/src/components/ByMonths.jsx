
import React from 'react'
import ReactDOM from 'react-dom'
import { BarChart } from 'react-d3-components'

function ByMonths ({ years, allYearsData, showDataForYear, monthsForSelectedYear, expensesForSelectedYear, dataForD3 }) {
console.log('allYearsData', allYearsData)
  if (!years || !allYearsData) {
    return (
      <p>No data available</p>
    )
  }

function handleOnChange(event) {
  const yearString = 'year '.concat(event.target.value)
  return showDataForYear(allYearsData, yearString, monthsForSelectedYear)
}
console.log('dataForD3', dataForD3)
  return (
    <div>
      <h1>Montly expenses for selected year</h1>
      <select onChange={handleOnChange}>
        {years.map((year) =>
          <option value={year}>{year}</option>
        )}
      </select>
      {monthsForSelectedYear &&
      <BarChart
            data={dataForD3}
            width={900}
            height={400}
            margin={{top: 10, bottom: 50, left: 50, right: 10}}
        />
      }
    </div>
  )
}

 export default ByMonths
