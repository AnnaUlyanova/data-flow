
import React from 'react'
import ReactDOM from 'react-dom'
import { BarChart } from 'react-d3-components'

function ByCategory ({
  categories,
  allCategoriesData,
  showDataForCategory,
  yearsForSelectedCategory,
  totalExpensesForSelectedCategory,
  averageExpensesForSelectedCategory,
  totalDataForD3,
  averageDataForD3,
  showTotalData,
  totalOrAverageDataForD3,
  toggledDataForD3,
  currentCategory
}) {

  if (!categories) {
    return (
      <p>No data available</p>
    )
  }

  function handleOnChange(event, toggledData) {
    const selectedCategory = event.target.value
    return showDataForCategory(allCategoriesData, selectedCategory, toggledData)
  }

  return (
    <div>
      <h1>Annual expenses for a selected category</h1>
      <select onChange={handleOnChange}>
        {categories.map((category) =>
          <option value={category}>{category}</option>
        )}
      </select>
      <button onClick={(event)=>handleOnChange(event, totalDataForD3)}>Show total annual expenses for {currentCategory}</button>
      <button onClick={(event)=>handleOnChange(event, averageDataForD3)}>Show average annual expenses for {currentCategory}</button>
//TODO abstract BarChart
      <BarChart
            data={toggledDataForD3}
            width={900}
            height={400}
            margin={{top: 10, bottom: 50, left: 50, right: 10}}
        />
    </div>
  )
}

 export default ByCategory
