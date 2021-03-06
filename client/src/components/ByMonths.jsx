
import React from 'react'
import ReactDOM from 'react-dom'

function ByMonths ({ years, allYearsData, showDataForYear, monthsForSelectedYear,  expensesForSelectedYear }) {

  if (!years || !allYearsData) {
    return (
      <p>No data available</p>
    )
  }

  function handleOnChange(event) {
    const yearString = 'year '.concat(event.target.value)
    return showDataForYear(allYearsData, yearString)
  }
  return (
    <div>
      <h1>Montly expenses for selected year</h1>
      <select onChange={handleOnChange}>
        {years.map((year) =>
          <option value={year}>{year}</option>
        )}
      </select>
      {monthsForSelectedYear && <p>dataForSelectedYear: {monthsForSelectedYear}, {expensesForSelectedYear}</p>}
    </div>
  )
}

 export default ByMonths
